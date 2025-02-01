import pytest
from fastapi.testclient import TestClient

def test_health_check(client):
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {"health_check": "OK"}

@pytest.mark.asyncio
async def test_chat_endpoint(client):
    request_data = {
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ]
    }
    response = client.post("/api/v1/chat", json=request_data)
    assert response.status_code == 200
    assert "response" in response.json()