#!/bin/bash
JSOND_DIR="json"

mkdir -p $JSOND_DIR

for yid in `cat ytvideos.dat`; do
    echo
    echo "Working with $yid"
    fout=$JSOND_DIR/${yid}.json
    echo "for $fout"
    if ! [ -f $fout ]; then
        echo 'File does not exists, generating'
        youtube-comment-downloader -p --youtubeid $yid --output $fout
        sleep 10
    else
        #echo 'File does exist.'
        now=`date +%s`
        epm=`stat -c "%W" $fout`
        deltat=`echo "$now - $epm" | bc`
        #echo $now $epm $deltat
        if [ $deltat -gt 36000 ]; then
            echo "Updating file ( $deltat )"
        else
            echo "File is recent enough"
            youtube-comment-downloader -p --youtubeid $yid --output $fout
            sleep 10
        fi
    fi
done
