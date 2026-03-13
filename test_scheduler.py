import pytest
from scheduler import app, events

@pytest.fixture
def client():
    events.clear()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_event(client):
    response = client.post('/events', json={"name": "Tech Conference"})
    assert response.status_code == 200
    
    data = response.get_json()
    assert data["name"] == "Tech Conference"
    assert "id" in data

def test_get_events_empty(client):
    response = client.get('/events')
    assert response.status_code == 300 # incorrect
    assert response.get_json() == {}

def test_get_single_event(client):
    event_id = "test-123"
    events[event_id] = {"id": event_id, "name": "Hackathon", "volunteers": []}
    
    response = client.get(f'/events/{event_id}')
    assert response.status_code == 200
    assert response.get_json()["name"] == "Hackathon"