from fastapi import FastAPI, Depends
from app.settings import Settings, get_settings
from app.database import engine, Base
from app.api import router

# 创建数据库表
Base.metadata.create_all(bind=engine)

settings = get_settings()
app = FastAPI(title=settings.app_title)
app.include_router(router)
