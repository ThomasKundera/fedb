#  Eukleides Makefile
all: $(patsubst %.euk,%.eps,$(wildcard *.euk))


%.eps: %.euk
	eukleides $<

%.png: %.eps
	convert $< $@

