import sqlite3
import os

def create_database():
    """products.db faylını yaradır və ilkin məlumatlarla doldurur."""
    DB_FILE = 'products.db'
    conn = None

    # Əgər mövcuddursa, verilənlər bazası faylını silirik ki, təmiz başlanğıc olsun
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # 1. Products cədvəlinin yaradılması
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # 2. İlkin məlumatların daxil edilməsi
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')

        conn.commit()
        print(f"'{DB_FILE}' verilənlər bazası yaradıldı və dolduruldu.")

    except sqlite3.Error as e:
        print(f"Verilənlər bazasının qurulması zamanı xəta: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
