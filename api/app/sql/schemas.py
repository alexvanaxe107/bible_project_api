from pydantic import BaseModel


class VerseBase(BaseModel):
    chapter: int
    verse: int
    text: str


class Verse(VerseBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name:  str
    acronym: str


class Book(BookBase):
    id: int
    book_reference_id: int
    testament_reference_id: int

    verses: list[Verse] = []

    class Config:
        orm_mode = True


class TestamentBase(BaseModel):
    name: str
    description: str


class Testament(TestamentBase):
    id: int

    class Config:
        orm_mode = True
