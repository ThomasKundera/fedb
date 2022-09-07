#!/bin/bash

for imgfp in `ls ../large_processed/*.png`; do
  img=`basename $imgfp`
  echo "Processing $img"
  convert $imgfp -rotate 35.15 -crop 2000x2000+1000+100    $img
done

