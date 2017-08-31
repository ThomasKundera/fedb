#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os, datetime
import pickle
import argparse

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

def debug_print(l,t,s):
  if(l>=t):
    print (s)


def u2f(u):
  return u.replace('/','_').replace('?','_').replace('=','_').replace(';','_').replace('&','_')


class DomObject:
  def __init__(self,args,url):
    self.args=args # FIXME: shoud be some global singleton or something
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
      debug_print(self.args.debug_level,100,"ctrl invalid (set as zero) "+str(self.url))
      return 0
    lmtc=ctrl[0].find_class("load-more-text")
    crcl=ctrl[0].find_class("comment-renderer-content")
    np=len(crcl)-1
    debug_print(self.args.debug_level,100,"np = "+str(np))
    if (len(lmtc)==0):
      debug_print(self.args.debug_level,100,"lmtc len() is zero. Assuming failed download. Returning -1"+str(np))
      return (-1)
    if (len(lmtc[0].text.strip().split(' '))>3):
      debug_print(self.args.debug_level,100,"lmtc len() > 3 . Returning "+str(int(lmtc[0].text.strip().split(' ')[2])))
      return int(lmtc[0].text.strip().split(' ')[2])
    if (len(lmtc[0].text.strip().split(' '))==2):
      debug_print(self.args.debug_level,100,"lmtc len() == 2 . Returning "+str(np+1))
      return (np+1)
    return 0
  
  def getTitle(self):
    if (not self.hfnok ): return "None1"
    if (self.root==None): return "None2"
    head=self.root.find("head")
    title=head.find("title")
    if (title ==None): return "None3"
    return title.text.encode('utf-8').strip()
  
  def h2f(self,retry=0):
    if (retry>3):
      print ("Wont retry again: download failed")
      return
    self.hfnok=True
    if ((not self.args.dont_be_lazy) and (os.path.exists(self.hfn))): return
    # dirty
    self.hfnok=False
    from subprocess import call
    call(["timeout","4","./render.py",'--url',self.url.toString(),'--file',self.hfn])
    if (not os.path.exists(self.hfn)):
      print ("Failed to download: "+str(self.url))
      return self.h2f(retry+1)
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
      


class View:
  def __init__(self,n):
    self.n=n
    self.date=datetime.datetime.now()

  def __str__(self):
    return ('[ '+str(self.n)+' - '+str(self.date)+' ]')

  def __lt__(self, other):
      return (self.date < other.date)
    
  def __gt__(self, other):
      return (self.date > other.date)

  def __eq__(self, other):
      return (self.date == other.date)

  def __le__(self, other):
      return (self.date <= other.date)

  def __ge__(self, other):
      return (self.date >= other.date)

  def __ne__(self, other):
      return (self.date != other.date)
     

class DbItem:
  def __init__(self,url):
    # No way to pickle Qurl, sad.
    self.url=url.toString()
    self.views=None

  def htmlWrite(self,views,title):
    if (self.views==None and views==None):
      bgcolor='#999999'
    elif (self.views==views):
      bgcolor='#AAFFAA'
    else:
      bgcolor='#FF0000'
    s ='<li style="background-color:'+bgcolor+';">'
    s+='<input type="checkbox">'
    s+='<a href="'
    if kuse_pyqt5:
      s+=self.url
    else:
      s+=str(QUrl(self.url).toEncoded())
    s+='"/a> ['+str(views)+' / '+str(self.views)+' ] '
    s+=str(title)+'</li>\n'
    
    return s


class DbItem2:
  def __init__(self,dbi):
    self.url=dbi.url
    self.views=[View(dbi.views)]


