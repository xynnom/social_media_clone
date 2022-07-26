"""conftest.py"""

from typing import Generator
import sys
import pytest

from fastapi.testclient import TestClient
from arcu.db.database import SessionLocal
from main import app


@pytest.fixture(scope="session")
def database() -> Generator:
    """DB session"""
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Test Client"""
    with TestClient(app) as test_client:
        yield test_client
