#!/bin/bash

mkdir -p data/out2

i=0

for img0 in `ls data/inputimages/`; do
  echo $img0

  it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it

  img0=data/inputimages/$img0
  img1=data/out2/sequence${it}.png

  convert $img0 +distort Polar 0 $img1

  ((i=i+1))
done

