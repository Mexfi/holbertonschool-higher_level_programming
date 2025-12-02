from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity, get_jwt

# Instantiate the Flask application
app = Flask(__name__)

# --- 1. Security Configuration ---

# Configuration for JWT
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in production!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False  # Tokens won't expire for simplicity

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# --- 2. User Data Store ---

# Store users with hashed passwords and roles
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- 3. Flask-HTTPAuth (Basic Authentication) ---

@auth.verify_password
def verify_password(username, password):
    """Callback for verifying username and password for Basic Auth."""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    # auth.current_user() holds the username of the successfully authenticated user
    return "Basic Auth: Access Granted"

# Override Basic Auth error handler to return 401 and JSON (if needed for consistency)
@auth.error_handler
def auth_error(status):
    """Custom error handler for Basic Auth failures."""
    return jsonify({"error": "Unauthorized"}), 401

# --- 4. Flask-JWT-Extended (Token-Based Authentication) ---

@app.route("/login", methods=["POST"])
def login():
    """Route to authenticate user and issue a JWT token."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')

    user_info = users.get(username)

    if user_info and check_password_hash(user_info['password'], password):
        # Create a token with the username as identity and role as extra claim
        # Role is embedded in the token for RBAC checks
        additional_claims = {"role": user_info['role']}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify(access_token=access_token)
    
    # Credentials invalid for login
    return jsonify({"error": "Invalid username or password"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    # get_jwt_identity() retrieves the identity (username) set during token creation
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"

# --- 5. Role-Based Access Control (RBAC) ---

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route accessible only by users with the 'admin' role."""
    # get_jwt() retrieves the full token payload (including custom claims like 'role')
    claims = get_jwt()
    
    if claims.get("role") == "admin":
        return "Admin Access: Granted"
    else:
        # Access denied because user does not have the 'admin' role
        return jsonify({"error": "Admin access required"}), 403

# --- 6. Custom JWT Error Handlers (Ensuring 401 for Auth Failures) ---
# These handlers ensure that all JWT-related authentication failures return 401.

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
