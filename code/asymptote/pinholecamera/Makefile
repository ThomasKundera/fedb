# Asymptote Makefile
sources := $(wildcard *.asy)

epsfiles = $(patsubst %.asy,%.eps, $(sources) )

all: $(epsfiles)
	echo "done"

%.eps: %.asy
	asy -f png -offscreen $<

