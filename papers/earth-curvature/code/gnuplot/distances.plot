# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'distance.eps'

r = 6371

k(x,ha)=x-sqrt(ha*ha+2*r*ha)

d(x,ha)=4*r*r+4*k(x,ha)*k(x,ha)

#(x) = sqrt(2*r*x+x*x)+sqrt(2*r*hb+hb*hb)

h(x,ha)=1000*(-2*r+sqrt(d(x,ha/1000.)))/2

set xrange [0:250]
set yrange [0:1500]
set xlabel "Distance (km)"
set ylabel "Height (m)"

plot h(x,0), h(x,10), h(x,100), h(x,250), h(x,500), h(x,1000)

