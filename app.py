import http.server
import SocketServer

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print("serving at port::",PORT)
httpd.serve_forever()
