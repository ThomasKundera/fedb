#!/bin/bash

cd sequence1
make
cd ..
cp out.jpg out-old.jpg
./overlay.sh
