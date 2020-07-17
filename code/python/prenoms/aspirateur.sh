#!/bin/bash 
URLBASE="https://www.sujetdebac.fr"
URLACLIST="${URLBASE}/resultats-bac/"

DATADIR="data"
BASEFILE="$DATADIR/base.html"

wget --user-agent="$USER_AGENT" --no-check-certificate -O $BASEFILE $URLACLIST

ACALIST="data/accalisty.txt"

grep "liste-liens" $BASEFILE | tr ' =' '\n' | grep result | tr -d '"' > $ACALIST

for urlpart in `cat $ACALIST`; do
  acpart=${URLBASE}$urlpart
  acpartdsk=`echo $urlpart | tr -d '/'`
  acpartdsk=${acpartdsk}.html
  echo $acpart $acpartdsk
  
  ls $DATADIR/$acpartdsk >& /dev/null
  if [ $? -ne 0 ]; then
    wget --user-agent="$USER_AGENT" --no-check-certificate -O $DATADIR/$acpartdsk $acpart
  fi
  
  acfillist=$DATADIR/${acpartdsk}-list.txt
  grep "liste-liens" $DATADIR/$acpartdsk | tr ' =' '\n' | grep result | tr -d '"' > $acfillist
  
  
  for urlpart in `cat $acfillist`; do
    acpart=${URLBASE}$urlpart
    acpartdsk=`echo $urlpart | tr -d '/'`
    acpartdsk=${acpartdsk}.html
    echo $acpart $acpartdsk
    
    ls $DATADIR/$acpartdsk >& /dev/null
    if [ $? -ne 0 ]; then
      wget --user-agent="$USER_AGENT" --no-check-certificate -O $DATADIR/$acpartdsk $acpart
    fi
    
    acfillletterlist=$DATADIR/${acpartdsk}-list.txt
    grep "lettre-lien" $DATADIR/$acpartdsk | tr ' =' '\n' | grep resultats | tr -d '"' > $acfillletterlist
 
 
    for urlpart in `cat $acfillletterlist`; do
      acpart=${URLBASE}$urlpart
      acpartdsk=`echo $urlpart | tr -d '/'`
      acpartdsk=${acpartdsk}.html
      echo $acpart $acpartdsk
      
      ls $DATADIR/$acpartdsk >& /dev/null
      if [ $? -ne 0 ]; then
        wget --user-agent="$USER_AGENT" --no-check-certificate -O $DATADIR/$acpartdsk $acpart
        sleep 5
      fi
      
      grep "Voir les" $DATADIR/$acpartdsk | grep -v 'Perles du' | cut -d'>' -f3 | cut -d'<' -f1 > $DATADIR/res-${acpartdsk}.txt
    done
  done
done
