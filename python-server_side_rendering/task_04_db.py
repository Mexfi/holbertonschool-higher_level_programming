# ... (digər importlar və read_json_data, read_csv_data funksiyaları) ...

def read_sql_data(product_id=None):
    """SQLite verilənlər bazasından məhsul məlumatlarını gətirir."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        # conn.row_factory - nəticə sətirlərini sözlük kimi əldə etməyə imkan verir
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()

        if product_id is None:
            # Bütün məhsulları gətir
            cursor.execute("SELECT id, name, category, price FROM Products")
        else:
            # ID-yə görə məhsulu gətir (təhlükəsiz filtrasiya)
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))

        # sqlite3.Row obyektlərini sözlüklərin siyahısına çevir
        data = [dict(row) for row in cursor.fetchall()]
        return data

    except sqlite3.Error as e:
        print(f"Database error: {e}") 
        return None # Xəta zamanı None qaytar
    finally:
        if conn:
            conn.close()
