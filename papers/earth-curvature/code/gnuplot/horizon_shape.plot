# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'horizon_shape.eps'

r = 6371000
e=0.05  # 50mm


hp(h)=r*h/(r+h)
l(h)=r*sqrt((h*(2*r+h)/((r+h)*(r+h))))
H(h)=hp(h)+h

f0(x,h)=-1000*H(h)*sqrt(e*e+x*x)/l(h)
f(x,h)=f0(x/1000,h)

set xrange [-18:18] # 24x36
set yrange [-12:12]
set xlabel "mm"
set ylabel "mm"


plot f(x,1), f(x,1000), f(x,10000), f(x,30000),f(x,100000)

