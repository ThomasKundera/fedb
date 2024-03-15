#!/usr/bin/env python3
import http.server
import socketserver

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class HttpHandler(http.server.SimpleHTTPRequestHandler):
  DIRECTORY = "/var/tkweb"
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory=HttpHandler.DIRECTORY, **kwargs)

  def do_GET(self):
    super().do_GET()

  def do_POST(self):
    logging.debug("HttpHandle:do_POST: START: "+self.path)
    content_length = int(self.headers['Content-Length'])
    post_data_bytes = self.rfile.read(content_length)
    logging.debug("HttpHandle:do_POST: Received data:\n", post_data_bytes)

    post_data_str = post_data_bytes.decode("UTF-8")
    js=json.loads(post_data_str)

    gtkyp.add_video(YTVideo(js['ytid'],gtkyp))

    jsr=json.dumps(gtkyp.get_video_dict())
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(jsr.encode(encoding='utf_8'))
    logging.debug("HttpHandle:do_POST: END")

def runserver():
  PORT = 8000
  with socketserver.TCPServer(("", PORT), HttpHandler) as httpd:
    logging.debug("serving at port: "+str(PORT))
    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      logging.debug("Stopping server...")
      httpd.shutdown()

# --------------------------------------------------------------------------
def main():
  logging.debug("main: START")
  runserver()
  logging.debug("main: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
        
