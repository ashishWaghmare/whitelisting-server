import http.server
import socketserver
import os


import http.server
import socketserver
server_base_class = socketserver.TCPServer

class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.headers['X-Forwarded-For'])
        http.server.SimpleHTTPRequestHandler.do_GET(self)

handler = GetHandler
PORT = int(os.environ.get("PORT", 17995))
httpd = socketserver.TCPServer(("",PORT), handler)
print("serving at port::",PORT)
httpd.serve_forever()
