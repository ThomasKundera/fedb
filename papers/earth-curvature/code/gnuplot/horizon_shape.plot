# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'horizon_shape.eps'

r = 6371000
e=0.05  # 50mm


hp(h)=r*h/(r+h)
l(h)=r*sqrt((h*(2*r+h)/((r+h)*(r+h))))
H(h)=hp(h)-h

f(x,h)=-sqrt(e*2*H(h)*H(h)+H(h)*H(h)*x*x)/l(h)

set xrange [-0.18:0.18] # 24x36
#set yrange [-0.024:0.024]
set xlabel "m"
set ylabel "m"


plot f(x,0), f(x,100), f(x,1000), f(x,10000), f(x,20000), f(x,30000), f(x,50000), f(x,100000), f(x,500000)

