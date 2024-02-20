import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from ..modules.bible import get_db
from pytest import fixture

from ..sql import models

from ..main import app

client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "postgresql://alexvanaxe@localhost/bible_project_test"

engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={},
        )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@fixture()
def populate_db():
    # For now for some unknown reason we have to put this two lines, since the pg_dump generates a file
    # that violates it's own import
    os.system("psql --host=localhost bible_project_test < data/ara.psql.sql")
    os.system("psql --host=localhost bible_project_test < data/ara.psql.sql")
    yield
    models.Base.metadata.drop_all(bind=engine)

def test_get_book(populate_db):
    response = client.get("/book/1")
    assert response.status_code == 200
