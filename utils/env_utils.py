import os

from dotenv import load_dotenv

load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
MINERU_API_TOKEN = os.getenv('MINERU_API_TOKEN')

MILVUS_URI = os.getenv('MILVUS_URI', 'http://127.0.0.1:19530')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 't_collection01')

# 会话持久化：auto | redis | sqlite | memory
SESSION_BACKEND = os.getenv('SESSION_BACKEND', 'auto')
REDIS_URL = (os.getenv('REDIS_URL') or '').strip()
SESSION_TTL_SECONDS = int(os.getenv('SESSION_TTL_SECONDS', '604800'))  # 7 天
