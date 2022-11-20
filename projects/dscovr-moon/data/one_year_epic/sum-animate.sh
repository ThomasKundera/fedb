#!/bin/bash

for img in `ls ../large_processed/*.png`; do
  imgo=`basename $img`
  convert $img  -background "#000000" -resize "1920x1080" -rotate 26.2 -crop "1920x1080+10+4" -resize "1925x1085!" -crop "1920x1080+8+6" $imgo
done


