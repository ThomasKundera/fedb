#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy_utils import JSONType
from sqlalchemy.orm import Session

from sqlsingleton import SqlSingleton, Base

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
class YTVideoRecord(Base):
  __tablename__ = 'ytvideos3'
  yid           = sqlalchemy.Column(sqlalchemy.Unicode(12),primary_key=True)
  valid         = sqlalchemy.Column(sqlalchemy.Boolean)
  populated     = sqlalchemy.Column(sqlalchemy.Boolean)
  url           = sqlalchemy.Column(sqlalchemy.Unicode(100))
  title         = sqlalchemy.Column(sqlalchemy.Unicode(200))
  thumb_url_s   = sqlalchemy.Column(sqlalchemy.Unicode(100))
  rawytdatajson = sqlalchemy.Column(           JSONType)

  def __init__(self,yid):
    self.yid=yid.strip()
    self.db_create_or_load()

  def copy_from(self,o):
    self.valid            =o.valid
    self.populated        =o.populated
    self.url              =o.url
    self.title            =o.title
    self.rawytdatajson    =o.rawytdatajson
    self.thumb_url_s=o.thumb_url_s

  def db_create_or_load(self):
    dbsession=Session.object_session(self)
    if not dbsession:
      dbsession=SqlSingleton().mksession()
    v=dbsession.query(YTVideoRecord).get(self.yid)
    if not v:
      print("New video: "+self.yid)
      dbsession.add(self)
      self.populate_variables_dummy()
    else:
      self.copy_from(v)
    if not self.populated:
      self.call_populate()
    dbsession.commit()

  def call_populate(self):
    task=ytqueue.YtTask('populate:'+self.yid,self.queued_populate)
    ytqueue.YtQueue().add(task)

  def queued_populate(self,youtube):
    dbsession=SqlSingleton().mksession()
    v=dbsession.query(YTVideoRecord).get(self.yid)
    dbsession.add(v)
    request=youtube.videos().list(part='snippet,statistics', id=self.yid)
    v.rawytdata = request.execute()
    if len(v.rawytdata['items']) != 1:
      v.valid=False
    else:
      v.rawytdatajson=json.dumps(v.rawytdata)
      #print(v.rawytdatajson)
      #print(v.rawytdata)
      v.title=v.rawytdata['items'][0]['snippet']['title']
      v.populated=True
    dbsession.commit()
    dbsession.close()

  def populate_variables_dummy(self):
    self.populated     = False
    self.title         = self.url
    self.rawytdata     = None
    self.thumb_url_s   = ""
    self.rawytdatajson = "{}"

