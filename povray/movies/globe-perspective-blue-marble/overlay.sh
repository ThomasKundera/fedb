#!/bin/bash

#convert  data/135918main_bm1_high.jpg -geometry 800x800 sequence1/sequence.png -geometry  -compose screen -composite out.jpg
composite -geometry 900x900+150-50  data/135918main_bm1_high.jpg -compose screen  sequence1/sequence.png out.jpg
