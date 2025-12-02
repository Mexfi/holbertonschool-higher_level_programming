from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Fayl yollarını təyin edirik
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'products.json')
CSV_FILE = os.path.join(BASE_DIR, 'products.csv')
DB_FILE = os.path.join(BASE_DIR, 'products.db')

# --- 1. Məlumat Oxuma Köməkçi Funksiyaları ---

def read_json_data(file_path):
    """JSON faylından məlumat oxuyur."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv_data(file_path):
    """CSV faylından məlumat oxuyur."""
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                try:
                    # Tipləri uyğunlaşdırırıq
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except (ValueError, KeyError):
                    continue
            return data
    except FileNotFoundError:
        return None

def read_sql_data(product_id=None):
    """SQLite-dan məhsul məlumatlarını gətirir."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        # Sətirlərə sütun adı ilə müraciət etmək üçün
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        
        if product_id is None:
            # Bütün məhsulları gətir
            cursor.execute("SELECT id, name, category, price FROM Products")
        else:
            # ID-yə görə məhsulu gətir (təhlükəsiz binding)
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        
        # sqlite3.Row obyektlərini adi sözlüklərə çevir
        data = [dict(row) for row in cursor.fetchall()]
        return data
        
    except sqlite3.Error as e:
        print(f"Database error: {e}") 
        return None
    finally:
        if conn:
            conn.close()

# --- 2. Flask Marşrutu ---

@app.route('/products')
def products():
    """
    /products marşrutunu idarə edir.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    data = None
    error = None
    target_id = None
    
    # 2.1. ID parametini yoxla və çevir
    if product_id_str is not None:
        try:
            target_id = int(product_id_str)
        except ValueError:
            error = "Invalid product ID format."
            return render_template('product_display.html', error=error)

    # 2.2. Mənbədən məlumatı gətir
    if source == 'json':
        data = read_json_data(JSON_FILE)
    elif source == 'csv':
        data = read_csv_data(CSV_FILE)
    elif source == 'sql':
        # SQL funksiyası target_id-ni qəbul edir və özü filtrləyir
        data = read_sql_data(target_id) 
    else:
        # Yanlış Mənbə Xətası
        error = "Wrong source. Must be 'json', 'csv', or 'sql'."
        return render_template('product_display.html', error=error)
    
    # 2.3. Məlumatın Gətirilməsi Xətası
    if data is None:
        error = f"Error reading data from {source} source."
        return render_template('product_display.html', error=error)

    # 2.4. Filtrasiya və Tapılmaması Yoxlanışı
    products_to_display = []
    
    if target_id is not None:
        if source == 'sql':
            # SQL məlumatı artıq filtirlənib. Əgər boşdursa, tapılmadı xətası verilir.
            if not data:
                error = "Product not found."
                return render_template('product_display.html', error=error)
            products_to_display = data
        else: 
            # JSON/CSV: məlumatı əl ilə filtrlə
            found_product = next((p for p in data if p.get('id') == target_id), None)
            
            if found_product:
                products_to_display.append(found_product)
            else:
                error = "Product not found."
                return render_template('product_display.html', error=error)
    else:
        # ID yoxdursa, hamısını göstər
        products_to_display = data


    # 2.5. Şablonu göstər
    return render_template('product_display.html', products=products_to_display, source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
