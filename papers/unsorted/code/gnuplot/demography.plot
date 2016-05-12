# gnuplot

set terminal png size 600,400

set output 'demography.png'

p0=1000.0


totsurf(x)=12000000000.0 # ha (surface Terre)
e1=10.0  # hag (hectares globaux)
e2=1     # hag
c1=2.0
c2=5.0

wasting(x)=e1*p0
reproducing(x)=e2*p0*(c2/2)**(x/30)


set xrange [0:120]
set yrange [0:30000]
set xlabel "year"
set ylabel "Ecological Footprint (hag)"

plot wasting(x), reproducing(x)

