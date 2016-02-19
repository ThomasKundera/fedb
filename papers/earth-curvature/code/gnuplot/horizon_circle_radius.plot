# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'horizon_circle_radius.eps'

r = 6371000

hp(h)=r*h/(r+h)
l(h)=r*sqrt((h*(2*r+h)/((r+h)*(r+h))))

set xrange [0:100]
#set yrange [-0.024:0.024]
set xlabel "m"
set ylabel "km"


plot l(x)/1000


