from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..sql import crud, schemas
from ..sql.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/versicle/{versicle_id}", response_model=schemas.Verse)
async def versicle(versicle_id: int, db: Session = Depends(get_db)):
    db_versicle = crud.get_verse(db, verse=versicle_id)

    return db_versicle

@router.get("/book/{book_id}", response_model=schemas.Book)
async def book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book=book_id)

    return db_book

@router.get("/chapter/{book_id}/{chapter_id}", response_model=list[schemas.Verse])
async def chapter(book_id: int, chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = crud.get_chapter(db, book=book_id, chapter=chapter_id)

    return db_chapter
