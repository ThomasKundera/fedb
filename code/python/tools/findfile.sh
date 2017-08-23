#!/bin/bash

FRAG=z235j1f54qyzgvqqt04t1aokgvzcwaai1mhnoxqv1axsbk0h00410""

FN=`ls tmpdata/html/*${FRAG}* | cut -d '/' -f3`
echo $FN
exit 0

cd tmpdata/html

tidy -config ../tidy.conf $FN > toto1.html
cd ../html-old2
tidy -config ../tidy.conf $FN > toto2.html


cd ..

diff html/toto1.html html-old2/toto2.html > stuff.html

echo $FN

