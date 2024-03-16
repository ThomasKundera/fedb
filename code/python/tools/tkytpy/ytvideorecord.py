#!/usr/bin/env python3
import json
import requests
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import JSONType
from sqlalchemy.orm import Session

import ytqueue
import sqlqueue

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

Base = declarative_base(bind=sqlqueue.SqlQueue('tkyttest').engine)

def valid_url(url):
  r = requests.head(url)
  print(r)
  return(r.status_code == 200)


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
      dbsession=sqlqueue.SqlQueue().mksession()
    v=dbsession.query(YTVideo).get(self.yid)
    if not v:
      print("New video: "+self.yid)
      dbsession.add(self)
      self.populate_variables_dummy()
    else:
      self.copy_from(v)
    if not self.populated:
      self.call_populate()
    dbsession.commit()

  def populate_variables_dummy(self):
    self.populated     = False
    self.title         = self.url
    self.rawytdata     = None
    self.thumb_url_s   = ""
    self.rawytdatajson = "{}"

