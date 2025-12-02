from flask import Flask, render_template, request, jsonify
import sqlite3
import csv

app = Flask(__name__)

def fetch_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        conn.close()
        return products
    except sqlite3.Error as e:
        return f"Database error: {e}"

@app.route('/')
def display_products():
    source = request.args.get('source')

    if source == 'json':
        products_data = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
        ]
        return jsonify(products_data)

    elif source == 'csv':
        products_data = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
        ]
        output = "id,name,category,price\n"
        for product in products_data:
            output += f"{product['id']},{product['name']},{product['category']},{product['price']}\n"
        return output, 200, {'Content-Type': 'text/csv'}

    elif source == 'sql':
        products_data = fetch_from_sql()
        if isinstance(products_data, str):
            return f"Error: {products_data}", 500
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in products_data]
        return render_template('product_display.html', products=products)

    else:
        return "Wrong source. Please provide a valid source (json, csv, or sql).", 400

if __name__ == '__main__':
    app.run(debug=True)
