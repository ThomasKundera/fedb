#!/bin/bash

for i in `seq 365`; do
    it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it
  
  img0=data/inputimages/${i}.jpg
  img1=data/out1/sequence${it}.png
  img2=data/out2/sequence${it}.png
  img3=data/out3/sequence${it}.png
  imgOUT=data/out4/sequence${it}.png

  montage -mode concatenate  -tile 2x2 $img0 -resize 1900x1080 $img2 $img1 $img3 $imgOUT
done
