from langchain_community.tools import TavilySearchResults
from langchain_openai import ChatOpenAI

from utils.env_utils import DEEPSEEK_API_KEY

llm = ChatOpenAI(
    temperature=0.5,
    model='deepseek-chat',
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com")


web_search_tool = TavilySearchResults(max_results=2)

