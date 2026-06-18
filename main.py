from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import mimetypes

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            filename = "index.html"
        else:
            filename = self.path.lstrip("/")



        if os.path.exists(filename):
            self.send_response(200)


            mime_type, _ = mimetypes.guess_type(filename)

            if mime_type:
                self.send_header("Content-type", mime_type)
            else:
                self.send_header("Content-type", "application/octet-stream")

            self.end_headers()


            with open(filename, "rb") as file:
                self.wfile.write(file.read())

        else:
            self.send_error(404, "File Not Found")


hostName = "localhost"
serverPort = 80


webServer = HTTPServer((hostName, serverPort), MyHandler)
print(f"Сервер запущен: http://{hostName}:{serverPort}")
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Сервер остановлен...")
