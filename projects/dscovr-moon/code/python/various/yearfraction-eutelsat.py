#!/usr/bin/env python3

import datetime


def main():
  # Computing year fraction starting from fdirst of january
  
  # January 2015
  utc2015NewYear=datetime.datetime.fromisoformat("2015-01-01 00:00:00.000+00:00")
  
  # Duration of 2015
  yearDuration=datetime.timedelta(days=365)
  
  # Begining and end
  utcStart=datetime.datetime.fromisoformat("2015-07-16 19:50:00.000+00:00")
  utcEnd=datetime.datetime.fromisoformat("2015-07-16 20:45:00.000+00:00")
  #utcDateOfPicture=datetime.datetime.fromisoformat("2015-09-23 19:50:00.000+00:00")
    
  deltaStart=utcStart-utc2015NewYear
  deltaStop =utcEnd-utc2015NewYear
  
  videoDuration=datetime.timedelta(minutes=8,seconds=44.421)
  fracStart=videoDuration*(deltaStart/yearDuration)
  fracStop =videoDuration*(deltaStop/yearDuration)
  
  
  print(fracStart)
  print(fracStop)
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



