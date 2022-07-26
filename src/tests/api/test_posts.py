from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_posts():
    response = client.get("/api/posts")
    assert response.status_code == 200