class DbItem3:
  def __init__(self,url):
    # Normal behavior
    if (isinstance(url,QUrl)):
      # No way to pickle Qurl, sad.
      self.url=url.toString()
      self.views=[]
      return
    # Database upgrade
    #if (isinstance(url,DbItem)):
    self.url=url.url
    self.views=[View(url.views)]
    #  return
    #print ("Error: DbItem3: Unknown type: "+str(type(url)))
    
  def addview(self,n):
    v=View(n)
    self.views.append(v)

  def isviewinview(self,v):
    self.views[-1].n

  def views2color(self):
    vl=[] # dirty
    for v in self.views:
      vl.append(v.n)
    
    if (len(vl)<=1):
      return '#999999'
    if (not (vl[-1] in vl[:-1])):
      return '#FF0000'
    if (vl[-1] > vl[-2]):
      return '#BBFFAA'
    return '#AAFFAA'

  def htmlWrite(self,title):
    bgcolor=self.views2color()
    #print (bgcolor)
    if (len(self.views)>1):
      previous=str(self.views[-2].n)
    else:
      previous=str(self.views[-1].n)
    s ='<li style="background-color:'+bgcolor+';">'
    s+='<input type="checkbox">'
    s+='<a href="'
    if kuse_pyqt5:
      s+=self.url
    else:
      s+=str(QUrl(self.url).toEncoded())
    s+='"> ['+str(self.views[-1].n)+' / '+previous+' ] '
    s+=str(title)+' </a></li>\n'
    
    return s
  
  def __str__(self):
    s=str(self.url)+" "
    for v in self.views:
      s+=str(v)+" "
    return s
  
  
  def cmpempty(self,other):
    if ((not len(self.views)) and  (not len(self.views))):
      return (True,False)
    if ((not len(self.views))):
      return (True,True)
    
        
  
  def __lt__(self, other):
    if ((not len(self.views)) and (not len(self.views))):
      return False
    if ((not len(self.views))):
      return True
    if ((not len(other.views))):
      return False
    return (self.views[0] <  other.views[0])
    
  def __gt__(self, other):
    if ((not len(self.views)) and (not len(self.views))):
      return False
    if ((not len(self.views))):
      return False
    if ((not len(other.views))):
      return True
    return (self.views[0] >  other.views[0])

  def __eq__(self, other):
    if ((not len(self.views)) and (not len(self.views))):
      return True
    if ((not len(self.views))):
      return False
    if ((not len(other.views))):
      return False
    return (self.views[0] == other.views[0])

  def __le__(self, other):
    if ((not len(self.views)) and (not len(self.views))):
      return True
    if ((not len(self.views))):
      return True
    if ((not len(other.views))):
      return False
    return (self.views[0] <= other.views[0])

  def __ge__(self, other):
    if ((not len(self.views)) and (not len(self.views))):
      return True
    if ((not len(self.views))):
      return False
    if ((not len(other.views))):
      return True
    return (self.views[0] >= other.views[0])

  def __ne__(self, other):
    if ((not len(self.views)) and (not len(self.views))):
      return False
    if ((not len(self.views))):
      return True
    if ((not len(other.views))):
      return True
    return (self.views[0] != other.views[0])

    
 

class Database:
  def __init__(self,args):
    self.args=args
    self.data={}
    dbi="database.dat"
    self.dbfn=os.path.join(kDATA_PATH,dbi)
    if (os.path.exists(os.path.join(self.dbfn))):      
      self.data=pickle.load(open(self.dbfn,'rb'))
    
  
  def close(self):
    # Version update
    if (self.args.upgrade_database):
      datanew={}
      dbo=os.path.join(kDATA_PATH,"database-new.dat")
      for (k,v) in self.data.items():
        datanew[k]=DbItem3(v)
      pickle.dump(datanew,open(dbo,'wb'))
    
    if (self.args.update_database):
      pickle.dump(self.data,open(self.dbfn,'wb'))
    else:
      print("Skipping database update")
                  
  def loadNew(self):
    urll=UrlList()
    nb=0
    nbn=0
    for ufn in urll.urlh.keys():
      nb+=1
      if (not (ufn in self.data)):
        nbn+=1
        print ("New URL to watch: "+str(urll.urlh[ufn]))
        self.data[ufn]=DbItem3(urll.urlh[ufn])
      else:
        pass
        #print ("Known data: "+str(self.data[ufn]))
    print (str(nb)+" entries read, "+str(nbn)+" new.")
        
  def refresh(self):
    ofn=os.path.join(kDATA_PATH,"res.html")
    of=open(ofn,"wt")
    # maybe there's better option there
    of.write('<html><head><title>YT comments</title><meta charset="UTF-8"></head><body>\n')
    of.write("<form>\n")
    of.write("<ol>\n")
    nb=0
    ntot=len(self.data.values())
    itlist=self.data.values()
    itlist.sort()
    for item in itlist:
      nb+=1
      if ((self.args.only_for_url != None) and ((self.args.only_for_url not in item.url))):
        pass
      else:
        url=QUrl(item.url) # All that because cant pickle Qurl
        print ("Item "+str(nb)+"/"+str(ntot)+" - "+str(url))
        mdo=DomObject(self.args,url)
        mdo.buildRoot()
        views=mdo.getViews() # Failure is flagged as -1
        title=mdo.getTitle()
        item.addview(views)
        of.write(item.htmlWrite(title))
        of.flush()
        #item.views=views
        #sys.exit(0)
    of.write("</ol>\n")
    of.write("</form>")
    of.write("<p>"+str(datetime.datetime.now())+"</p>\n")
    of.write("<p>END of DATA</p>\n")
    of.write("</body><html>\n")
    of.close()
    

def get_cmd_options():
    """
        gets and validates the input from the command line
    """
    usage = "usage: %prog [options] args"
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-level"     , default=0          , help="Debug level")
    parser.add_argument("--update-database" , action='store_true', help="Update database")
    parser.add_argument("--upgrade-database", action='store_true', help="Upgrade database")
    parser.add_argument("--dont-be-lazy"    , action='store_true', help="Dont reuse already downloaded html files even if existing")
    parser.add_argument("--only-for-url"    ,                      help="Only url's matching this substring will be proccessed")
    args = parser.parse_args()

    return args

def main():
  if (not os.path.exists(os.path.join(kDATA_PATH,'html'  ))):
    os.makedirs(os.path.join(kDATA_PATH,'html'  ))
  args=get_cmd_options()
  db=Database(args)
  if (args.upgrade_database):
    print ("Upgrading database!!!")
    db.close()
    return
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
        
        
