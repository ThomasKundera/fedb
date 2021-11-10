###################################################################################
#
# Makefile for povray stuff
# 
###################################################################################

NICE=$(shell which nice)
POVRAY   =       $(NICE) -10 povray +I
CONVERT  =       convert
PPMTOMPEG=       $(NICE) -10 ppmtompeg
MENCODER =       $(NICE) -10 mencoder

ENCODEROPTIONS = -mf fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -oac copy

DIREPS  =       .

IMG_FILE =       sequence.png

SYMLINKEDFILES = common.inc frame.inc earth-simple.inc sun-simple.inc spline.inc


all: povray.ini $(SYMLINKEDFILES) $(IMG_FILE)
	@echo "made it!"

install:
	mv *.eps $(DIREPS)/


hq:	prephq all

prephq:
	ln -fs povray_hq.ini povray.ini

#png:  $(IMG_FILE) 

.SUFFIXES : .eps .png .pov

.pov.png:
	@echo "povray create  $<"
	$(POVRAY)$<  povray.ini

movie:
	$(MENCODER) mf://sequence*.png $(ENCODEROPTIONS) -o output.avi
clean:  
	@/bin/rm *.png

COMMON   = ../../common


%.inc: $(COMMON)/%.inc
	ln -s $<
	
%.mcr: $(COMMON)/%.mcr
	ln -s $<
