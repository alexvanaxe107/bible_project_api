from sqlalchemy.orm import Session

from . import models, schemas


def get_book(db: Session, book: str):
    return db.query(models.Book).filter(models.Book.id == book).first()

def get_chapter(db: Session, book: str, chapter: str):
    return db.query(models.Verse).filter((models.Verse.book_id == book) & (models.Verse.chapter == chapter)).all()

def get_verse(db: Session, verse: str):
    return db.query(models.Verse).filter(models.Verse.id == verse).first()
