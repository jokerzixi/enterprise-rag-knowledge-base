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

# Laya System-1 意图路由（可选；关闭或失败时回退 DeepSeek）
LAYA_ENABLED = (os.getenv('LAYA_ENABLED', 'false') or '').strip().lower() in (
    '1', 'true', 'yes', 'on',
)
LAYA_SERVER_URL = (os.getenv('LAYA_SERVER_URL') or 'http://127.0.0.1:8000').strip()
LAYA_MODEL = (os.getenv('LAYA_MODEL') or 'convaiinnovations/laya-multilingual').strip()
LAYA_API_KEY = (os.getenv('LAYA_API_KEY') or '').strip()
try:
    LAYA_CONFIDENCE_MIN = float(os.getenv('LAYA_CONFIDENCE_MIN', '0.55'))
except ValueError:
    LAYA_CONFIDENCE_MIN = 0.55
try:
    LAYA_TIMEOUT_SECONDS = float(os.getenv('LAYA_TIMEOUT_SECONDS', '0.5'))
except ValueError:
    LAYA_TIMEOUT_SECONDS = 0.5
