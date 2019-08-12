#!/usr/bin/env python3
import os
from lxml import html


kDATA_PATH="./html"


def debug_print(l,t,s):
  if(l>=t):
    print (s)

class Comment:
  def __init__(self,c):
    #self.comment=c
    self.setTypoScore(c)
    self.setSanityScore(c)
    
  def setTypoScore(self,c):
    s=len(c)
    nc=0 # Number of caps
    nt=0 # Number of transion nocaps2cap
    np=0 # Number of 
    

class CommentBase:
  def __init__(self):
    self.cb=[]
  
  def append(self,c):
    co=Comment(c)
    self.cb.append(co)

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

def analyse_file(f):
  print (f)
  cb=CommentBase()
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

  for f in files:
    analyse_file(f)



# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()