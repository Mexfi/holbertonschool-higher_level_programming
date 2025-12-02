import unittest
import json
from app import app  # Import your Flask app

class TestProductSQL(unittest.TestCase):
    
    def setUp(self):
        """This method is called before each test."""
        self.app = app.test_client()
        self.app.testing = True

        # You can optionally set up the database here or reset it between tests
        # Create and populate the SQLite database (This can also be in a setup.py)
        self.create_test_db()

    def tearDown(self):
        """This method is called after each test."""
        # Clean up any test-specific data or reset database after tests
        self.clean_up_db()

    def create_test_db(self):
        """Set up the database with test data (can be used in setUp)."""
        import sqlite3
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
        conn.close()

    def clean_up_db(self):
        """Clean up the database after each test."""
        import sqlite3
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Products')  # Clear the products table
        conn.commit()
        conn.close()

    def test_valid_sql_id(self):
        """Test for valid product ID in the database."""
        response = self.app.get('/?source=sql&id=1')
        self.assertEqual(response.status_code, 200)
        product = json.loads(response.data)
        self.assertEqual(product['id'], 1)
        self.assertEqual(product['name'], 'Laptop')
        self.assertEqual(product['category'], 'Electronics')
        self.assertEqual(product['price'], 799.99)

    def test_invalid_sql_id(self):
        """Test for an invalid product ID that doesn't exist in the database."""
        response = self.app.get('/?source=sql&id=999')  # Non-existing ID
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Product not found', response.data)

if __name__ == '__main__':
    unittest.main()
