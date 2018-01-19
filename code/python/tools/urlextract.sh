#!/bin/bash

cd tmpdata
grep 'A répondu' *Historique*.html | sed -e 's#><#>@<#g' | tr '@' '\n' |\
grep 'commentaire' | tr ' ' '\n' | grep https | grep 'commentaire' |\
cut -d'"' -f2 | sort -u  > urlist.txt 

grep 'ytd-notification-renderer' Historique*.html | grep href |\
tr ' ' '\n' | grep href | cut -d'"' -f2 | grep 'lc=' | rev |\
cut -d '.' -f2- | rev | grep 'lc=' >> urlist.txt
