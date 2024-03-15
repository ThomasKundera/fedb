#!/usr/bin/env python3
import time
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from tksecrets import localsqldb_pass
import tkqueue

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class SqlTask(tkqueue.TkTask):
  def run(self,dbsession):
    self.task(dbsession)

# Of course this task makes way less sense than the
# ggl api one (when we have limited access), however
# this looks simple enough for now.
# ENHANCE: swicth to a priority queue to favor interactive tasks

# There will only be one instance of this,
# as it derivates from SingletonMeta
# Thus, we can queue SQL requests here,
# without worrying of multitheads (hoppefully)
class SqlQueue(tkqueue.QueueWork):
  def __init__(self):
    db_url = sqlalchemy.engine.URL.create(
      drivername="mysql+mysqlconnector",
      username="tkyt",
      password=localsqldb_pass,
      host="127.0.0.1",
      database="tkyt",
    )
    self.engine = sqlalchemy.create_engine(db_url, echo=True)
    session_factory = sessionmaker(bind=self.engine)
    self.mksession = scoped_session(session_factory)
    super().__init__()

  def do_work(self,item):
    dbsession=self.mksession()
    item.run(dbsession)
    dbsession.commit()
    dbsession.close()

  def close(self):
     self.engine.dispose()


def classtest():
  from sqlalchemy.ext.declarative import declarative_base
  Base = declarative_base(bind=SqlQueue().engine)
  Base.metadata.create_all()

def directtest():
  sqlproto='mysql+mysqlconnector'
  sqluser='tkyt'
  connection_url = sqlalchemy.engine.URL.create(
    drivername="mysql+mysqlconnector",
    username="tkyt",
    password=localsqldb_pass,
    host="127.0.0.1",
    database="tkyt",
  )
  engine = sqlalchemy.create_engine(connection_url, echo=True)
  from sqlalchemy.ext.declarative import declarative_base
  Base = declarative_base(bind=engine)
  Base.metadata.create_all()

# --------------------------------------------------------------------------
def main():
  logging.debug("sqlqueue test: START")
  #directtest()
  classtest()
  logging.debug("sqlqueue test: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
