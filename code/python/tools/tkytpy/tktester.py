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

# Create a new Http() object for every request
def build_request(http, *args, **kwargs):
  new_http = google_auth_httplib2.AuthorizedHttp(credentials, http=httplib2.Http())
  return googleapiclient.http.HttpRequest(new_http, *args, **kwargs)
authorized_http = google_auth_httplib2.AuthorizedHttp(credentials, http=httplib2.Http())
service = discovery.build('api_name', 'api_version', requestBuilder=build_request, http=authorized_http)

# Pass in a new Http() manually for every request
service = discovery.build('api_name', 'api_version')
http = google_auth_httplib2.AuthorizedHttp(credentials, http=httplib2.Http())
service.stamps().list().execute(http=http)


# --------------------------------------------------------------------------
def main():
  logging.debug("main: START")


  logging.debug("main: END")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

