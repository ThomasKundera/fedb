# gnuplot

set terminal postscript eps size 10,6 enhanced color font 'Helvetica,20' linewidth 2
set output 'eight_inches.eps'

set key left top

r = 6371

h0(x)=0.0254*8*(x/1609.34)**2
h(x)=h0(x*1000)/1000
hp(x)=sqrt(r*r+x*x)-r

hpp(x)=sqrt(x*x*hp(x)*hp(x)/(r*r)+hp(x)*hp(x))

dlp(x)=r*tan(x/r)


set xrange [0:6371]
set yrange [0:6371]
set xlabel "km"
set ylabel "km"


plot h(x)        title "h(d)"  , \
     hp(x)       title "h'(d)" , \
     hpp(x)      title "h''(d)", \
     h(dlp(x))   title "h(l)"  , \
     hp(dlp(x))  title "h'(l)" , \
     hpp(dlp(x)) title "h''(l)"
     
