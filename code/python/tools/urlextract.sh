#!/bin/bash

cd tmpdata
grep 'A répondu' *Historique*.html | sed -e 's#><#>@<#g' | tr '@' '\n' | grep 'commentaire' | grep https | cut -d'"' -f2 | sort -u  > urlist.txt 

