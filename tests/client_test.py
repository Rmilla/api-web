
from fastapi.testclient import TestClient
# from unittest import main, TestCase
import unittest
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from src.main import app

class TestFastAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_client(self):
        new_client_data = {
            "nom_client": "Daenerys",
            "prenom_client": "Targaryen",
            "email_client": "khaleesi@dragons.com",
            "telephone_client": "0712345678",
            "preferences_client": "Aventure",
            "adresse_livraison_client": "Dragonstone",
            "adresse_facturation_client": "Dragonstone"
        }
        response = self.client.post("/create_client", json=new_client_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data.get('nom_client'),
                         new_client_data['nom_client'])
        self.assertEqual(response_data.get('prenom_client'),
                         new_client_data['prenom_client'])
        self.assertEqual(response_data.get('email_client'),
                         new_client_data['email_client'])
        self.assertEqual(response_data.get('telephone_client'),
                         new_client_data['telephone_client'])
        self.assertEqual(response_data.get('preferences_client'),
                         new_client_data['preferences_client'])
        self.assertEqual(response_data.get('adresse_livraison_client'),
                         new_client_data['adresse_livraison_client'])
        self.assertEqual(response_data.get(
            'adresse_facturation_client'), new_client_data['adresse_facturation_client'])

    def test_read_item(self):
        response = self.client.get(
            "/client/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "nom_client": "Daenerys", "prenom_client": "Targaryen", "email_client": "khaleesi@dragons.com", "telephone_client": "0712345678", "preferences_client": "Aventure", "adresse_livraison_client": "Dragonstone", "adresse_facturation_client": "Dragonstone"
        })

    def test_read_all_item(self):
        response = self.client.get("/client")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_delete_client(self):
        # Envoyer une requête DELETE
        response = self.client.delete("/delete_client/2")
        # Vérifier que la suppression a réussi
        self.assertEqual(response.status_code, 200)

    def test_update_client(self):
        client_data_update = {
            "nom_client": "NomUpdate",
            "prenom_client": "PrenomUpdate",
            "email_client": "emailUpdate",
            "telephone_client": "telephoneUpdate",
            "preferences_client": "preferenceUpdate",
            "adresse_livraison_client": "Winterfel",
            "adresse_facturation_client": "Thrones"
        }
        response = self.client.put(
            "/update_client/2", json=client_data_update)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['nom_client'],
                         client_data_update['nom_client'])
        self.assertEqual(
            response_data['prenom_client'], client_data_update['prenom_client'])
        self.assertEqual(
            response_data['email_client'], client_data_update['email_client'])
        self.assertEqual(
            response_data['telephone_client'], client_data_update['telephone_client'])
        self.assertEqual(
            response_data['preferences_client'], client_data_update['preferences_client'])
        self.assertEqual(response_data['adresse_livraison_client'],
                         client_data_update['adresse_livraison_client'])
        self.assertEqual(response_data['adresse_facturation_client'],
                         client_data_update['adresse_facturation_client'])


if __name__ == "__main__":
    unittest.main()
