import os
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the handler to serve the HTML file
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

# Function to start the server and open the browser
def start_server():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Serving on port {port}")
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()
