import sqlite3
import os

def create_database():
    """products.db faylını yaradır, mövcud faylı silir və ilkin məlumatlarla doldurur."""
    DB_FILE = 'products.db'
    conn = None

    # --- Zəmanətli Təmiz Başlanğıc ---
    if os.path.exists(DB_FILE):
        try:
            os.remove(DB_FILE)
            print(f"Mövcud '{DB_FILE}' faylı uğurla silindi.")
        except OSError as e:
            # Faylın silinməsi zamanı icazə xətası ola bilər
            print(f"Xəbərdarlıq: Mövcud '{DB_FILE}' faylını silmək mümkün olmadı: {e}")
    # ---------------------------------

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
        # OR IGNORE istifadə edilmir, çünki faylı silmişik, amma INSERT edirik.
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        
        conn.commit()
        print(f"Database '{DB_FILE}' uğurla yaradıldı və dolduruldu.")
        
    except sqlite3.Error as e:
        print(f"Verilənlər bazası əməliyyatı zamanı xəta: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
