#  Eukleides Makefile
all: $(patsubst %.euk,%.png,$(wildcard *.euk))


%.eps: %.euk
	eukleides $<

%.png: %.eps
	convert $< $@

