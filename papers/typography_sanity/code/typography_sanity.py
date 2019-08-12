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
  def __init__(self,cm,profanity):
    #self.comment=c
    self.setTypoScore(cm)
    self.setSanityScore(cm,profanity)
    # Load dictionnary
    
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
    
  def setSanityScore(self,cm,profanity):
    s=len(cm.split()) # FIXME can be buggy
    # convert to lower
    cml=cm.lower()
    np=0
    for w in profanity:
      np+=cml.count(w)
    self.saniscore=(1.0*np/s)
    if (self.saniscore>1): self.saniscore=1
    
    

class CommentBase:
  def __init__(self):
    self.cb=[]
    self.profanity=[]
    f=open("base-list-of-bad-words_text-file_2018_07_30.txt","rt")
    for line in f.readlines():
      w=line.strip()
      self.profanity.append(w)
  
  def append(self,c):
    co=Comment(c,self.profanity)
    self.cb.append(co)
  
  def plot(self):
    tt=[]
    ts=[]
    for c in self.cb:
      tt.append(c.typoscore)
      ts.append(c.saniscore)
    print ("Number of comments analysed: "+str(len(ts)))
    #plt.hist(ts,log=True)
    #plt.show()
    counts,xbins,ybins, img=plt.hist2d(tt,ts)
    #plt.show()
    tm=[]
    for ix in range(len(counts)):
      n=0.
      m=0.
      for iy in range(len(counts[ix])):
        n+=counts[ix][iy]
        m+=counts[ix][iy]*( ybins[iy+1]-ybins[iy] )/2.
      if (n!=0): tm.append(m/n)
      else: tm.append(0)
      print (m)
 
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
    if (not (n%100)): print (str(n))
    if (n>20): break
    analyse_file(f,cb)
  cb.plot()


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()