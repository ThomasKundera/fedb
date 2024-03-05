#!/usr/bin/env python3
import json

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

  def __str__(self):
    s=self.op.cid
    for c in self.subcoms:
      s+="\n"+c.cid+" "+str(c.time_parsed)
    s+="\n"
    return s

# --------------------------------------------------------------------------
def main():
  f = open('DR1qnvMDh4w.json')
  data= json.load(f)

  cthreads={}

  i=0
  for cm in data['comments']:
    c=Comment(cm)
    if c.parent and (c.parent in cthreads):
      cthreads[c.parent].append(c)
    elif c.cid in cthreads:
      print("WARNING")
    else:
      cthreads[c.cid]=OneThread(c)

    i+=1
    if i>=100: break

  for v in cthreads.values():
    print(v)
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        
