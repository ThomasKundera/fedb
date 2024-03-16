#!/usr/bin/env python3
import requests

from ytvideorecord import YTVideoRecord

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# --------------------------------------------------------------------------
def valid_url(url):
  r = requests.head(url)
  print(r)
  return(r.status_code == 200)


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
class YTVideo(YTVideoRecord):
  def __init__(self,yid):
    self.yid=yid.strip()
    self.url='https://www.youtube.com/watch?v='+self.yid
    if not self.is_valid_id():
      print("Not valid yid:"+self.yid)
      self.valid=False
      return
    self.valid=True
    self.populated= False
    super().__init__(self.yid)

  def resurect(self):
    if not self.valid: return
    if not self.rawytdatajson:
      self.populate_variables_dummy()
    print("- "+self.rawytdatajson+" -")
    self.rawytdata=json.loads(self.rawytdatajson)
    if self.populated: return
    self.call_populate()

  def is_valid_id(self):
    if (len(self.yid) != 11): return False
    return valid_url(self.url)

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
