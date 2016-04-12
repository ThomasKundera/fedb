# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'demography.png'

p0=1000.0


totsurf(x)=12000000000.0 # ha (surface Terre)
e1=10.0  # hag (hectares globaux)
e2=1     # hag
c1=2.0
c2=5.0

ep1(x)=e1*p0
ep2(x)=e2*p0*(c2/2)**(x/30)


set xrange [0:120]
set yrange [0:30000]
set xlabel "year"
#set ylabel "mm"

plot ep1(x), ep2(x)

