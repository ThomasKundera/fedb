# Asymptote Makefile

all: simple-gnomon.eps
#half-light-sphere.png

%.eps: %.asy
	asy  -offscreen $< -o $@ 

%.png: %.asy
	asy  -f png -offscreen $< -o $@ 

