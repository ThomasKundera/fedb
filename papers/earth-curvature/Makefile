# Global Makefile

all: curvature.pdf

curvature.pdf: curvature.tm Docode
	xvfb-run texmacs --convert curvature.tm curvature.pdf --quit


Docode:
	cd code && $(MAKE)
