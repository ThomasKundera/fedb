# Global Makefile

all: tds.pdf

tds.pdf: tds.tm Docode
	xvfb-run texmacs --convert tds.tm tds.pdf --quit


Docode:
	cd code && $(MAKE)

