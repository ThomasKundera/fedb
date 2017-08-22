#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os, time
import pickle

#import PyQt5
#from PyQt5.QtCore import QUrl 
#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWebKitWidgets import QWebPage
#from lxml import html
from PyQt4.QtCore import QUrl
from lxml import html

#import render

kDATA_PATH="./tmpdata"

def u2f(u):
  return u.replace('/','_').replace('?','_').replace('=','_').replace(';','_').replace('&','_')


class DomObject:
  def __init__(self,url):
    self.url=url

  def buildRoot(self):
    hfn=self.url.toString()
    hfn=hfn.remove(0,8)
    hfn=u2f(hfn)
    # str() needed for python < 3
    self.hfn=os.path.join(kDATA_PATH,'html',str(hfn))
    self.h2f()
    if (not self.hfnok): return
    tree=html.parse(self.hfn)
    self.root = tree.getroot()
  
  def getViews(self):
    if (not self.hfnok): return 0
    # <span class="load-more-text"> View all 7 replies </span>
    lmtc=self.root.find_class("load-more-text")
    views=0
    try:
      views=int(lmtc[0].text.strip().split(' ')[2])
    except IndexError:
      print ("View invalid (set as zero) "+str(self.url))

    return views

  def h2f(self):
    self.hfnok=True
    #if (os.path.exists(self.hfn)): return
    # dirty
    self.hfnok=False
    from subprocess import call
    call(["timeout","3","./render.py",'--url',self.url.toString(),'--file',self.hfn])
    if (not os.path.exists(self.hfn)):
      print ("Failed to download: "+str(self.url))
      return
    self.hfnok=True


class UrlList:
  def __init__(self):
    f=open('./tmpdata/urlist.txt','rt')
    
    self.urlh={}
    
    for line in f.readlines():
      #print line
      url=QUrl(line.strip())
      ufn=url.toString()
      ufn=ufn.remove(0,8)
      ufn=u2f(ufn)
      if (ufn in self.urlh):
        print ("WARNING: duplicates: "+url)
      else:
        self.urlh[ufn]=url
      

class DbItem:
  def __init__(self,url):
    # No way to pickle Qurl, sad.
    self.url=url.toString()
    self.views=None

  def htmlWrite(self,views):
    if (self.views==None):
      bgcolor='#999999'
    elif (self.views==views):
      bgcolor='#AAFFAA'
    else:
      bgcolor='#FF0000'
    
    return('<li style="background-color:'+bgcolor+';"><a href="'+str(QUrl(self.url).toEncoded())+'"</a> ['+str(views)+' / '+str(self.views)+' ] '+self.url+'</li>\n')
    

class Database:
  def __init__(self):
    self.data={}
    self.dbfn=os.path.join(kDATA_PATH,"database.dat")
    if (os.path.exists(os.path.join(self.dbfn))):      
      self.data=pickle.load(open(self.dbfn,'rb'))
  
  def close(self):
    pickle.dump(self.data,open(self.dbfn,'wb'))
                  
  def loadNew(self):
    urll=UrlList()
    for ufn in urll.urlh.keys():
      if (not (ufn in self.data)):
        print ("New URL to watch: "+str(urll.urlh[ufn]))
        self.data[ufn]=DbItem(urll.urlh[ufn])
      else:
        print ("Known data: "+str(self.data[ufn]))
        
  def refresh(self):
    ofn=os.path.join(kDATA_PATH,"res.html")
    of=open(ofn,"wt")
    # maybe there's better option there
    of.write("<html><head><title>YT comments</title></head><body>\n")
    of.write("<ul>\n")
    
    for item in self.data.values():
      url=QUrl(item.url) # All that because cant pickle Qurl
      print (url)
      mdo=DomObject(url)
      mdo.buildRoot()
      views=mdo.getViews()
      of.write(item.htmlWrite(views))
      of.flush()
      item.views=views
    of.write("</ul>\n")
    of.write("</body><html>\n")
    of.close()
    


def main():
  if (not os.path.exists(os.path.join(kDATA_PATH,'html'  ))):
    os.makedirs(os.path.join(kDATA_PATH,'html'  ))
  
  db=Database()
  db.loadNew()
  try:
    db.refresh()
  except KeyboardInterrupt:
    print ("Saving DB...")
    db.close()
    print ("...Done.")
    raise
  db.close()
  
  

    
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        