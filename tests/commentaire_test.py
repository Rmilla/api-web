from fastapi.testclient import TestClient
import unittest
from datetime import datetime

# Importation des modules sys et os pour manipuler les chemins de fichiers et les variables d'environnement.
# Configuration du chemin d'accès au répertoire parent pour pouvoir importer l'application FastAPI.
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.main import app

class TestFastAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    # Test de la lecture d'un client spécifique via l'API.

    def test_read_item(self):
        response = self.client.get(
            "/commentaire/1")
        # Vérification des données reçues.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "date_publication_commentaire": "2023-11-28T11:35:53", "auteur_commentaire": "Test create", "titre_commentaire": "Test create"
        })
    # Test de la lecture de tout les commentaires.

    def test_read_all_item(self):
        response = self.client.get("/commentaire")
        # Vérification des données reçues.
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_commentaire(self):
        # Test de la création d'un commentaire via l'API.
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S")

        new_client_data = {
            # Définition des données du nouveau commentaire.
            "date_publication_commentaire": formatted_datetime,
            "auteur_commentaire": "Test create",
            "titre_commentaire": "Test create",
            "id_client": 6

        }
        # Envoi d'une requête POST à l'API pour créer un commentaire.
        response = self.client.post(
            "/create_commentaire", json=new_client_data)
        # Vérification de la réponse de l'API.
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data.get('date_publication_commentaire'),
                         new_client_data['date_publication_commentaire'])
        self.assertEqual(response_data.get('auteur_commentaire'),
                         new_client_data['auteur_commentaire'])
        self.assertEqual(response_data.get('titre_commentaire'),
                         new_client_data['titre_commentaire'])
        self.assertEqual(response_data.get('id_client'),
                         new_client_data['id_client'])

    def test_delete_commentaire(self):
        # Envoyer une requête DELETE
        response = self.client.delete("/commentaire_delete/1")
        # Vérifier que la suppression a réussi
        self.assertEqual(response.status_code, 200)

    def test_update_commentaire(self):
        # Test de la mise à jour des données d'un commentaire via l'API.
        client_data_update = {
            "auteur_commentaire": "TestUpdate",

        }
        # Envoi d'une requête PUT pour mettre à jour les données du commentaire 2.
        response = self.client.put(
            "/update_commentaire/2", json=client_data_update)
        # Vérification de la mise à jour des données.
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(
            response_data['auteur_commentaire'], client_data_update['auteur_commentaire'])


if __name__ == "__main__":
    unittest.main()
