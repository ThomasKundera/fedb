# Global Makefile

FILEFIX=gnomon

all: $(FILEFIX).pdf

$(FILEFIX).pdf: $(FILEFIX).tm docode
	xvfb-run texmacs --convert $(FILEFIX).tm $(FILEFIX).pdf --quit


docode:
	cd code && $(MAKE)
