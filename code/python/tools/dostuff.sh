#!/bin/bash

cd tmpdata
grep '<a' Historique\ -\ YouTube.html | grep 'www.youtube.com/watch' | sed -e 's#><#>@<#g' \
| tr '@' '\n' | grep 'www.youtube.com/watch' | grep 'yt-uix-sessionlink' | tr ' ' '\n' \
| grep 'www.youtube.com/watch' | grep ';elc=1' | cut -d'"' -f2 > urlist.txt

