#!/usr/bin/env python3
import threading
import queue
import time
import datetime

import tksingleton

class TkTask:
  def __init__(self,tid,run):
    self.tid=tid
    self.run=run

  def run(self):
    self.run()

  def __str__(self):
    return self.tid

class QueueWork(metaclass=tksingleton.SingletonMeta):
  lastuse: datetime.datetime = None

  def __init__(self):
    self.lastuse=datetime.datetime.now()
    self.q=queue.Queue()
    self.taskdict={}
    threading.Thread(target=self.worker, daemon=True).start()

  def worker(self):
    while True:
      item = self.q.get()
      print(f'Working on {item} ( about '+str(self.q.qsize())+' elements remaining )')
      item.run()
      self.q.task_done()
      time.sleep(1)
      del self.taskdict[item.tid]

  def add(self,item):
    if item.tid in self.taskdict:
      print("Task {item} already in queue")
      return False
    self.taskdict[item.tid]=item.tid
    self.q.put(item)
    return

  def join(self):
    self.q.join()

