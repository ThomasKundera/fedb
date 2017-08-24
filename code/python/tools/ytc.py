#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os, time
import pickle

try:
    __import__('PyQt5')
    kuse_pyqt5 = True
except ImportError:
    kuse_pyqt5 = False
    
if kuse_pyqt5:
    from PyQt5.QtCore import QUrl, QTimer
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebKitWidgets import QWebPage
else:
    import PyQt4
    from PyQt4.QtCore import QUrl, QTimer
    from PyQt4.QtGui import QApplication


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
    if kuse_pyqt5:
      hfn=hfn[8:-1]
    else:
      hfn=hfn.remove(0,8)
    hfn=u2f(hfn)
    # str() needed for python < 3
    self.hfn=os.path.join(kDATA_PATH,'html',str(hfn))
    self.h2f()
    if (not self.hfnok): return
    tree=html.parse(self.hfn)
    self.root = tree.getroot()
  
  def getViews(self):
    if (not self.hfnok ): return 0
    if (self.root==None): return 0
    #print (title.text)
    #sys.exit(0)
    # <span class="load-more-text"> View all 7 replies </span>
    ctrl=self.root.find_class("comment-thread-renderer")
    #comment-renderer-content
    if (len(ctrl)==0):
      #print ("ctrl invalid (set as zero) "+str(self.url))
      return 0
    lmtc=ctrl[0].find_class("load-more-text")
    crcl=ctrl[0].find_class("comment-renderer-content")
    np=len(crcl)-1
    if (len(lmtc)==0):
      #print ("toto1")
      #print (np)
      return np
    #print (np)
    if (len(lmtc[0].text.strip().split(' '))>3):
      #print("toto3")
      #print (int(lmtc[0].text.strip().split(' ')[2]))
      return int(lmtc[0].text.strip().split(' ')[2])
      #+np
    #print (lmtc[0].text.strip().split(' '))
    if (len(lmtc[0].text.strip().split(' '))==2):
      #print ("toto2")
      #print (np+1)
      return (np+1)
    return 0
  
  def getTitle(self):
    if (not self.hfnok ): return "None1"
    if (self.root==None): return "None2"
    head=self.root.find("head")
    title=head.find("title")
    if (title ==None): return "None3"
    return title.text.encode('utf-8').strip()
  
  def h2f(self):
    self.hfnok=True
    #if (os.path.exists(self.hfn)): return
    # dirty
    self.hfnok=False
    from subprocess import call
    call(["timeout","4","./render.py",'--url',self.url.toString(),'--file',self.hfn])
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
      if kuse_pyqt5:
        ufn=ufn[8:-1]
      else:
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

  def htmlWrite(self,views,title):
    if (self.views==None):
      bgcolor='#999999'
    elif (self.views==views):
      bgcolor='#AAFFAA'
    else:
      bgcolor='#FF0000'
    if kuse_pyqt5:
      return('<li style="background-color:'+bgcolor+';"><a href="'+self.url+'"/a> ['+str(views)+' / '+str(self.views)+' ] '+str(title)+'</li>\n')
    else:
      return('<li style="background-color:'+bgcolor+';"><a href="'+str(QUrl(self.url).toEncoded())+'"/a> ['+str(views)+' / '+str(self.views)+' ] '+title+'</li>\n')
    

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
        pass
        #print ("Known data: "+str(self.data[ufn]))
        
  def refresh(self):
    ofn=os.path.join(kDATA_PATH,"res.html")
    of=open(ofn,"wt")
    # maybe there's better option there
    of.write('<html><head><title>YT comments</title><meta charset="UTF-8"></head><body>\n')
    of.write("<ol>\n")
    nb=0
    for item in self.data.values():
      if (False): #("z12bjzxh3z35t3bod04cjt0j3vf3x1srwkk0k" not in item.url) and ("z235j1f54qyzgvqqt04t1aokgvzcwaai1mhnoxqv1axsbk0h00410" not in item.url)):
        pass
      else:
        url=QUrl(item.url) # All that because cant pickle Qurl
        print (url)
        mdo=DomObject(url)
        mdo.buildRoot()
        views=mdo.getViews()
        title=mdo.getTitle()
        of.write(item.htmlWrite(views,title))
        of.flush()
        item.views=views
    of.write("</ol>\n")
    of.write("<p>END of DATA\n")
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
        
        
