#!/bin/bash
JSOND_DIR="json"

mkdir -p $JSOND_DIR

for yid in `cat ytvideos.dat`; do
    echo "Working with $yid"
    fout=$JSOND_DIR/${yid}.json
    echo "for $fout"
    if ! [ -f $fout ]; then
        echo 'File does not exists, generating'
        youtube-comment-downloader -p --youtubeid $yid --output $fout
    else
        echo 'File does exist.'
    fi
done
