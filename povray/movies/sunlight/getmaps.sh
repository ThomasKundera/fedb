#!/bin/bash

BASEURL=https://www.timeanddate.com/scripts/sunmap.php?iso=
20170206T1646
for month in `seq 1 12` ; do
  if [ $month -lt 10 ]; then month="0$month"; fi
  for day in `seq 1 30`; do
    if [ $day   -lt 10 ]; then   day="0$day";   fi
    thedate="2017${month}${day}T1200"
    URL="${BASEURL}$thedate"
    echo $URL
    wget -nc  -O "data/${thedate}.png"  $URL
    sleep 2
  done
done

