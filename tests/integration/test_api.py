
import pytest
from src.api.rest_api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_content_endpoint(client):
    response = client.post('/generate', json={
        "topic": "Test Topic",
        "length": 100,
        "style": "formal"
    })
    assert response.status_code == 201
    assert 'content' in response.json

def test_discover_content_endpoint(client):
    response = client.get('/discover')
    assert response.status_code == 200
    assert 'ideas' in response.json
