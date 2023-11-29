from fastapi.testclient import TestClient
import unittest
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.main import app

class TestThemeRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_theme(self):
        response = self.client.get("/theme/1")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["theme_id"], 1)
        self.assertEqual(response_data["nom_theme"], "Horreur")

    def test_get_all_theme(self):
        response = self.client.get("/theme")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_theme(self):
        new_theme_data = {"theme_id": "4", "nom_theme": "Fantasy"}
        response = self.client.post("/create_theme", json=new_theme_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data["nom_theme"], new_theme_data["nom_theme"])
        self.assertEqual(response_data["theme_id"], new_theme_data["theme_id"])

    def test_update_theme(self):
        theme_data_update = {"theme_id": "2", "nom_theme": "Fantasy Update"}
        response = self.client.put("/update_theme/1", json=theme_data_update)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["theme_id"], theme_data_update["theme_id"])
        self.assertEqual(response_data["nom_theme"], theme_data_update["nom_theme"])

    def test_delete_theme(self):
        response = self.client.delete("/delete_theme/2")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
