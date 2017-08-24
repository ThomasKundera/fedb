#!/bin/bash

FRAG=$1

FN=`ls tmpdata/html/*${FRAG}* | cut -d '/' -f3`
echo $FN
echo tmpdata/html/$FN
echo tmpdata/html-old2/$FN
echo file://`pwd`/tmpdata/html/$FN
echo file://`pwd`/tmpdata/html-old2/$FN

exit 0

cd tmpdata/html

tidy -config ../tidy.conf $FN > toto1.html
cd ../html-old2
tidy -config ../tidy.conf $FN > toto2.html


cd ..

diff html/toto1.html html-old2/toto2.html > stuff.html

echo $FN

