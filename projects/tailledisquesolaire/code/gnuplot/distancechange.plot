# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'distancechange.eps'

load "common.plot"

set xrange [0:24]
#set yrange [-12:12]
set xlabel "hours"
set ylabel "distance to Sun (km)"


plot d(x)

