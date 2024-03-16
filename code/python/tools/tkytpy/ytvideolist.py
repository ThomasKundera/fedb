#!/usr/bin/env python3

from ytvideo import YTVideo

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


# --------------------------------------------------------------------------
class YTVideoList:
  def __init__(self,field_storage):
    logging.debug("YTVideoList.__init__(): START")
    self.field_storage=field_storage
    self.videos=self.field_storage.get_videos()

  def add_from_yid(self,yid):
    v=YTVideo(yid)
    return self.add(v)

  def add(self,v):
    if not v.valid:
      logging.debug("Not adding invalid video: "+str(v))
      return False
    self.videos[v.yid]=v

  def get_video_dict(self):
    l=[]
    for v in self.videos.values():
      print("video: "+str(v))
      if v.valid:
        l.append(v.get_dict())
    return  {'ytvlist': l}

