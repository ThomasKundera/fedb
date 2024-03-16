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

class YTVideo2(Base):
  __tablename__ = 'ytvideos2'
  yid           = sqlalchemy.Column(sqlalchemy.Unicode(12),primary_key=True)
  valid         = sqlalchemy.Column(sqlalchemy.Boolean)
  populated     = sqlalchemy.Column(sqlalchemy.Boolean)
  url           = sqlalchemy.Column(sqlalchemy.Unicode(100))
  title         = sqlalchemy.Column(sqlalchemy.Unicode(200))
  rawytdatajson = sqlalchemy.Column(           JSONType)

  def __init__(self,yid):
    self.yid=yid.strip()
    self.db_create_or_load()

  def db_create_or_load(self):
    dbsession=Session.object_session(self)
    if not dbsession:
      dbsession=sqlqueue.SqlQueue().mksession()
    v=dbsession.query(YTVideo).get(self.yid)
    self.copy_from(v)
    dbsession.commit()

  def copy_from(self,o):
    self.valid            =o.valid
    self.populated        =o.populated
    self.url              =o.url
    self.title            =o.title


class YTVideo(Base):
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
    self.url='https://www.youtube.com/watch?v='+self.yid
    if not self.is_valid_id():
      print("Not valid yid:"+self.yid)
      self.valid=False
      return
    self.valid=True
    self.populated= False
    self.db_create_or_load()

  def copy_from2(self,o):
    self.valid            =o.valid
    self.populated        =o.populated
    self.url              =o.url
    self.title            =o.title
    self.rawytdatajson    =o.rawytdatajson

  def copy_from(self,o):
    self.copy_from2(o)
    self.thumb_url_s=o.thumb_url_s

  def db_create_or_load(self):
    #dbsession=sqlqueue.SqlQueue().mksession()
    dbsession=Session.object_session(self)
    if not dbsession:
      dbsession=sqlqueue.SqlQueue().mksession()
    v=dbsession.query(YTVideo).get(self.yid)
    if not v:
      print("New video: "+self.yid)
      self.populate_variables_dummy()
      dbsession.add(self)
    else:
      self.copy_from(v)

    if not self.populated:
      self.call_populate()
    dbsession.commit()
    #dbsession.close()

  def resurect(self):
    if not self.valid: return
    if not self.rawytdatajson:
      self.populate_variables_dummy()
    print("- "+self.rawytdatajson+" -")
    self.rawytdata=json.loads(self.rawytdatajson)
    if self.populated: return
    self.call_populate()

  def call_populate(self):
    task=ytqueue.YtTask('populate:'+self.yid,self.queued_populate)
    ytqueue.YtQueue().add(task)

  def queued_populate(self,youtube):
    dbsession=sqlqueue.SqlQueue().mksession()
    v=dbsession.query(YTVideo).get(self.yid)
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


  def is_valid_id(self):
    if (len(self.yid) != 11): return False
    return valid_url(self.url)

  def populate_variables_dummy(self):
    self.populated=False
    self.title=self.url
    self.rawytdata = None
    self.rawytdatajson = "{}"


  def get_dict(self):
    return {
      'yid'  : self.yid,
      'url'  : self.url,
      'title': self.title
      }

  def __str__(self):
    return self.yid

  def dump(self):
    return {
      'valid': self.valid,
      'populated': self.populated,
      'yid'  : self.yid,
      'url'  : self.url,
      'title': self.title
      }

class YTVideo3(YTVideo):
  def __init__(self,v2):
    self.yid=v2.yid
    self.copy_from2(v2)
    self.db_create_or_load()

# --------------------------------------------------------------------------
class YTVideoList:
  def __init__(self):
    logging.debug("YTVideoList.__init__(): START")
    self.videos={}
    logging.debug("YTVideoList.__init__(): 1")
    print(sqlqueue)
    print(sqlqueue.SqlQueue)
    print(sqlqueue.SqlQueue())
    dbsession=sqlqueue.SqlQueue().mksession()
    logging.debug("YTVideoList.__init__(): 2")
    self.fill_from_db(dbsession)
    dbsession.commit()
    dbsession.close()
    logging.debug("YTVideoList.__init__(): END")

  def call_fill_from_db(self):
    task=sqlqueue.SqlTask(self.fill_from_db)
    sqlqueue.SqlQueue().add(task)

  def fill_from_db2to3(self,dbsession):
    logging.debug("YTVideoList.fill_from_db(): START")
    for v2 in dbsession.query(YTVideo2):
      v3=YTVideo(v2.yid)
      v3.copy_from2(v2)
      self.videos[v3.yid]=v3
    logging.debug("YTVideoList.fill_from_db(): END")

  def fill_from_db(self,dbsession):
    logging.debug("YTVideoList.fill_from_db(): START")
    for v in dbsession.query(YTVideo):
      v.resurect()
      logging.debug("YTVideoList.fill_from_db(): video: "+str(v.dump()))
      self.videos[v.yid]=v
    logging.debug("YTVideoList.fill_from_db(): END")

  def add_from_yid(self,yid):
    dbsession=sqlqueue.SqlQueue().mksession()
    v=YTVideo(yid)
    self.add(v)
    dbsession.close()

  def add(self,v):
    if (v.valid):
      self.videos[v.yid]=v
    else:
      print("Not adding invalid video: "+str(v))

  def to_dict(self):
    l=[]
    for v in self.videos.values():
      print("video: "+str(v))
      if v.valid:
        l.append(v.get_dict())
    return  {'ytvlist': l}

