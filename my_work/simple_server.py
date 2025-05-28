from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Save data to file
        with open('data.txt', 'a') as f:
            f.write(post_data + '\n')

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Thanks! Data received.')

if __name__ == "__main__":
    server_address = ('', 5000)  # Listen on all interfaces, port 5000
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running on port 5000...")
    httpd.serve_forever()
