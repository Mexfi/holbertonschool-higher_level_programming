import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Subclass of BaseHTTPRequestHandler to handle requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Check the path of the request
        if self.path == "/":
            # Handle root ("/") request
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Handle "/data" request
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Data to return
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            # Convert Python dictionary to JSON string and send
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            # Handle "/status" request
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))

        else:
            # Handle undefined endpoints
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# Function to run the server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

# Entry point for running the server
if __name__ == "__main__":
    run()
