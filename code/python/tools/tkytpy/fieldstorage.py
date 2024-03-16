#!/usr/bin/env python3
from sqlsingleton import SqlSingleton, Base

from ytvideo import YTVideo

class FieldStorage:
  def __init__(self):
    Base.metadata.create_all()
    return

  def get_videos(self):
    dbsession=SqlSingleton().mksession()
    vl={}
    for v in dbsession.query(YTVideo):
      vl[v.yid]=v
    return vl
