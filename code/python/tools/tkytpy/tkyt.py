#!/usr/bin/env python3
import tksingleton

import ytvideolist

class TkYt(metaclass=tksingleton.SingletonMeta):
  def __init__(self,field_storage):
    self.field_storage=field_storage
    return

  def setup(self):
    self.videos=ytvideolist.YTVideoList(self.field_storage)

  def add_video(self,yid):
    self.videos.add_from_yid(yid)

  def get_video_list(self):
    return self.videos.get_video_dict()


