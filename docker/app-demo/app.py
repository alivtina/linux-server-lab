import os
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_ENV = os.getenv("APP_ENV", "development")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"Hello from Docker! Environment: {APP_ENV}\n"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8000), Handler)

print(f"Server running on port 8000 in {APP_ENV} environment")

server.serve_forever()
