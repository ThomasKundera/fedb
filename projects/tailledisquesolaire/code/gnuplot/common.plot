# gnuplot

pi=3.14159265358979328
degtorad=pi/180.
ns= 24.

# Model constants

R = 20000.  # flat Earth size
h =  8000. # height of the Sun
phis=pi/2. # Above equator

# Location of observer (Strasbourg)

lambda    = 7.75*degtorad
phi       = 48.5*degtorad

#lambda=0.
#phi=pi/2.

t0     = 12. # Time of reference

# Computation

lambdas(t)=2*pi*t/ns+pi
rs=R*phis/pi

r=R*phi/pi

dd(t)=sqrt(r*r+rs*rs-2*r*rs*cos(lambdas(t)-lambda))

d(t)=sqrt(h*h+dd(t)*dd(t))

dl(t)=d(t0)/d(t)

a(t)=atan(h/d(t))
