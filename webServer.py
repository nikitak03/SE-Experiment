from http.server import BaseHTTPRequestHandler, HTTpServer
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BestHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_header()
        self.wfile.write(bytes("<html><head><title>http://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>Task 2</h1>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%:%s" % (hostName, serverPort))
    try:
        webserver.server_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stooped.")
