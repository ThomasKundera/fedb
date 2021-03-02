# Global Makefile

FILEFIX=day-night

all: $(FILEFIX).pdf docode

$(FILEFIX).pdf: $(FILEFIX).tm docode
	xvfb-run texmacs --convert $(FILEFIX).tm $(FILEFIX).pdf --quit


docode:
	cd code && $(MAKE)
