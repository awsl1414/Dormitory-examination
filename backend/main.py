import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import api_router

app = FastAPI(
    title="查寝",
    description="查寝系统",
)

app.include_router(api_router)

# 允许跨域请求的设置
origins = [
    "http://localhost:5173",  # 这是您的前端开发服务器的地址，您可以根据需要进行修改
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def init_db():
    from db.database import Base, engine
    from models.models_users import User
    from models.models_sanitation import Sanitation
    from models.models_class_info import Grade, Major, Classes, Dorm

    Base.metadata.create_all(bind=engine)


init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
