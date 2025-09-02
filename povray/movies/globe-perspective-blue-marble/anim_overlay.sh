#!/bin/bash

mkdir -p output

#for i in `seq 0 100`; do
#    echo $i
#    # Padding $1 to nnn:
#    if   [ $i -lt  10 ]; then
#      it='0'${i}
#    elif [ $i -lt 100 ]; then
#      it=${i}
#    fi
#    convert img2.png   -alpha set -background none -channel A -evaluate multiply 0.${it} +channel tmp.png
#    convert img1.png tmp.png -geometry +0+0 -compose Over -composite output/img_${it}.png
#done

#convert output/img_*.png -duplicate 1,-1-1 -delay 50 -loop 0 -strip -layers Optimize output.gif
ffmpeg -framerate 3.32 -i img_%02d.png -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 \
    -filter_complex "[0:v]reverse[r];[0:v][r]concat=n=2:v=1:a=0,scale=720:720:flags=lanczos,fps=30[v]" \
    -map "[v]" -map 1:a -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -c:a aac -b:a 128k -t 59.9 -y output.mp4