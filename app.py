import http.server
import socketserver

PORT = 8080
MESSAGE = "Hello from Github version V1"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(MESSAGE.encode())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server listening on port {PORT}")
    httpd.serve_forever()
