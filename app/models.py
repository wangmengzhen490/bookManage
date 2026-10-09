from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, comment="图书名称")
    author = Column(String(50), nullable=False, comment="作者")
    stock = Column(Integer, default=0, comment="库存")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
