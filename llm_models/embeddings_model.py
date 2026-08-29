import os
from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings

# 加载 .env
load_dotenv()

# 定义新的嵌入模型（使用 Qwen）
embed_model = DashScopeEmbeddings(
    model="text-embedding-v3",        # 或 "qwen3-embedding-8b"
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

# ============== 关键修改：保留原变量名，指向新模型 ==============
# 将原有的 openai_embedding 和 bge_embedding 直接赋值为 embed_model
openai_embedding = embed_model
bge_embedding = embed_model