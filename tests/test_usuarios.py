import unittest
from app import main

class TestUsuariosAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = main.test_client()

    def test_get_usuarios(self):
        response = self.client.get('/usuarios')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_usuario(self):
        response = self.client.get('/usuarios/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id_usuario', response.json)

    def test_get_usuario_not_found(self):
        response = self.client.get('/usuarios/9999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
