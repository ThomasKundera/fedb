###################################################################################
#
# Makefile for povray stuff
# 
###################################################################################

NICE=$(shell which nice)
PPMTOMPEG=       $(NICE) -20 ppmtompeg
MENCODER =       $(NICE) -20 mencoder

ENCODEROPTIONS = -mf fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -oac copy

movie:
	$(NICE) $(MENCODER) mf://../sequence1/sequence*.png mf://../sequence2/sequence*.png mf://../sequence3/sequence*.png $(ENCODEROPTIONS) -o output.avi
clean:  
	@/bin/rm *.png
