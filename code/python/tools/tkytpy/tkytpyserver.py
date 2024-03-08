#!/usr/bin/env python3
import http.server
import socketserver

PORT = 8000
DIRECTORY = "/var/tkweb"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


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
        
