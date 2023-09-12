import pytest
froma app import app

@pytest.fixture
def clinet():
		app.config['Testinhg'] =true
		with app.test_client() as client :
		yield client
		
def test_appworking(client):
			response = client.get('/')
			assert response.status_code == 200
			assert b "HelooWo" in response.data
			
