#!/bin/bash

BASEDIR=./data/oldata/data/

mkdir -p $BASEDIR/out5

for i in `seq 365`; do
    it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it
  
  img0=$BASEDIR/out1/${it}.jpg
  img1=$BASEDIR/out2/${i}-flat.jpg
  img2=$BASEDIR/out3/sequence${it}.png
  img3=$BASEDIR/out4/sequence${it}.png
  imgOUT=$BASEDIR/out5/sequence${it}.png

  montage -background black  -geometry 950x540 -tile 2x2 $img0 -resize 400x400 $img2 $img1 $img3 -resize 1900x1080 $imgOUT

  exit 0
done
