# Asymptote Makefile

all: simple-sphere.eps
#half-light-sphere.png

%.eps: %.asy
	asy  -offscreen $< -o $@ 

%.png: %.asy
	asy  -f png -offscreen $< -o $@ 

