#!/usr/bin/env python3
import threading
import queue
import time
import datetime

import tksingleton

class TkTask:
  def __init__(self,task):
    self.task=task

  def run(self):
    self.task()

  def __str__(self):
    return str(self.task)

class TkTaskUniq(TkTask):
  def __init__(self,tid,task):
    self.tid=tid
    self.task=task

  def run(self):
    self.task()

  def __str__(self):
    return self.tid

class QueueWork(metaclass=tksingleton.SingletonMeta):
  lastuse: datetime.datetime = None

  def __init__(self):
    self.lastuse=datetime.datetime.now()
    self.q=queue.Queue()
    threading.Thread(target=self.worker, daemon=True).start()

  def do_work(self,item):
    item.run()


  def worker(self):
    while True:
      item = self.q.get()
      print(f'Working on {item} ( about '+str(self.q.qsize())+' elements remaining )')
      self.do_work(item)
      self.q.task_done()
      #time.sleep(1)

  def add(self,item):
    self.q.put(item)

  def join(self):
    self.q.join()


# This class prevents two requests having same id to be queued
class QueueWorkUniq(QueueWork):
  lastuse: datetime.datetime = None

  def __init__(self):
    self.taskdict={}
    super().__init__()

  def do_work(self,item):
    super().do_work(item)
    del self.taskdict[item.tid]

  def add(self,item):
    if item.tid in self.taskdict:
      print("Task {item} already in queue")
      return False
    self.taskdict[item.tid]=item.tid
    super().add(item)


