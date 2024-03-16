#!/usr/bin/env python3
from httpserver import HttpServer

class CmdNView:
  def __init__(self,tkyt):
    self.server=HttpServer(tkyt)
    return


  def run(self):
    self.server.run()
    return



