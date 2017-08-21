#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtCore import QUrl 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebPage
from lxml import html

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  



def main():
    url = 'http://pycoders.com/archive/'  
    r = Render(url)  
    result = r.frame.toHtml()
    #This step is important.Converting QString to Ascii for lxml to process
    archive_links = html.fromstring(str(result))
    print (archive_links)
    
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        