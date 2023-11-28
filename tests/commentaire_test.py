from fastapi.testclient import TestClient
# from unittest import main, TestCase
import unittest
import sys
import os
from datetime import datetime

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.main import app

class TestFastAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_item(self):
        response = self.client.get(
            "/commentaire/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
           "date_publication_commentaire":"2023-11-24T12:34:25", "auteur_commentaire": "Andy le lecteur", "titre_commentaire":"Incroyable !"
        })

    def test_read_all_item(self):
        response = self.client.get("/commentaire")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_client(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S")

        new_client_data = {
           "date_publication_commentaire": formatted_datetime,
           "auteur_commentaire":"Test create",
           "titre_commentaire":"Test create"
        }
        response = self.client.post("/create_commentaire", json=new_client_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data.get('date_publication_commentaire'),
                         new_client_data['date_publication_commentaire'])
        self.assertEqual(response_data.get('auteur_commentaire'),
                         new_client_data['auteur_commentaire'])
        self.assertEqual(response_data.get('titre_commentaire'),
                         new_client_data['titre_commentaire'])

    def test_delete_client(self):
        # Envoyer une requête DELETE
        response = self.client.delete("/commentaire_delete/3")
        # Vérifier que la suppression a réussi
        self.assertEqual(response.status_code, 200)

    def test_update_client(self):
        client_data_update = {
            "auteur_commentaire":"TestUpdate",
            
        }
        response = self.client.put(
            "/update_commentaire/9", json=client_data_update)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['auteur_commentaire'], client_data_update['auteur_commentaire'])
        


if __name__ == "__main__":
    unittest.main()