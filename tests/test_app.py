import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Named Entity Recognition" in response.data

def test_submit_text(client, mocker):
    mock_nlp = mocker.patch('app.nlp', return_value=[
        {"word": "test", "start": 0, "end": 4}
    ])
    response = client.post('/submit_text', json={"input_text": "test"})
    assert response.status_code == 200
    assert "<mark>test</mark>" in response.data.decode()