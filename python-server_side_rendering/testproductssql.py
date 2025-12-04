import unittest
from app import app
import json

class TestProductSQL(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_sql_id(self):
        """Test valid product ID"""
        response = self.app.get('/?source=sql&id=1')
        self.assertEqual(response.status_code, 200)
        product = json.loads(response.data)
        self.assertEqual(product['id'], 1)
        self.assertEqual(product['name'], 'Laptop')

    def test_invalid_sql_id(self):
        """Test invalid product ID"""
        response = self.app.get('/?source=sql&id=999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Product not found', response.data)

if __name__ == '__main__':
    unittest.main()
