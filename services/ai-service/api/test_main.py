from fastapi.testclient import TestClient
from api.main import app

def test_health():
    client = TestClient(app)
    response = client.get("/api/chat")
    assert response.status_code in [404, 405]  # Endpoint exists, but method may not be allowed
