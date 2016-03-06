#  Eukleides Makefile

sources := $(wildcard *.euk)


epsfiles = $(patsubst %.euk,%.eps, $(sources) )


all: $(epsfiles)
	echo "done"

%.eps: %.euk
	eukleides $<

