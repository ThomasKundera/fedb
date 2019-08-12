#!/usr/bin/env python
# Have to use python 2 for mathplotlib for now :('
import os
import string
from lxml import html
import matplotlib.pyplot as plt


kDATA_PATH="./html"


def debug_print(l,t,s):
  if(l>=t):
    print (s)

class Comment:
  def __init__(self,cm):
    #self.comment=c
    self.setTypoScore(cm)
    #self.setSanityScore(cm)
    
  def setTypoScore(self,cm):
    s=len(cm)
    nc=0 # Number of caps
    nt=0 # Number of transition nocaps2cap
    np=0 # Number of repeated puctuation maks
    
    ft=False
    fp=0
    fpp=0
    for c in cm:
      if (not len(c.strip())): # c is some space
        ft=False
      if (c.isupper()):
        nc+=1
        ft=True
      else:
        if (ft):
          nt+=1
          ft=False
      if (c == '.'):
        fpp+=1
        if (fpp>=3):
          np+=1
      elif (c in string.punctuation):
        fp+=1
        if (fp>1):
          np+=1
      else:
        fpp=0
        fp=0
      
    self.typoscore=(1.0*(nc+nt+np))/s
    #if (self.typoscore>.5): print(cm)
    
  def setSanityScore(self,cm):
    
    
    

class CommentBase:
  def __init__(self):
    self.cb=[]
  
  def append(self,c):
    co=Comment(c)
    self.cb.append(co)
  
  def plot(self):
    ts=[]
    for c in self.cb:
      ts.append(c.typoscore)
    print ("Number of comments analysed: "+str(len(ts)))
    plt.hist(ts,log=True)
    plt.show()
  
  def dump(self):
    for c in self.cb:
      print (c.typoscore)

class DomObject:
  def __init__(self,f):
    self.f=f

  def buildRoot(self):
    tree=html.parse(self.f)
    self.root = tree.getroot()
  
  def getComments(self,cb):
    crcl=self.root.find_class("comment-renderer-text-content")
    for crc in crcl:
      cb.append(crc.text_content())

def analyse_file(f,cb):
  #print (f)
  tree=DomObject(f)
  tree.buildRoot()
  tree.getComments(cb)
  
  

# --------------------------------------------------------------------------
def main():
  path = kDATA_PATH
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      files.append(os.path.join(r, file))
  n=0
  cb=CommentBase()
  for f in files:
    n+=1
    if (not (n%1000)): print (str(n))
    #if (n>100): break
    analyse_file(f,cb)
  cb.plot()


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()