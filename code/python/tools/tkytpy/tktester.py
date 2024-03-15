#!/usr/bin/env python3
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
import mysql.connector

import tksecrets

from sqlalchemy import create_engine


sqlproto='mysql+mysqlconnector'
sqluser='tkyt'
sqlstring = sqlproto+'://'+sqluser+'@'+tksecrets.localsqldb_pass+'@localhost/tkyt'
engine = create_engine(sqlstring, echo=True)



# --------------------------------------------------------------------------
def main():
  logging.debug("main: START")


  logging.debug("main: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

