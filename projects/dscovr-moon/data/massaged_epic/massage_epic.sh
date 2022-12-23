#!/bin/bash

for imgfp in `ls ../large_processed/*.png`; do
  img=`basename $imgfp`
  echo "Processing $img"
  convert $imgfp -rotate 25 -crop 2000x2000+1000+100    $img
done

