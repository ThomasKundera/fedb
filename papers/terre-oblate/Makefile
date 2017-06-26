# Global Makefile

FILEFIX=terre-oblate

all: $(FILEFIX).pdf

$(FILEFIX).pdf: $(FILEFIX).tm Docode
	xvfb-run texmacs --convert $(FILEFIX).tm $(FILEFIX).pdf --quit


Docode:
	cd code && $(MAKE)
