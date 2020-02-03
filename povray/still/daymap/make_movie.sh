#!/bin/bash

for i in `seq 1 6`; do
  echo $i
  montage -mode concatenate -tile 2x mapped/sequence${i}.png lighted/sequence${i}.png out/out${i}.png
done

convert -delay 50 -loop 1  out/out*.png output.gif
