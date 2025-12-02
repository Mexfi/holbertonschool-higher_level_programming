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

# --- Data Reading Helper Functions (From previous task, modified for consistency) ---

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
                    # Convert to appropriate types for consistency
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except (ValueError, KeyError):
                    continue
            return data
    except FileNotFoundError:
        return None

# --- New SQLite Data Reading Function ---

def read_sql_data(product_id=None):
    """Fetches product data from the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        if product_id is None:
            # Fetch all products
            cursor.execute("SELECT id, name, category, price FROM Products")
        else:
            # Fetch specific product by id
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        
        # Get column names to build dictionary keys
        columns = [col[0] for col in cursor.description]
        
        # Convert list of tuples into a list of dictionaries
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data
        
    except sqlite3.Error as e:
        # --- Edge Case: Database Error ---
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
    # Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    data = None
    error = None
    target_id = None
    
    # Attempt to convert product_id
    if product_id_str is not None:
        try:
            target_id = int(product_id_str)
        except ValueError:
            error = "Invalid product ID format."
            return render_template('product_display.html', error=error)

    # --- Data Source Selection ---
    if source == 'json':
        data = read_json_data(JSON_FILE)
    elif source == 'csv':
        data = read_csv_data(CSV_FILE)
    elif source == 'sql':
        data = read_sql_data(target_id) # SQL logic handles filtering internally
    else:
        # --- Edge Case: Invalid Source ---
        error = "Wrong source. Must be 'json', 'csv', or 'sql'."
        return render_template('product_display.html', error=error)
    
    # --- Data Error Check ---
    if data is None:
        error = f"Error reading data from {source} source."
        return render_template('product_display.html', error=error)

    # --- Data Filtering (for JSON/CSV sources) ---
    products_to_display = []
    
    if source in ('json', 'csv') and target_id is not None:
        # Filter the list to find the single matching product
        found_product = next((p for p in data if p.get('id') == target_id), None)
        
        if found_product:
            products_to_display.append(found_product)
        else:
            # --- Edge Case: ID Not Found ---
            error = "Product not found."
            return render_template('product_display.html', error=error)
            
    elif source == 'sql':
        # SQL logic returns either a list of one product (if ID was specified) or all products
        products_to_display = data
        
        # Check if ID was requested but no product was returned
        if target_id is not None and not products_to_display:
             error = "Product not found."
             return render_template('product_display.html', error=error)

    else:
        # If no id is provided (or source is SQL with no id), display all products
        products_to_display = data


    # Render template with the results
    return render_template('product_display.html', products=products_to_display, source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
