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

echo "Done"
