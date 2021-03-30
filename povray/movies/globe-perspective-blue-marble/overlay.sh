#!/bin/bash

# 1972
#convert  data/135918main_bm1_high.jpg -geometry 800x800 sequence1/sequence.png -geometry  -compose screen -composite out.jpg
#composite -geometry 900x900+150-50  data/135918main_bm1_high.jpg -compose screen  sequence1/sequence.png out.jpg

# 2012
composite -geometry 900x900+150-40  data/618486main_earth_full.jpg -compose screen  sequence1/sequence.png out.jpg
