#!/usr/bin/env python3
import http.server
import socketserver
import yattag
import urllib
import json
import requests
import asyncio
import time

import tkqueue

from tksecrets import google_api_key
from googleapiclient.discovery import build

PORT = 8000
DIRECTORY = "/var/tkweb"


def valid_url(url):
  r = requests.head(url)
  print(r)
  return(r.status_code == 200)

class YTVideo:
  def __init__(self,yid):
    self.valid=False
    self.yid=yid.strip()
    self.url='https://www.youtube.com/watch?v='+self.yid
    if not self.is_valid_id():
      print("Not valid yid:"+self.yid)
      return
    self.valid=True
    # Filling with temporary data
    self.populate_variables_dummy()
    # Queue filling with real data asynchronously
    task=tkqueue.TkTask('populate:'+self.yid,self.populate_variables_from_youtube)
    tkqueue.QueuWork().add(task)
    #asyncio.run(self.populate_variables_from_youtube())

  def is_valid_id(self):
    if (len(self.yid) != 11): return False
    return valid_url(self.url)

  def get_data(self):
    request = gtkyp.youtube.videos().list(part='snippet,statistics', id=self.yid)
    self.rawytdata = request.execute()
    if len(self.rawytdata['items']) != 1:
      self.valid=False


  def populate_variables_dummy(self):
    self.populated=False
    self.title=self.url
    return

  def populate_variables_from_youtube(self):
    self.get_data()
    if not self.valid:
      return
    self.title=self.rawytdata['items'][0]['snippet']['title']
    self.populated=True


  def get_dict(self):
    return {
      'yid'  : self.yid,
      'url'  : self.url,
      'title': self.title
      }

  def __str__(self):
    return self.yid


class YTVideoList:
  def __init__(self):
    self.videos={}

  def add(self,v):
    if (v.valid):
      self.videos[v.yid]=v
    else:
      print("Not adding invalid video: "+str(v))

  def to_html(self,doc,tag,text,line):
    for v in  self.videos:
      with tag('p'):
        text(v.yid)

  def to_dict(self):
    l=[]
    for v in self.videos.values():
      if v.valid:
        l.append(v.get_dict())
    return  {'ytvlist': l}

class TKYTGlobal:
  def __init__(self):
    self.videos=YTVideoList()
    self.youtube = build('youtube','v3',developerKey=google_api_key)
    return

  def return_page(self,path):
    self.doc, self.tag, self.text, self.line = yattag.Doc().ttl()
    self.doc.asis('<!DOCTYPE html>')
    with self.tag('html'):
      with self.tag('head'):
        self.doc.stag('link',href='style.css',rel="stylesheet", type="text/css")
        with self.tag('title'):
          self.text("YT comment manager - Main page")

      with self.tag('body'):
        with self.tag('h1'):
          self.text("YT comment manager - Main page")

      self.videos.to_html(self.doc, self.tag, self.text, self.line)
      with self.tag('form', action = ""):
        self.doc.input(name = 'title', type = 'text')

      with self.tag('script', src='script.js'):
        self.text()

    return (yattag.indent(self.doc.getvalue(), indent_text = True))

  def get_video_dict(self):
    return self.videos.to_dict()

  def add_video(self,v):
    self.videos.add(v)

class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory=DIRECTORY, **kwargs)

  def do_GET(self):
    super().do_GET()
    return
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    self.wfile.write(bytes(gtkyp.return_page(self.path), "utf-8"))
    self._set_response()
    self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


  def do_POST(self):
    print ("POST request: "+self.path)
    content_length = int(self.headers['Content-Length'])
    post_data_bytes = self.rfile.read(content_length)
    print ("Received data:\n", post_data_bytes)

    post_data_str = post_data_bytes.decode("UTF-8")
    js=json.loads(post_data_str)

    gtkyp.add_video(YTVideo(js['ytid']))

    jsr=json.dumps(gtkyp.get_video_dict())
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(jsr.encode(encoding='utf_8'))


def runserver():
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# --------------------------------------------------------------------------
def main():
  global gtkyp
  gtkyp=TKYTGlobal()
  #YTVideo('BHa4AJwZDZg')
  runserver()
  tkqueue.QueuWork().join()

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
        
