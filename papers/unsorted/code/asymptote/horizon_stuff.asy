import three;
import math;
import graph3;

import solids;


size(10cm,0);

currentprojection = orthographic((6,3,5),(0,0,0),(0,1,0));

scale(Linear,Linear,Linear);

xaxis3("$x$",0,1,red,OutTicks(2,2));
yaxis3("$y$",0,1,red,OutTicks(2,2));
zaxis3("$z$",0,1,red,OutTicks(2,2));

real r=3;


revolution b=sphere(O,r);
draw(surface(b), paleblue+opacity(0.5));


real h=1;

triple P=(0,r+h,0);

dot("P",P);

real hp=r*h/(r+h);

real l=r*sqrt(h*(2*r+h))/(r+h);

triple c1=( l,r-hp, 0);
triple c2=( 0,r-hp, l);
triple c3=(-l,r-hp, 0);
triple c4=( 0,r-hp,-l);

path3 horizon=c1..c2..c3..c4..cycle;
draw(horizon);
