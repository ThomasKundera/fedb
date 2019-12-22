#!/bin/bash

#480 1179 349
convert -crop 699x349+480x0  -resize 825x425 from_iss.png    from_iss-crop.png
convert -crop 1600x812+25x0 -resize 825x425 whole_earth.png whole_earth-crop.png

montage from_iss-crop.png whole_earth-crop.png  -geometry +1+1 -tile 1x2 final.png


