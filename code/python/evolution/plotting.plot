# gnuplot
set terminal png size 800,600
set output 'myplot.png'

# Set linestyle 1 to blue (#0060ad)
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5

plot "datafile.dat" using 1:2 with linespoints linestyle 1 , \
     "datafile.dat" using 1:3 