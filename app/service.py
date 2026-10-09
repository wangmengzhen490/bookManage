from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookCreate, BookUpdate

class BookService:
    # 图书新增
    @staticmethod
    def create_book(db: Session, obj: BookCreate):
        book = Book(**obj.model_dump())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    # 单本图书
    @staticmethod
    def get_book_by_id(db: Session, id: int):
        book = db.query(Book).filter(Book.id == id).first()
        if not book:
            return None
        return book

    @staticmethod
    def get_book_list(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Book).offset(skip).limit(limit).all()

    # 图书编辑
    @staticmethod
    def update_book(db: Session, id: int, obj: BookUpdate):
        book = BookService.get_book_by_id(db, id)
        if not book:
            return None
        for k, v in obj.model_dump().items():
            setattr(book, k, v)
        db.commit()
        db.refresh(book)
        return book

    # 图书删除
    @staticmethod
    def delete_book(db: Session, id: int):
        book = db.query(Book).filter(Book.id == id).first()
        if not book:
            return None
        db.delete(book)
        db.commit()
        return book
