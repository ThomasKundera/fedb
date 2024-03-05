#!/usr/bin/env python3
import json
import yattag



class Comment:
  def __init__(self,d):
    self.cid=d['cid']
    res=self.cid.split('.')
    if (len(res)==2):
      self.parent=res[0]
    else:
      self.parent=None
    self.text=d['text']
    self.author=d['author']
    self.channel=d['channel']
    self.votes=int(d['votes'])
    self.photo=d['photo']
    self.heart=d['heart']
    self.reply=d['reply']
    self.time_parsed=float(d['time_parsed'])
    #print(self)

  def __eq__(self, other):
    return (self.cid is other.cid)

  def __lt__(self, other):
    return (self.time_parsed < other.time_parsed)

  def __str__(self):
    s="cid: "+self.cid
    if (self.parent):
      s+=" with parent: "+self.parent
    return s

class OneThread:
  def __init__(self,parent):
    self.op=parent
    self.subcoms=[]

  def append(self,c):
    self.subcoms.append(c)


  def to_html(self,doc,tag,text,line):
    with tag('div'):
      line('p',self.op.cid)
      with tag('ul'):
        for c in self.subcoms:
          line('li',c.cid)


  def __str__(self):
    s=self.op.cid
    for c in self.subcoms:
      s+="\n"+c.cid+" "+str(c.time_parsed)
    s+="\n"
    return s


class YTPage:
  def __init__(self,pid):
    self.pid=pid
    self.read_comments()

  def read_comments(self):
    f = open(self.pid+'.json')
    data= json.load(f)

    self.cthreads={}

    i=0
    for cm in data['comments']:
      c=Comment(cm)
      if c.parent and (c.parent in self.cthreads):
        self.cthreads[c.parent].append(c)
      elif c.cid in self.cthreads:
        print("WARNING")
      else:
        self.cthreads[c.cid]=OneThread(c)
      i+=1
      if i>=100: break # FIXME for tests


  def generate_page(self):
    self.doc, self.tag, self.text, self.line = yattag.Doc().ttl()
    self.doc.asis('<!DOCTYPE html>')

    with self.tag('html'):
      with self.tag('body'):
        for t in self.cthreads.values():
          t.to_html(self.doc, self.tag, self.text, self.line)


    f=open(self.pid+".html","wt")
    f.write(self.doc.getvalue())


# --------------------------------------------------------------------------
def main():
  ytp=YTPage('DR1qnvMDh4w')
  ytp.generate_page()
  return

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        
