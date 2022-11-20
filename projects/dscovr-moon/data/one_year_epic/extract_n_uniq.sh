#!/bin/bash

/bin/rm -f extract*.png

ffmpeg -ss 0:02:50 -i 'DSCOVR - one year of EPIC images - YouTube.webm' -t  0:00:08 extract%05d.png

/bin/rm -f extract0000*.png extract0001*.png extract0002*.png extract0003*.png  extract0004*.png extract0005*.png extract00456.png

# Dummy
refimg=out.png

for img in `ls extract*.png`; do
  echo "------------- $refimg $img"
  res=`findimagedupes -t 99% $refimg $img`
  echo $res
  echo $res | grep png
  if [ $? -eq 1 ]; then
    echo differ
    refimg=$img
  else
    echo same
    /bin/rm -f $img
  fi
done


