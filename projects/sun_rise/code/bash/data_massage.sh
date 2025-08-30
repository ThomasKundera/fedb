#!/bin/bash

kBATCH="2025_08_22"
kSIZE=1250

DATADIR="../../data/$kBATCH"

cd $DATADIR

ls -l

rm -rf ${kSIZE}_sun
mkdir ${kSIZE}_sun

for imgf in full_sun/*.JPG; do 
    img=`basename $imgf`
    echo "For: $img"
    convert full_sun/$img -resize ${kSIZE}x${kSIZE} ${kSIZE}_sun/$img
done

