#!/usr/bin/env python3
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

  def __str__(self):
    return self.yid+" "+self.title


def init_db():
  Base.metadata.create_all()
  print("Initialized the db")

# --------------------------------------------------------------------------
def main():
  import time
  logging.debug("tkyoutube test: START")
  init_db()
  yidlist=['j2GXgMIYgzU','iphcyNWFD10','aBr2kKAHN6M','aBr2kKAHN6M']
  while True:
    for yid in yidlist:
      t=TestClass(yid)
      print(t)
      time.sleep(2)
  sqlqueue.SqlQueue().close()
  logging.debug("tkyoutube test: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
