#!/usr/bin/env python3
from cmdnview     import CmdNView
from filestorage  import FileStorage
from fieldstorage import FieldStorage
from tkyt         import TkYt

class Manager:
  def __init__(self):
    self.file_storage  = FileStorage ()
    self.field_storage = FieldStorage()
    self.tkyt          = TkYt(self.field_storage)
    self.tkyt.setup()
    self.cmd_n_view    = CmdNView    (self.tkyt)

  def run(self):
    self.cmd_n_view.run()
    return

# --------------------------------------------------------------------------
def main():
  manager=Manager()
  manager.run()


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
        
