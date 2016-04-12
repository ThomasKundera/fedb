# Gnuplot Makefile

sources := $(wildcard *.plot)


pngfiles = $(patsubst %.plot,%.png, $(sources) )


all: $(pngfiles)
	echo "done"


%.png: %.plot
	gnuplot $<

