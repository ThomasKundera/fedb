#!/usr/bin/env python3
import sqlqueue

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

Base = declarative_base(bind=SqlQueue().engine)

class TestClass(Base):
  __tablename__ = 'tktest'
  yid           = sqlalchemy.Column(sqlalchemy.Unicode(12),primary_key=True)
  title         = sqlalchemy.Column(sqlalchemy.Unicode(100))

  def __init__(self,yid):
    self.yid=yid
    time.sleep(1)
    task=sqlqueue.SqlQueue('populate:'+self.yid,self.populate_variables_from_youtube)
    YtQueue().add(task)

  def commit_in_db(self):
    logging.debug("YTVideoList.commit_in_db: START")
    dbsession = mksession()
    try:
      dbsession.add(self)
    except sqlite3.IntegrityError:
      dbsession.merge(self)
    dbsession.commit()
    dbsession
    logging.debug(self.dump())
    logging.debug("YTVideoList.commit_in_db: END")



# --------------------------------------------------------------------------
def main():
  logging.debug("tkyoutube test: START")

  t1=TestClass('j2GXgMIYgzU')
  t1=TestClass('iphcyNWFD10')
  t1=TestClass('aBr2kKAHN6M')
  t1=TestClass('aBr2kKAHN6M')

  YtQueue().join()
  logging.debug("tkyoutube test: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
