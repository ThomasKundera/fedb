#!/usr/bin/env python3
import http.server
import socketserver
import json

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

import tksingleton

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
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
    logging.debug("HttpHandle:do_POST: Received data:\n"+str(post_data_bytes))
    post_data_str = post_data_bytes.decode("UTF-8")
    js=json.loads(post_data_str)
    print(js)

    EventHandler().add_video(js)

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    response=EventHandler().get_video_list()

    self.wfile.write(response.encode(encoding='utf_8'))
    logging.debug("HttpHandle:do_POST: END")



class EventHandler(metaclass=tksingleton.SingletonMeta):
  def __init__(self,tkyt=None):
    self.tkyt=tkyt
    return

  def add_video(self,js):
    yid=js['ytid']
    self.tkyt.add_video(yid)
    return

  def get_video_list(self):
    return json.dumps(self.tkyt.get_video_list())


class HttpServer:
  def __init__(self,tkyt):
    EventHandler(tkyt)

  def run(self):
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
  return

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
        
