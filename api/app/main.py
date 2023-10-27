from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from sql import crud, models, schemas
from sql.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
        "http://localhost:5173"
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )

@app.get("/versicle/{versicle_id}", response_model=schemas.Verse)
async def versicle(versicle_id: int, db: Session = Depends(get_db)):
    db_versicle = crud.get_verse(db, verse=versicle_id)

    return db_versicle
