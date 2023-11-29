from fastapi.testclient import TestClient
import unittest


class TestThemeOuvrageRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_theme_ouvrage(self):
        response = self.client.get("/theme_ouvrage/1/2")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["id_ouvrage"], 1)
        self.assertEqual(response_data["id_theme"], 2)
        self.assertEqual(response_data["nom_theme"], "Science-fiction")

    def test_get_theme_ouvrage_404(self):
        response = self.client.get("/theme_ouvrage/100/200")
        self.assertEqual(response.status_code, 404)

    def test_get_theme_ouvrage_400_ouvrage_id_invalid(self):
        response = self.client.get("/theme_ouvrage/0/2")
        self.assertEqual(response.status_code, 400)

    def test_get_theme_ouvrage_400_theme_id_invalid(self):
        response = self.client.get("/theme_ouvrage/1/0")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
