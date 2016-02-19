# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'horizon_angle_camera.eps'

r = 6371
e=0.05  # 50mm


hp(h)=r*h/(r+h)
l(h)=r*sqrt(h*(2*r+h))/(r+h)
H(h)=hp(h)-h

#f(x)=1000*e*H(x)/l(x)
f(x)=1000*e*H(x)/l(x)

#a(h)=atan(sqrt(h*h+2*r*h)/r)
#t(h)=e*tan(a)

t(x)=-1000*e*sqrt(x*x+2*r*x)/r

set xrange [0:1000]
#set yrange [-12:12] # 24x36
set xlabel "km"
set ylabel "mm"


plot f(x),t(x)
