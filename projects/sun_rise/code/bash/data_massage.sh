#!/bin/bash

kBATCH="2025_08_22"

DATADIR="../../data/$kBATCH"

cd $DATADIR

ls -l

rm -rf 500_sun
mkdir 500_sun

for imgf in full_sun/*.JPG; do 
    img=`basename $imgf`
    echo "For: $img"
    convert full_sun/$img -resize 500x500 500_sun/$img
done
