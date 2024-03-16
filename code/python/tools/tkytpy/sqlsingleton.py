#!/usr/bin/env python3
import time
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

from tksecrets import localsqldb_pass

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

import tksingleton

class SqlSingleton(metaclass=tksingleton.SingletonMeta):
  def __init__(self,db='tkyt'):
    db_url = sqlalchemy.engine.URL.create(
      drivername="mysql+mysqlconnector",
      username="tkyt",
      password=localsqldb_pass,
      host="127.0.0.1",
      database=db,
    )
    self.engine = sqlalchemy.create_engine(db_url, echo=True)
    self.session_factory = sessionmaker(bind=self.engine)
    #self.mksession = self.session_factory
    self.mksession = scoped_session(self.session_factory)
    super().__init__()

  def close(self):
     self.engine.dispose()


Base = declarative_base(bind=SqlSingleton('tkyttest').engine)


def classtest():
  from sqlalchemy.ext.declarative import declarative_base
  Base = declarative_base(bind=SqlSingleton().engine)
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
