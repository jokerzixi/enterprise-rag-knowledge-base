from langchain_core.tools import create_retriever_tool
from documents.milvus_db import MilvusVectorSave

mv = MilvusVectorSave()
mv.create_connection()
retriever = mv.vector_store_saved.as_retriever(
    search_type='similarity',  # 仅返回相似度超过阈值的文档
    search_kwargs={
        "k": 4,
        "score_threshold": 0.1,
        "ranker_type": "rrf",
        "ranker_params": {"k": 100},
        'filter': {"category": "content"}
    }
)


def get_partition_retriever(partition_names=None, k: int = 4):
    """支持指定半导体工艺分区检索的检索器工厂"""
    search_kwargs = {
        "k": k,
        "score_threshold": 0.1,
        "ranker_type": "rrf",
        "ranker_params": {"k": 100},
        'filter': {"category": "content"}
    }
    if partition_names:
        search_kwargs["partition_names"] = partition_names if isinstance(partition_names, list) else [partition_names]

    return mv.vector_store_saved.as_retriever(
        search_type='similarity',
        search_kwargs=search_kwargs
    )


retriever_tool = create_retriever_tool(
    retriever,
    'rag_retriever',
    '搜索并返回关于 ‘半导体和芯片’ 的信息, 内容涵盖：半导体和芯片的封装、测试、光刻胶等'
)