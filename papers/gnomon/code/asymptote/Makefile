# Asymptote Makefile

all: simple-gnomon.eps simple-gnomon.png

%.eps: %.asy
	asy  -offscreen $< -o $@ 

%.png: %.asy
	asy  -f png -offscreen $< -o $@ 

