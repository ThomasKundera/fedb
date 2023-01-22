#!/bin/bash

#echo "Using old data"
#exit 0

mkdir -p data/oldata/data/out1

cd data/oldata/data/out1

i=0

for img0 in `ls ../out0/*.png`; do
  echo $img0

  it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it

  img0=../out0/$img0
  img1=${it}.png

  ln -s $img0 $img1

  ((i=i+1))
done

