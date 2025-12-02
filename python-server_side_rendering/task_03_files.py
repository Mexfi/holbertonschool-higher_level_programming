from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# Define file paths (assuming files are in the same directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'products.json')
CSV_FILE = os.path.join(BASE_DIR, 'products.csv')

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
            # Use csv.DictReader to read rows as dictionaries
            reader = csv.DictReader(f)
            # Convert the price column to float for consistency
            data = []
            for row in reader:
                # Ensure 'id' is int and 'price' is float for proper comparison/display
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except ValueError:
                    # Skip rows with invalid numeric data
                    continue
            return data
    except FileNotFoundError:
        return None

@app.route('/products')
def products():
    """
    Handles the /products route, reading data based on 'source' and filtering by 'id'.
    """
    # Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    data = None
    error = None
    
    # --- Data Source Selection ---
    if source == 'json':
        data = read_json_data(JSON_FILE)
        if data is None:
            error = "JSON data file not found or invalid."
    elif source == 'csv':
        data = read_csv_data(CSV_FILE)
        if data is None:
            error = "CSV data file not found or invalid."
    else:
        # --- Edge Case: Invalid Source ---
        error = "Wrong source. Must be 'json' or 'csv'."

    if error:
        return render_template('product_display.html', error=error)
    
    # --- Data Filtering by ID ---
    
    # Determine the target data format (list for Jinja rendering)
    products_to_display = []
    
    if product_id_str is not None:
        try:
            target_id = int(product_id_str)
        except ValueError:
            # Handle case where id is provided but is not a valid integer
            error = "Invalid product ID format."
            return render_template('product_display.html', error=error)

        # Filter the list to find the single matching product
        found_product = next((p for p in data if p.get('id') == target_id), None)
        
        if found_product:
            products_to_display.append(found_product)
        else:
            # --- Edge Case: ID Not Found ---
            error = "Product not found."
            return render_template('product_display.html', error=error)
            
    else:
        # If no id is provided, display all products
        products_to_display = data

    # Render template with the results
    return render_template('product_display.html', products=products_to_display, source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
