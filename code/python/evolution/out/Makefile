NICE=$(shell which nice)
POVRAY   =       $(NICE) -20 povray +I
CONVERT  =       convert
PPMTOMPEG=       $(NICE) -20 ppmtompeg
MENCODER =       $(NICE) -20 mencoder

ENCODEROPTIONS = -mf fps=12:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -oac copy

DOT_FILES = $(wildcard idvtree_*.dot)
PNG1_FILES =$(DOT_FILES:.dot=.png1)
PNG2_FILES =$(DOT_FILES:.dot=.png2)
.PRECIOUS: %.png1 %.png2

all: movie

%.png1 : %.dot
	dot -Tpng -Gsize=12,9\! -Gdpi=100 -o$@ $<

%.png2 : %.png1
	$(CONVERT) $< -gravity center -background white -extent 1200x900 $@

movie: $(PNG2_FILES)
	$(MENCODER) mf://idvtree_*.png2 $(ENCODEROPTIONS) -o output.avi

clean:
	rm *.png*

realclean:
	rm *.png* *.dot

moviedirect:
	$(MENCODER) mf://idvtree_*.png2 $(ENCODEROPTIONS) -o output.avi

