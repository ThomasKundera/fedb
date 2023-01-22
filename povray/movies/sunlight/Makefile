###################################################################################
#
# Makefile for povray stuff
# 
###################################################################################

NICE=$(shell which nice)
POVRAY   =       $(NICE) -20 povray +I
CONVERT  =       convert
PPMTOMPEG=       $(NICE) -20 ppmtompeg
MENCODER =       $(NICE) -20 mencoder

ENCODEROPTIONS = -mf fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -oac copy

IMG_FILE =       sequence.png

COMMONPATH = ../../common/

COMMONFILES = $(COMMONPATH)/common.inc $(COMMONPATH)/frame.inc $(COMMONPATH)/earth-simple.inc

all: povray.ini $(COMMONFILES) $(IMG_FILE)
	@echo "made it!"

install:
	mv *.eps $(DIREPS)/

hq:	prephq all

lq:	preplq all

hqanim:	prephqanim all

lqanim:	preplqanim all

prephq:
	ln -fs povray_hq.ini povray.ini

preplq:
	ln -fs povray_lq.ini povray.ini

prephqanim:
	ln -fs povray_hq_anim.ini povray.ini

preplqanim:
	ln -fs povray_lq_anim.ini povray.ini

.SUFFIXES : .eps .png .pov

.pov.png: $(COMMONFILES) povray_hq.ini povray.ini
	@echo "povray create  $<"
	$(POVRAY)$<  povray.ini

movie:
	$(MENCODER) mf://data/out4/sequence*.png $(ENCODEROPTIONS) -o output.avi
clean:  
	@/bin/rm *.png
	
