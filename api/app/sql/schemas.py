from pydantic import BaseModel, ConfigDict


class VerseBase(BaseModel):
    chapter: int
    verse: int
    text: str


class BookBase(BaseModel):
    name:  str
    acronym: str


class Verse(VerseBase):
    id: int
    book_id: int

    books: BookBase

    model_config = ConfigDict(from_attributes=True)


class Book(BookBase):
    id: int
    book_reference_id: int
    testament_reference_id: int

    verses: list[Verse] = []

    model_config = ConfigDict(from_attributes=True)


class TestamentBase(BaseModel):
    name: str
    description: str


class Testament(TestamentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
