#!/bin/bash
JSOND_DIR="json"

mkdir -p $JSOND_DIR

for yid in `cat ytvideo.dat`; do
    echo "Working with $yid"
    fout=$JSOND_DIR/${yid}.json
    echo "for $fout"
done
