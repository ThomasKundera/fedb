# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'sizechange.eps'

load "common.plot"

set xrange [0:24]
#set yrange [-12:12]
set xlabel "hours"
set ylabel "ratio to GMT noon"


plot 100*dl(x)

