import http.server
import socketserver
import os


import http.server
import socketserver
server_base_class = socketserver.TCPServer
class LocalTCPServer(socketserver.TCPServer):
    "Only accepts requests from 14.143.243.78"
    def verify_request(self, request, client_address):
        print(client_address)
        return (client_address[0] == '14.143.243.78')
handler = http.server.SimpleHTTPRequestHandler
PORT = int(os.environ.get("PORT", 17995))
httpd = LocalTCPServer(("",PORT), handler)
print("serving at port::",PORT)
httpd.serve_forever()
