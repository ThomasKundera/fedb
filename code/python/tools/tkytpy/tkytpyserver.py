#!/usr/bin/env python3
import http.server
import socketserver

PORT = 8000
DIRECTORY = "/var/tkweb"





class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory=DIRECTORY, **kwargs)

  def do_GET(self):
    if self.path == "/magic":
      self.simple_magic()
      return
    super().do_GET()

  def simple_magic(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("<html><head><title>Magic!</title></head>", "utf-8"))
    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
    self.wfile.write(bytes("<body>", "utf-8"))
    self.wfile.write(bytes("<p>This is an example.</p>", "utf-8"))
    self.wfile.write(bytes("</body></html>", "utf-8"))


def run():
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# --------------------------------------------------------------------------
def main():
  run()
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
