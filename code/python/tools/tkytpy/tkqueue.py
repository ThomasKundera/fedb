#!/usr/bin/env python3
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

class TkTask:
  def __init__(self,tid,run):
    self.tid=tid
    self.run=run

  def run(self):
    self.run()

  def __str__(self):
    return self.tid

class QueuWork(metaclass=SingletonMeta):
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
          time.sleep(10)
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

