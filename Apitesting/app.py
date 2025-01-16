import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# In-memory data store
users = [
    {"id": 1, "name": "John", "email": "john@example.com"},
    {"id": 2, "name": "Jane", "email": "jane@example.com"}
]

# Custom request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, response_data, status=200):
        """Send JSON response."""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/users":
            self._send_response(users)
        else:
            self._send_response({"error": "Not found"}, status=404)

    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/users":
            # Read and parse the request body
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            new_user = json.loads(body)

            # Add the new user to the data store
            users.append(new_user)
            self._send_response(new_user, status=201)
        else:
            self._send_response({"error": "Not found"}, status=404)

# Start the HTTP server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
