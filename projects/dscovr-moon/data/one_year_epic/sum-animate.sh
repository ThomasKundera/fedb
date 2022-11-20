#!/bin/bash

imglist="00000@00066 00058@00076 00087@00086 00116@00096 00145@00106 00174@00116 00203@00126 00232@00136 00261@00146 00290@00156 00319@00166 00348@00176 00377@00186 00435@00206 00464@00216 00493@00226 00522@00236 00551@00246"

i=0
for imgc in $imglist; do
  imga=`echo $imgc | cut -d'@' -f1`
  imga=EPIC_${imga}.png
  imgb=`echo $imgc | cut -d'@' -f2`
  imgb=extract${imgb}.png
  echo $imgc $imga $imgb
  is=$i
  if [ $i -lt 10 ]; then is=0${i}; fi
    
  montage $imga $imgb -tile 1x2 -geometry 455x256+1+1 tiled${is}.png
  ((i++))
done


