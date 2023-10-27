from sqlalchemy.orm import Session

from . import models, schemas


def get_verse(db: Session, verse: str):
    return db.query(models.Verse).filter(models.Verse.id == verse).first()
