from typing import List

from langchain_core.documents import Document
from langchain_milvus import Milvus, BM25BuiltInFunction
from pymilvus import IndexType, MilvusClient, Function
from pymilvus.client.types import MetricType, DataType, FunctionType

from documents.markdown_parser import MarkdownParser
from llm_models.embeddings_model import bge_embedding
from utils.env_utils import MILVUS_URI, COLLECTION_NAME


DEFAULT_PARTITIONS = ["lithography", "etch", "deposition", "cmp", "metrology", "general"]


class MilvusVectorSave:
    """把新的document数据插入到数据库中"""

    def __init__(self) -> object:
        """自定义collection的索引"""
        self.vector_store_saved: Milvus = None

    def ensure_collection_exists(self, partitions: List[str] = None):
        """幂等安全建表：若集合已存在则跳过，绝不执行误删操作。支持工艺分区初始化。"""
        client = MilvusClient(uri=MILVUS_URI)
        existing = client.list_collections()

        if COLLECTION_NAME not in existing:
            schema = client.create_schema()
            schema.add_field(field_name='id', datatype=DataType.INT64, is_primary=True, auto_id=True)
            schema.add_field(field_name='text', datatype=DataType.VARCHAR, max_length=6000, enable_analyzer=True,
                             analyzer_params={"tokenizer": "jieba", "filter": ["cnalphanumonly"]})
            schema.add_field(field_name='category', datatype=DataType.VARCHAR, max_length=1000)
            schema.add_field(field_name='source', datatype=DataType.VARCHAR, max_length=1000)
            schema.add_field(field_name='filename', datatype=DataType.VARCHAR, max_length=1000)
            schema.add_field(field_name='filetype', datatype=DataType.VARCHAR, max_length=1000)
            schema.add_field(field_name='title', datatype=DataType.VARCHAR, max_length=1000)
            schema.add_field(field_name='category_depth', datatype=DataType.INT64)
            schema.add_field(field_name='sparse', datatype=DataType.SPARSE_FLOAT_VECTOR)
            schema.add_field(field_name='dense', datatype=DataType.FLOAT_VECTOR, dim=1024)

            bm25_function = Function(
                name="text_bm25_emb",
                input_field_names=["text"],
                output_field_names=["sparse"],
                function_type=FunctionType.BM25,
            )
            schema.add_function(bm25_function)
            index_params = client.prepare_index_params()

            index_params.add_index(
                field_name="sparse",
                index_name="sparse_inverted_index",
                index_type="SPARSE_INVERTED_INDEX",
                metric_type="BM25",
                params={
                    "inverted_index_algo": "DAAT_MAXSCORE",
                    "bm25_k1": 1.2,
                    "bm25_b": 0.75
                },
            )
            index_params.add_index(
                field_name="dense",
                index_name="dense_inverted_index",
                index_type=IndexType.HNSW,
                metric_type=MetricType.IP,
                params={"M": 16, "efConstruction": 64}
            )

            client.create_collection(
                collection_name=COLLECTION_NAME,
                schema=schema,
                index_params=index_params
            )

        # 检查并初始化工艺分区（Partitions）
        parts = partitions or DEFAULT_PARTITIONS
        for part in parts:
            try:
                if not client.has_partition(collection_name=COLLECTION_NAME, partition_name=part):
                    client.create_partition(collection_name=COLLECTION_NAME, partition_name=part)
            except Exception:
                pass

        try:
            client.load_collection(collection_name=COLLECTION_NAME)
        except Exception:
            pass

    def recreate_collection(self, force: bool = False):
        """清库重建操作：必须显式传入 force=True，防止生产环境误删全量知识库。"""
        if not force:
            raise RuntimeError("【安全拦截】清空重建集合存在数据全部丢失风险，必须显式指定 force=True 确认操作！")

        client = MilvusClient(uri=MILVUS_URI)
        if COLLECTION_NAME in client.list_collections():
            try:
                client.release_collection(collection_name=COLLECTION_NAME)
                client.drop_index(collection_name=COLLECTION_NAME, index_name='sparse_inverted_index')
                client.drop_index(collection_name=COLLECTION_NAME, index_name='dense_inverted_index')
            except Exception:
                pass
            client.drop_collection(collection_name=COLLECTION_NAME)

        self.ensure_collection_exists()

    def create_collection(self, force: bool = False):
        """兼容旧脚本接口；默认安全幂等创建，若需重建请传 force=True。"""
        if force:
            self.recreate_collection(force=True)
        else:
            self.ensure_collection_exists()

    def create_connection(self):
        """创建一个Connection： milvus + langchain。先做幂等安全建表检查。"""
        try:
            self.ensure_collection_exists()
        except Exception:
            pass

        self.vector_store_saved = Milvus(
            embedding_function=bge_embedding,
            collection_name=COLLECTION_NAME,
            builtin_function=BM25BuiltInFunction(),
            vector_field=['dense', 'sparse'],
            consistency_level="Strong",
            auto_id=True,
            connection_args={"uri": MILVUS_URI}
        )

    def add_documents(self, datas: List[Document], partition_name: str = None):
        """把新的document保存到Milvus中，支持写入指定工艺分区"""
        kwargs = {}
        if partition_name:
            kwargs["partition_name"] = partition_name
        self.vector_store_saved.add_documents(datas, **kwargs)



if __name__ == '__main__':
    # 解析文件内容
    file_path = r'E:\Agent_Learn\RAG项目\RAG项目\RAG企业知识库项目\RAG_PROJECT\datas\md\tech_report_0tfhhamx.md'
    parser = MarkdownParser()
    docs = parser.parse_markdown_to_documents(file_path)

    # 写入Milvus数据库
    mv = MilvusVectorSave()
    mv.create_collection()
    mv.create_connection()
    mv.add_documents(docs)

    client = mv.vector_store_saved.client
    # 得到表结构
    desc_collection = client.describe_collection(
        collection_name=COLLECTION_NAME
    )
    print('表结构是: ', desc_collection)

    # 得到当前表的，所有的index
    res = client.list_indexes(
        collection_name=COLLECTION_NAME
    )
    print('表中的所有索引：', res)

    if res:
        for i in res:
            # 得到索引的描述
            desc_index = client.describe_index(
                collection_name=COLLECTION_NAME,
                index_name=i
            )
            print(desc_index)

    result = client.query(
        collection_name=COLLECTION_NAME,
        filter="category == 'Title'",  # 查询 category == 'Title' 的所有数据
        output_fields=['text', 'category', 'filename']  # 指定返回的字段
    )

    print('测试 过滤查询的结果是: ', result)
