from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test GET /
def test_root_redirect():
    # Arrange
    # (client déjà prêt)
    # Act
    response = client.get("/")
    # Assert
    assert response.status_code == 200 or response.status_code == 307

# Test GET /activities
def test_get_activities():
    # Arrange
    # (client déjà prêt)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Vérifie qu'au moins une activité attendue est présente
    assert any(key in data for key in ["Art Studio", "Robotics Club", "Drama Club"])  # Adapter selon les activités réelles
