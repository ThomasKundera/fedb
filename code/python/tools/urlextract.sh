#!/bin/bash

outfile="/tmp/urlist.txt"

cd tmpdata
grep 'A répondu' *Historique*.html | sed -e 's#><#>@<#g' | tr '@' '\n' |\
grep 'commentaire' | tr ' ' '\n' | grep https | grep 'commentaire' |\
cut -d'"' -f2 | sort -u  > $outfile

grep 'ytd-notification-renderer' Historique*.html | grep href |\
tr ' ' '\n' | grep href | cut -d'"' -f2 | grep 'lc=' | rev |\
cut -d '.' -f2- | rev | grep 'lc=' >> $outfile

FFBD=~/.mozilla/firefox

for fdir in $FFBD; do
  echo "For fdir=$fdir"
  pdirs=`find $fdir -maxdepth 1 -type d`
  for pdir in $pdirs; do
    echo "For pdir=$pdir in fdir=$fdir"
    cp $pdir/places.sqlite mytmp.sqlite
    sqlite3 mytmp.sqlite .dump | grep youtube | grep watch | cut -d "'" -f2 |\
    grep https | sort -u | grep 'lc=' | rev |\
    cut -d '.' -f2- | rev | sort -u | grep 'lc=' >> $outfile
  done
done

echo "WARNING: output is in $OUTFILE"

