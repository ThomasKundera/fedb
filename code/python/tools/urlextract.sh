#!/bin/bash

cd tmpdata
grep 'A répondu' Historique\ -\ YouTube.html | sed -e 's#><#>@<#g' | tr '@' '\n' | grep 'A répondu' | cut -d'"' -f2  > urlist.txt 

