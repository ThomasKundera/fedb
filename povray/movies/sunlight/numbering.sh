#!/bin/bash

mkdir -p data/out1

cd data/out1

i=0

for img0 in `ls ../inputimages/`; do
  echo $img0

  it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it

  img0=../inputimages/$img0
  img1=sequence${it}.png

  ln -s $img0 $img1

  ((i=i+1))
done

