from pydantic import BaseModel,ConfigDict
from datetime import datetime

# 新增模型 BookCreate
class BookCreate(BaseModel):
    title: str
    author: str
    stock: int

# 更新模型 BookUpdate
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    stock: int | None = None

# 响应模型 BookRead
class BookRead(BookCreate):
    id: int
    create_time: datetime
    update_time: datetime

    model_config = ConfigDict(from_attributes=True)
