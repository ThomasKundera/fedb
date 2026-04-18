#!/bin/bash

# Location of this script
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# Projectdir is two up
export PROJECTDIR="$( cd $SCRIPTDIR/../.. >/dev/null 2>&1 && pwd )"

export FEDBDIR="$( cd $PROJECTDIR/../.. >/dev/null 2>&1 && pwd )"

export LC_ALL=C

export PYTHONDIR=$PROJECTDIR/code/blender
export PYTHONPATH=$PYTHONPATH:$PYTHONDIR
export BLENDER_USER_SCRIPTS=$PYTHONPATH:$PYTHONDIR

export WORKDIR=$PROJECTDIR/output

mkdir -p $WORKDIR

cd $WORKDIR

echo "Working in $WORKDIR"
/usr/bin/nice -20 blender --python-use-system-env -b -P $PROJECTDIR/code/blender/iss_render.py
#  -- --gpu-backend opengl
echo "Render done"

echo "Magiking"

convert "$PROJECTDIR/output/renders/iss.png" \
  -colorspace gray -alpha remove "$PROJECTDIR/output/iss-preproc.mpc"

convert "$PROJECTDIR/output/iss-preproc.mpc" \
  -morphology Convolve DoG:1,0,1 \
  -threshold 20% \
  -morphology Dilate Disk:1 \
  -alpha set \
  -alpha copy \
  -channel a -negate +channel \
  "png32:$PROJECTDIR/output/edges0.png"

convert "$PROJECTDIR/output/edges0.png" \
    -resize 4288x2848! \
    "$PROJECTDIR/output/edges.png"

convert $PROJECTDIR/org/255-STS-s130e012141.jpg $PROJECTDIR/output/edges.png \
  -compose Over -composite \
  $PROJECTDIR/output/comparison_edges.png
echo "Done"