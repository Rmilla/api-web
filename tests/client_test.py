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

    def test_read_item(self):
        response = self.client.get(
            "/client/23")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "nom_client": "Andy", "prenom_client": "O", "email_client": "andy@hotmail.com", "telephone_client": "0789998998", "preferences_client": "Horreur", "adresse_livraison_client": "rue de la paix", "adresse_facturation_client": "rue de l'amour"
        })

    def test_read_all_item(self):
        response = self.client.get("/client")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

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
        response = self.client.post ("/create_client", json=new_client_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data.get('nom_client'), new_client_data['nom_client'])
        self.assertEqual(response_data.get('prenom_client'), new_client_data['prenom_client'])
        self.assertEqual(response_data.get('email_client'), new_client_data['email_client'])
        self.assertEqual(response_data.get('telephone_client'), new_client_data['telephone_client'])
        self.assertEqual(response_data.get('preferences_client'), new_client_data['preferences_client'])
        self.assertEqual(response_data.get('adresse_livraison_client'), new_client_data['adresse_livraison_client'])
        self.assertEqual(response_data.get('adresse_facturation_client'), new_client_data['adresse_facturation_client'])


unittest.main()
