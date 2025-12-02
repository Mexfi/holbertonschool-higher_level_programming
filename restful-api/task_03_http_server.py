import http.server
import socketserver
import json

# Define the port the server will run on
PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A custom request handler for the simple API server.
    Handles GET requests for different endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests and route them to the appropriate response.
        """
        if self.path == '/':
            # Handling the root endpoint (/)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode('utf-8'))

        elif self.path == '/data':
            # Handling the /data endpoint to serve JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))

        elif self.path == '/status':
            # Handling the /status endpoint to check API status
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response = "OK"
            self.wfile.write(response.encode('utf-8'))

        elif self.path == '/info':
            # Handling the /info endpoint for general API information
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(info_data)
            self.wfile.write(response.encode('utf-8'))

        else:
            # Handling undefined endpoints (404 Not Found)
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response = "Endpoint not found"
            self.wfile.write(response.encode('utf-8'))

# --- Server Setup ---

def run_server():
    """
    Sets up and starts the HTTP server.
    """
    # Use ThreadingTCPServer for concurrent connections (better than TCPServer)
    # The HandlerClass is SimpleAPIHandler
    with socketserver.ThreadingTCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving on port {PORT}")
        print(f"Access the API at http://localhost:{PORT}")
        try:
            # Keep the server running until interrupted
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.shutdown()

if __name__ == "__main__":
    run_server()
