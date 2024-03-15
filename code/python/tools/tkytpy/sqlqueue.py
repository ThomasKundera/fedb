#!/usr/bin/env python3
import time

from tksecrets import localsqldb_pass
import tkqueue

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class TkSqlTask(tkqueue.TkTask):
  def run(self,dbsession):
    self.run(dbsession)

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
    sqlproto='mysql+mysqlconnector'
    sqluser='tkyt'
    sqlstring = sqlproto+'://'+sqluser+'@'+localsqldb_pass+'@localhost/tkyt'
    self.engine = create_engine(sqlstring, echo=True)
    session_factory = sessionmaker(bind=self.engine)
    mksession = scoped_session(session_factory)
    self.dbsession=mksession()
    super().__init__()

  def do_work(self,item):
    item.run(self.dbsession)
