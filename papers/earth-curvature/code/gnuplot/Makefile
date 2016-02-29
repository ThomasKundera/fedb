# Gnuplot Makefile

all: distances.eps angle_horizon.eps horizon_shape.eps\
     horizon_circle_radius.eps horizon_angle_camera.eps\
     eight_inches.eps eight_inches_small.eps

%.eps: %.plot
	gnuplot $<

