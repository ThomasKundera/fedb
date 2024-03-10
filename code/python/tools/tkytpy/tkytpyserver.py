#!/usr/bin/env python3
import http.server
import socketserver
import yattag

PORT = 8000
DIRECTORY = "/var/tkweb"



class YTVideo:
  def __init__(self,yid):
    self.yid=yid


class YTVideoList:
  def __init__(self):
    self.videos={}

  def add(self,v):
    self.videos[v.yid]=yid

  def to_html(self,doc,tag,text,line):
    for v in  self.videos:
      with tag('p'):
        text(v.yid)

class TKYTGlobal:
  def __init__(self):
    self.videos=YTVideoList()
    return

  def return_page(self,path):
    self.doc, self.tag, self.text, self.line = yattag.Doc().ttl()
    self.doc.asis('<!DOCTYPE html>')
    with self.tag('html'):
      with self.tag('head'):
        self.doc.stag('link',href='style.css',rel="stylesheet", type="text/css")
        with self.tag('script', src='script.js'):
          self.text()
        with self.tag('title'):
          self.text("YT comment manager - Main page")

      with self.tag('body'):
        with self.tag('h1'):
          self.text("YT comment manager - Main page")

      self.videos.to_html(self.doc, self.tag, self.text, self.line)

    return (yattag.indent(self.doc.getvalue(), indent_text = True))

class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory=DIRECTORY, **kwargs)

  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    self.wfile.write(bytes(gtkyp.return_page(self.path), "utf-8"))



def runserver():
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# --------------------------------------------------------------------------
def main():
  global gtkyp
  gtkyp=TKYTGlobal()
  runserver()
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
