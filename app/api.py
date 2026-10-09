from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import BookCreate, BookUpdate, BookRead
from app.service import BookService

router = APIRouter(prefix="/books", tags=["图书管理"])

# 新增图书 POST
@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return BookService.create_book(db, book)

# 分页列表 GET
@router.get("/", response_model=list[BookRead])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return BookService.get_book_list(db, skip, limit)

# 详情 GET /{id}
@router.get("/{id}", response_model=BookRead)
def get_book(id: int, db: Session = Depends(get_db)):
    book = BookService.get_book_by_id(db, id)
    if not book:
        raise HTTPException(status_code=404,detail="该图书不存在")
    return book

# 更新 PUT
@router.put("/{id}", response_model=BookRead)
def update_book(id: int, book: BookUpdate, db: Session = Depends(get_db)):
    book =  BookService.update_book(db, id, book)
    if not book:
        raise HTTPException(status_code=404,detail="该图书不存在")
    return book

# 删除 DELETE
@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_book(id: int, db: Session = Depends(get_db)):
    book = BookService.delete_book(db, id)
    if not book:
        raise HTTPException(status_code=404, detail="该图书不存在")
    return {"msg": "删除成功"}
