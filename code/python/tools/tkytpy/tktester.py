#!/usr/bin/env python3
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
import mysql.connector

import tksecrets

#from sqlalchemy import create_engine
#connection_string = "mysql+mysqlconnector://user1:pscale_pw_abc123@us-east.connect.psdb.cloud:3306/sqlalchemy"
#engine = create_engine(connection_string, echo=True)

cnx = mysql.connector.connect(user='tkyt', password=tksecrets.localsqldb_pass,
                              host='127.0.0.1',
                              database='tkyt')
cnx.close()



# --------------------------------------------------------------------------
def main():
  logging.debug("main: START")


  logging.debug("main: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

