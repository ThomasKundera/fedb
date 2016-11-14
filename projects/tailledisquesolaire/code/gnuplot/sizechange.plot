# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'sizechange.eps'

pi=3.14159265358979328
degtorad=pi/180.
ns= 86400.

# Model constants

R = 10000.  # flat Earth size
h =  8000. # height of the Sun
phis=pi/2. # Above equator

# Location of observer (Strasbourg)

lambda    = 7.75*degtorad
phi       = 48.5*degtorad

#lambda=0.
#phi=pi/2.

t0     = 43200. # Time of reference

# Computation

lambdas(t)=2*pi*t/ns+pi
rs=R*phis/pi

r=R*phi/pi

dd(t)=sqrt(r*r+rs*rs-2*r*rs*cos(lambdas(t)-lambda))

d(t)=sqrt(h*h+dd(t)*dd(t))

dl(t)=d(t0)/d(t)

set xrange [0:86200]
#set yrange [-12:12]
set xlabel "seconds"
set ylabel "ratio to GMT noon"


plot 100*dl(x)

