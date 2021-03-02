# Global Makefile

FILEFIX=night-time

all: $(FILEFIX).pdf

$(FILEFIX).pdf: $(FILEFIX).tm docode
	xvfb-run texmacs --convert $(FILEFIX).tm $(FILEFIX).pdf --quit


docode:
	cd code && $(MAKE)
