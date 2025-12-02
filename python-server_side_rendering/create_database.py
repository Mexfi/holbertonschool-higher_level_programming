import sqlite3
import os

def create_database():
    """Creates and populates the SQLite database file (products.db)."""
    DB_FILE = 'products.db'
    conn = None

    # --- FIX: Delete existing DB file before connecting ---
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Removed existing {DB_FILE} to ensure a clean start.")
    # --------------------------------------------------------

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # 1. Create the Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # 2. Insert initial data
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        
        conn.commit()
        print(f"Database '{DB_FILE}' created and populated successfully.")
        
    except sqlite3.Error as e:
        print(f"Database error during setup: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
