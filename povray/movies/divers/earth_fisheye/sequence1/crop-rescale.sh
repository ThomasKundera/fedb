#!/bin/bash

#480 1179 349
convert -crop 699x349+480x0  -resize 825x425 from_iss.png  \
        -background Khaki label:'Altitude 320km Fisheye Lens FOV 170°' \
        -gravity Center -append from_iss-crop.png
convert -crop 1600x812+25x0 -resize 825x425 whole_earth.png \
        -background Khaki label:'Altitude 5000km regular Lens FOV 95°' \
        -gravity Center -append -background YellowGreen label:'Both images use the same standard 6371km radius globe Earth' \
        -gravity Center -append whole_earth-crop.png

montage from_iss-crop.png whole_earth-crop.png  -geometry +1+1 -tile 1x2 \
        final.png


