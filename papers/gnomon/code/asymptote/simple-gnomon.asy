size(14cm,0);
import graph3;
import three;
import math;

limits((-2,-2,-1),(2,2,2));

xaxis3("$x$",Arrow3);
yaxis3("$y$",Arrow3);
zaxis3("$z$",Arrow3);

currentprojection=perspective(10,10,10);
currentlight=light(white,(2,2,2),(2,-2,-2));

draw(surface(unitcircle3),green+opacity(.6));


dot("O",O);
//linewidth(2)
triple O=(0,0,0);
triple S=(0,0,1);

dot("S",S);
draw(O--S,linewidth(5));

triple Vsun=(-.36,.48,-.8);
triple Ssun=S+Vsun;

draw(S-Ssun);

real t=intersect(S,Ssun,(0,0,1),(0,0,0));
write(t);
triple Sp=point(S--Vsun,t);
write(Sp);

dot("S'",Sp);
draw(S--Sp);
