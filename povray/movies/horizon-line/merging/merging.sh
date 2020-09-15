#!/bin/bash

for i in `seq 750`; do
  it=$i
  if   [ $i -lt  10 ]; then
    it='00'${i}
  elif [ $i -lt 100 ]; then
    it='0'${i}
  fi
  echo $it
  
  imgA=../seq2a/sequence${it}.png
  imgB=../seq2b/sequence${it}.png
  imgC=../seq2c/sequence${it}.png
  imgOUT=sequence${it}.png
 
  convert   $imgA -page +830+20 $imgB   -page +450+165 $imgC  -layers merge $imgOUT
  #-alpha set -channel a -evaluate set 50% +channel 
  #exit 0
done
