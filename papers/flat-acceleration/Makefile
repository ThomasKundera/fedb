# Global Makefile

FILEFIX=flat-acceleration

all: $(FILEFIX).pdf

$(FILEFIX).pdf: $(FILEFIX).tm
	xvfb-run texmacs --convert $(FILEFIX).tm $(FILEFIX).pdf --quit


#Docode:
#	cd code && $(MAKE)
