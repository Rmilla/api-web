from fastapi.testclient import TestClient
from src.main import app
import unittest
class TestFastAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    def test_create_ouvrage(self):
        new_ouvrage_data = {
            "id_ouvrage": 0,
            "titre_ouvrage": "string",
            "auteur_ouvrage": "string",
            "isbn_ouvrage": "string",
            "langue_ouvrage": "string",
            "prix_ouvrage": 0,
            "date_parution_ouvrage": "string",
            "categorie_ouvrage": "string",
            "date_disponibilite_libraire_ouvrage": "string",
            "date_disponibilite_particulier_ouvrage": "string",
            "image_ouvrage": "string",
            "table_des_matieres_ouvrage": "string",
            "mot_cle_ouvrage": "string",
            "description_ouvrage": "string"
        }
        response = self.client.post("/models/ouvrage/", json=new_ouvrage_data)
        assert response.status_code == 201
        assert response.json == new_ouvrage_data

    def test_update_ouvrage(self):
        response = self.client.patch("/models/ouvrage/1", json={"titre_ouvrage": "Updated Title"})
        ouvrage_data = {
            "id_ouvrage": 0,
            "titre_ouvrage": "Updated Title",
            "auteur_ouvrage": "string",
            "isbn_ouvrage": "string",
            "langue_ouvrage": "string",
            "prix_ouvrage": 0,
            "date_parution_ouvrage": "string",
            "categorie_ouvrage": "string",
            "date_disponibilite_libraire_ouvrage": "string",
            "date_disponibilite_particulier_ouvrage": "string",
            "image_ouvrage": "string",
            "table_des_matieres_ouvrage": "string",
            "mot_cle_ouvrage": "string",
            "description_ouvrage": "string"
        }
        assert response.status_code == 200
        assert response.json == ouvrage_data

    def test_delete_item(self):
        response = self.client.delete("/models/ouvrage/1")

        assert response.status_code == 200
        assert response.json() == {"message": "Ouvrage deleted successfully"}

    def test_read_database(self):
        response = self.client.get("/models/ouvrage")
        assert response.status_code == 200
        assert len(response.json()) > 0



    def test_read_ouvrage(self):
        response = self.client.get("/models/ouvrage/1")

        assert response.status_code == 200
        assert response.json()["id"] == 1

        response = self.client.get("/models/ouvrage/", params={"titre_ouvrage": "Example Title"})

        assert response.status_code == 200
        assert response.json()["titre_ouvrage"] == "Example Title" 

        response = self.client.get("/models/ouvrage/", params={"isbn_ouvrage": "1234"})

        assert response.status_code == 200
        assert response.json()["isbn_ouvrage"] == "1234" 

