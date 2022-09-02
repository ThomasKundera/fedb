#!/usr/bin/env python3

import datetime


def main():
  # Computing year fraction starting from winter solstice
  
  # Date of winter solstice in 2015
  utc2015WinterSolstice=datetime.datetime.fromisoformat("2015-12-22 04:48:00.000+00:00")
  
  # Duration of an astronomical year
  yearDuration=datetime.timedelta(days=365.2425)
  
  # Date of the picture
  utcDateOfPicture=datetime.datetime.fromisoformat("2015-07-16 19:50:00.000+00:00")
  
  detaTime=utcDateOfPicture-utc2015WinterSolstice
  
  print(utc2015WinterSolstice)
  print(yearDuration)
  print(utcDateOfPicture)
  print(detaTime)
  print(detaTime/yearDuration)
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



