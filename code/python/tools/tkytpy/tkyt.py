#!/usr/bin/env python3
import tksingleton

import ytvideolist

class TkYt(metaclass=tksingleton.SingletonMeta):
  def __init__(self):
    return

  def setup(self):
    self.videos=ytvideolist.YTVideoList()


