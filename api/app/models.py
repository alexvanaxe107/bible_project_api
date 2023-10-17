from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship

from .database import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    book_reference_id = Column(Integer)
    testament_reference_id = Column(Integer, ForeignKey("testament.id"))
    name = Column(String)
    acronym = Column(string)

    verses = relationship("Verse", back_populates="books")

class Testament(Base):
    __tablename__ = "testament"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    verses = relationship("Verse", back_populates="testmaments")


class Verse(Base):
    __tablename__ = "verse"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String)

    books = relationship("Book", back_populates="verses")
    testaments = relationship("Testaments", back_populates="verses")
