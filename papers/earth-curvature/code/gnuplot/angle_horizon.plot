# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'angle_horizon.eps'

r = 6371

a(h)=atan(sqrt(h*h+2*r*h)/r)

set angles degrees
set xrange [0:100]
set yrange [0:10]
set xlabel "Height  (km)"
set ylabel "Angle  (degrees)"

plot a(x)
