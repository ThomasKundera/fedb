#!/usr/bin/env python3
import time
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

import sqlqueue

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

Base = declarative_base(bind=sqlqueue.SqlQueue().engine)

class TestClass(Base):
  __tablename__ = 'tktest'
  yid           = sqlalchemy.Column(sqlalchemy.Unicode(12),primary_key=True)
  title         = sqlalchemy.Column(sqlalchemy.Unicode(100))

  def __init__(self,yid):
    self.yid  =yid
    self.title="default title"
    self.db_create_or_load()

  def db_create_or_load(self):
    dbsession=sqlqueue.SqlQueue().mksession()
    tc= dbsession.query(TestClass).get(self.yid)
    if not tc:
      print("Entry didn't existe: "+self.yid)
      dbsession.add(self)
    else:
      self.title=dbsession.query(TestClass).get(self.yid).title
    dbsession.commit()
    dbsession.close()

  def direct_call_double_title(self):
    dbsession=sqlqueue.SqlQueue().mksession()
    self.queued_double_title(dbsession)
    dbsession.commit()
    dbsession.close()

  def call_double_title(self):
    task=sqlqueue.SqlTask(self.queued_double_title)
    sqlqueue.SqlQueue().add(task)

  def queued_double_title(self,dbsession):
    logging.debug("TestClass:queued_double_title: START")
    #time.sleep(5)
    item=dbsession.query(TestClass).get(self.yid)
    dbsession.add(item)
    title=dbsession.query(TestClass).get(self.yid).title
    title=title+"UTU"+title
    item.title=title[:80]
    #setattr(user, 'no_of_logins', User.no_of_logins + 1)
    logging.debug("TestClass:queued_double_title: END")

  def __str__(self):
    return self.yid+" "+self.title


def init_db():
  Base.metadata.create_all()
  print("Initialized the db")

# --------------------------------------------------------------------------
def main():
  import time
  logging.debug("sqlqueuetest test: START")
  init_db()
  yidlist=['j2GXgMIYgzU','iphcyNWFD10','aBr2kKAHN6M','aBr2kKAHN6M']
  while True:
    for yid in yidlist:
      t=TestClass(yid)
      print(t)
      t.call_double_title()
      time.sleep(2)
  sqlqueue.SqlQueue().close()
  logging.debug("tkyoutube test: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
