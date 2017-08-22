#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import pickle

#import PyQt5
#from PyQt5.QtCore import QUrl 
#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWebKitWidgets import QWebPage
#from lxml import html
import PyQt4
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication
#from PyQt4.QtWidgets import QApplication
from PyQt4.QtWebKit import QWebPage
from lxml import html

kDATA_PATH="./tmpdata"

def u2f(u):
  return u.replace('/','_').replace('?','_').replace('=','_').replace(';','_').replace('&','_')


# From: https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/
class Render(QWebPage):  
  def __init__(self, url,fn):  
    self.app = QApplication(sys.argv)
    self.fname=fn
    self.url=url
    #url = QUrl(url)
    #username = input('username')
    #password = input('password')

    #base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    #authheader = "Basic %s" % base64string
    
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(self.url)  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    f = open( self.fname, 'wt' )
    f.write( self.mainFrame().toHtml() )
    f.close()
    self.app.quit()  


class DomObject:
  def __init__(self,url):
    self.url=url

  def process(self):
    print (self.url)
    ufn=self.url.toString()
    ufn=ufn.remove(0,8)
    ufn=u2f(ufn)
    # str() needed for python < 3
    self.hfn=os.path.join(kDATA_PATH,'html',str(ufn))
    self.h2f()
    tree=html.parse(self.hfn)
    root = tree.getroot()
    # <span class="load-more-text"> View all 7 replies </span>
    lmtc=root.find_class("load-more-text")
    for l in lmtc:
      print l.text
    sys.exit(0)

  def h2f(self):
    if (os.path.exists(self.hfn)): return
    r = Render(self.url,self.hfn)
    


class UrlList:
  def __init__(self):
    f=open('./tmpdata/urlist.txt','rt')
    
    self.urlh={}
    
    for line in f.readlines():
      #print line
      url=QUrl(line.strip())
      if (url in self.urlh):
        print ("WARNING: duplicates: "+url)
      else:
        self.urlh[url]=url
    
  def process(self):
    for url in self.urlh.values():
      mdo=DomObject(url)
      mdo.process()
      

class DbItem:
  def __init__(self):
    pass


class Database:
  def __init__(self):
    self.dbfn=op.path.join(kDATA_PATH,"database.dat")
    if (os.path.exists(os.path.join(self.dbfn))):
      pickle.load(self.data,open(self.dbfn,'rb'))
  
  def close(self):
    pickle.dump(self.data,open(self.dbfn,'wb'))
                  
               


def main():
  if (not os.path.exists(os.path.join(kDATA_PATH,'html'  ))):
    os.makedirs(os.path.join(kDATA_PATH,'html'  ))
  
  urll=UrlList()
  urll.process()

    
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        