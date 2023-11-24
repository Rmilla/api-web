import unittest
from fastapi.testclient import TestClient
from src.main import app


class TestFastAPIValidation(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_model_validation_client(self):
        response = self.client.post(
            "/create_item", json={"nom_client": "example", "prenom_client": "test", "email_client": "test", "telephone_client": "test", "preferences_client": "test", "adresse_livraison_client": "test", "adresse_facturation_client": "test"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
                         "nom_client": "example", "prenom_client": "test", "email_client": "test", "telephone_client": "test", "preferences_client": "test", "adresse_livraison_client": "test", "adresse_facturation_client": "test"})
