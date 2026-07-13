import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cadastro(self):
        response = self.client.post(
            "/adicionar",
            data={
                "titulo": "Teste",
                "descricao": "Teste Automatizado",
                "responsavel": "Iago"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()