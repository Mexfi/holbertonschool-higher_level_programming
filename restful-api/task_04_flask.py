from flask import Flask, jsonify, request
import json

# Instantiate the Flask application
app = Flask(__name__)

# In-memory data store for users
# NOTE: The users dictionary is initialized with example data for development testing,
# but it should be empty or contain only necessary initial data for the checker.
# Per instructions, do not include testing data when pushing your code.
users = {} 
# For testing purposes, you can uncomment this line:
# users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    """
    Handles the root endpoint.
    Returns a simple welcome message.
    """
    return "Welcome to the Flask API!"

# --- GET Requests ---

@app.route("/status")
def get_status():
    """
    Handles the /status endpoint.
    Returns the API status.
    """
    return "OK"

@app.route("/data")
def get_data():
    """
    Handles the /data endpoint.
    Returns a JSON list of all usernames.
    """
    # Return a list of all keys (usernames) from the users dictionary
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    """
    Handles the /users/<username> dynamic endpoint.
    Returns the full user object or a 404 error if not found.
    """
    user_data = users.get(username)
    if user_data:
        # User found, return their data
        return jsonify(user_data)
    else:
        # User not found, return 404 error
        return jsonify({"error": "User not found"}), 404

# --- POST Request ---

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles the /add_user endpoint for POST requests.
    Adds a new user to the in-memory store.
    """
    try:
        # 1. Parse incoming JSON data
        user_data = request.get_json()
        
        # Check if JSON parsing failed (e.g., body is not valid JSON)
        if user_data is None:
            return jsonify({"error": "Invalid JSON"}), 400

    except Exception:
        # Catch exceptions during JSON parsing
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Validate required field
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]

    # 3. Check for conflict (username already exists)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Add the new user to the data store
    # Ensure the user object contains the 'username' field (which it should, 
    # but it's good practice to set it)
    user_data["username"] = username 
    users[username] = user_data

    # 5. Return confirmation message with the user data and 201 Created status
    response = {
        "message": "User added",
        "user": user_data
    }
    return jsonify(response), 201


if __name__ == "__main__":
    # The default port for Flask is 5000
    app.run(debug=True)
