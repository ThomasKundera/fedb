#!/usr/bin/env python3
import time
import ytvideolist

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def init_db():
  ytvideolist.Base.metadata.create_all()
  print("Initialized the db")

# --------------------------------------------------------------------------
def main():
  import time
  import ytqueue
  logging.debug("ytvideolist test: START")
  init_db()
  yidlist=['j2GXgMIYgzU','iphcyNWFD10','aBr2kKAHN6M','aBr2kKAHN6M']

  vl=ytvideolist.YTVideoList()
  for yid in yidlist:
    vl.add(ytvideolist.YTVideo(yid))

  ytqueue.YtQueue().join()
  logging.debug("tkyoutube test: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
