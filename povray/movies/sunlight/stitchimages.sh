#!/bin/bash

for i in `seq 365`; do
    it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it
  
  img0=data/${i}.jpg
  img1=out1/sequence${it}.png
  img2=out2/sequence${it}.png
  img3=out3/sequence${it}.png
  imgOUT=out4/sequence${it}.png

  montage -mode concatenate  -tile 2x2 $img0 -resize 200x300 $img2 $img1 $img3 $imgOUT
  exit 0
done
