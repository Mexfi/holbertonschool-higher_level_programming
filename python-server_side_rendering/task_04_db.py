from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Define file paths (assuming files and db are in the same directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'products.json')
CSV_FILE = os.path.join(BASE_DIR, 'products.csv')
DB_FILE = os.path.join(BASE_DIR, 'products.db')

# --- Data Reading Helper Functions ---

def read_json_data(file_path):
    """Reads and parses data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv_data(file_path):
    """Reads and parses data from a CSV file."""
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except (ValueError, KeyError):
                    continue
            return data
    except FileNotFoundError:
        return None

def read_sql_data(product_id=None):
    """Fetches product data from the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        # Allows accessing columns by name, which is crucial for dictionary conversion
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        
        if product_id is None:
            # Fetch all products
            cursor.execute("SELECT id, name, category, price FROM Products")
        else:
            # Fetch specific product by id (using ? for safe parameter binding)
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        
        # Convert list of sqlite3.Row objects into a list of regular dictionaries
        data = [dict(row) for row in cursor.fetchall()]
        return data
        
    except sqlite3.Error as e:
        # Log database error for debugging
        print(f"Database error: {e}") 
        return None
    finally:
        if conn:
            conn.close()

# --- Flask Routes ---

@app.route('/products')
def products():
    """
    Handles the /products route, supporting json, csv, and sql data sources.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    data = None
    error = None
    target_id = None
    
    # 1. Validate and convert product_id
    if product_id_str is not None:
        try:
            target_id = int(product_id_str)
        except ValueError:
            error = "Invalid product ID format."
            return render_template('product_display.html', error=error)

    # 2. Data Source Selection and Retrieval
    if source == 'json':
        data = read_json_data(JSON_FILE)
    elif source == 'csv':
        data = read_csv_data(CSV_FILE)
    elif source == 'sql':
        # SQL logic handles filtering internally
        data = read_sql_data(target_id) 
    else:
        # Invalid Source
        error = "Wrong source. Must be 'json', 'csv', or 'sql'."
        return render_template('product_display.html', error=error)
    
    # 3. Data Retrieval Error Check (e.g., file not found, db connection error)
    if data is None:
        error = f"Error reading data from {source} source."
        return render_template('product_display.html', error=error)

    # 4. Data Filtering and Not Found Check
    products_to_display = []
    
    if target_id is not None:
        if source == 'sql':
            # SQL data is already filtered. Check if the result is empty.
            if not data:
                error = "Product not found."
                return render_template('product_display.html', error=error)
            products_to_display = data
        else: 
            # JSON/CSV: manually filter the data list
            found_product = next((p for p in data if p.get('id') == target_id), None)
            
            if found_product:
                products_to_display.append(found_product)
            else:
                error = "Product not found."
                return render_template('product_display.html', error=error)
    else:
        # No ID provided, display all data
        products_to_display = data


    # 5. Render template
    return render_template('product_display.html', products=products_to_display, source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
