#!/usr/bin/env python3
import os
import json
import yattag
import requests
import shutil
import threading
import queue
import time
import datetime

# From https://refactoring.guru/fr/design-patterns/singleton/python/example
class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: threading.Lock = threading.Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DownloadThreaded(metaclass=SingletonMeta):
  lastuse: datetime.datetime = None

  def __init__(self):
    self.lastuse=datetime.datetime.now()
    self.q=queue.Queue()
    threading.Thread(target=self.worker, daemon=True).start()

  def worker(self):
      while True:
          item = self.q.get()
          print(f'Working on {item}')
          time.sleep(10)
          url,fn=item
          res = requests.get(url, stream = True)
          if res.status_code == 200:
            with open(fn,'wb') as f:
              shutil.copyfileobj(res.raw, f)
            print('OK download: ',fn)
          else:
            print('FAILED download:'+url)

          #print(f'Finished {item}')
          self.q.task_done()

  def queueDownload(self,url,fout):
    self.q.put((url,fout))
    return

  def join(self):
    self.q.join()


class ProfilPict:
  def __init__(self):
    self.ppdir="profilepics"
    try:
      os.makedirs(self.ppdir, exist_ok=True)
    except OSError as error:
      print(error)

  def url2fn(self,url):
    fn=os.path.join(self.ppdir,url.split('/')[-1])
    return(fn)

  def download(self,url):
    f=self.url2fn(url)
    if (os.path.isfile(f)):
      print("IMG already downloaded")
      return
    dt=DownloadThreaded()
    dt.queueDownload(url,f)



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
    pp=ProfilPict()
    pp.download(self.photo)
    self.heart=d['heart']
    self.reply=d['reply']
    self.time_parsed=float(d['time_parsed'])
    #print(self)

  def to_html(self,doc,tag,text,line):
    with tag('table'):
      with tag('tr'):
        with tag('td'):
          line('span',self.photo)
          line('span',self.author)
        with tag('td'):
          line('p',self.text)


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
      with tag('div'):
        for c in self.subcoms:
          c.to_html(doc,tag,text,line)


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
      if i>=5: break


  def generate_page(self):
    self.doc, self.tag, self.text, self.line = yattag.Doc().ttl()
    self.doc.asis('<!DOCTYPE html>')

    with self.tag('html'):
      with self.tag('body'):
        for t in self.cthreads.values():
          t.to_html(self.doc, self.tag, self.text, self.line)


    f=open(self.pid+".html","wt")
    f.write(yattag.indent(self.doc.getvalue(), indent_text = True))

# --------------------------------------------------------------------------
def main():
  ytp=YTPage('DR1qnvMDh4w')
  ytp.generate_page()

  # Wait end of queue
  dt=DownloadThreaded()
  dt.join()

  return

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        
