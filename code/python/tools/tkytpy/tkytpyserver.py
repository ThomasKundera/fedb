#!/usr/bin/env python3
import http.server
import socketserver
import json

import sqlqueue
import ytvideolist

import tkyt

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

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
    tkyt.TkYt().videos.add_from_yid(js['ytid'])

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    jsr=json.dumps(tkyt.TkYt().videos.to_dict())

    self.wfile.write(jsr.encode(encoding='utf_8'))
    logging.debug("HttpHandle:do_POST: END")


# --------------------------------------------------------------------------
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
def init_db():
  ytvideolist.Base.metadata.create_all()
  print("Initialized the db")


# --------------------------------------------------------------------------
def main():
  logging.debug("main: START")
  init_db()
  logging.debug("main: 1")
  dbsession=sqlqueue.SqlQueue().mksession()
  logging.debug("main: 2")
  tkyt.TkYt().setup()
  logging.debug("main: 3")
  runserver()
  logging.debug("main: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
        
