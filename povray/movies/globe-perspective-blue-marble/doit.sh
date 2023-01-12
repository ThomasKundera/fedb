#!/bin/bash

cd sequence1
make hq
cd ..
cp out.jpg out-old.jpg
./overlay.sh
