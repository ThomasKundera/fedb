#!/bin/bash

ENCODEROPTIONS="-mf fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=8000 -oac copy"
MENCODER="/bin/nice -20 mencoder"
${MENCODER} mf://sequence*.png ${ENCODEROPTIONS} -o output.avi