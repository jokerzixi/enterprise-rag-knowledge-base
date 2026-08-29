from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graph2.graph_2 import graph

# from graph_2 import graph  # 确保你的图实例能导入

app = FastAPI()

# 允许跨域请求配置（让本地网页能访问 API）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名访问，测试阶段图方便
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    inputs = {"question": request.question}

    final_response = "我没有找到答案，请稍后再试。"
    # 运行图网络
    # 注意：这里假设 graph.stream 是同步的。如果是异步，需要改用 async for 和 astream()
    for output in graph.stream(inputs):
        for key, value in output.items():
            if key == "generate":
                final_response = value["generation"]

    return {"answer": final_response}