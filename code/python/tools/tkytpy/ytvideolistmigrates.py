#!/usr/bin/env python3
import time
import ytvideolist
import sqlqueue

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def init_db():
  ytvideolist.Base.metadata.create_all()
  print("Initialized the db")

# --------------------------------------------------------------------------
def main():
  import time
  import ytqueue
  logging.debug("ytvideolist migrates: START")
  init_db()
  dbsession=sqlqueue.SqlQueue().mksession()

  videos=ytvideolist.YTVideoList()

  #ytqueue.YtQueue().join()
  logging.debug("ytvideolist migrates: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
