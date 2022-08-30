from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.core.database import Base
from app.core.dependencies import get_db
from app.main import app
from tests.database import TestingSessionLocal, engine


@pytest.fixture(scope="session")
def db() -> Generator:
    engine.execute("CREATE DATABASE IF NOT EXISTS test")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client(db) -> Generator:
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
