#!/bin/bash

for i in `seq 0 21`; do
  let "nb=29 * $i"
  s=""
  if [ $nb -lt  10 ]; then s=${s}"0"; fi
  if [ $nb -lt 100 ]; then s=${s}"0"; fi
  
  wget https://svs.gsfc.nasa.gov/vis/a010000/a011900/a011971/frames/4104x2304_16x9_30p/EPIC_00${s}${nb}.png
done
