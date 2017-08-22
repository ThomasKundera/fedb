#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtCore import QUrl 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebPage
from lxml import html



# From: https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)
    
    #url = QUrl(url)
    #username = input('username')
    #password = input('password')

    #base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    #authheader = "Basic %s" % base64string
    
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

class UrlList:
  def __init__(self):
    f=open('./tmpdata/urlist.txt')
    
    self.urlh={}
    
    for url in f.readline():
      if (url in self.urlh):
        print ("WARNING: duplicates: "+url)
      else:
        self.urlh[url]=url
    
  def process(self):
    for url in self.urlh.values():
      r = Render(url)  
      result = r.frame.toHtml()
      
      


def main():
  urll=UrlList()
  
  urll.process()

  url = './tmpdata/'  
  r = Render(url)  
  result = r.frame.toHtml()
  #This step is important.Converting QString to Ascii for lxml to process
  archive_links = html.fromstring(str(result))
  print (archive_links)
    
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        