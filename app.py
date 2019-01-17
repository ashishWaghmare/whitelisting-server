import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 17995))
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port::",PORT)
httpd.serve_forever()
