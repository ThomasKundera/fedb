#!/bin/bash

echo "Using old data"
exit 0

BASEURL=https://www.timeanddate.com/scripts/sunmap.php?iso=
#20170206T1646

mkdir -p data/inputimages

for month in `seq 1 12` ; do
  if [ $month -lt 10 ]; then month="0$month"; fi
  for day in `seq 1 31`; do
    if [ $day   -lt 10 ]; then   day="0$day";   fi
    thedate="2017${month}${day}T1200"
    URL="${BASEURL}$thedate"
    echo $URL
    if [ -f "data/inputimages/${thedate}.png" ]; then
      echo "File already here"
    else
      wget -nc  -O "data/inputimages/${thedate}.png"  $URL
      sleep 2
    fi
  done
done

