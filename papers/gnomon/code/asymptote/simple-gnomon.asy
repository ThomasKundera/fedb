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

draw(shift(-Z)*surface(unitcircle3),green+opacity(.6));


dot("O",O);
//linewidth(2)
triple O=(0,0,0);
triple P=(0,0,-1);

//dot("P",P);
draw(O--P,linewidth(5));

triple M=(0.8,-0.7,2.6);
draw("M",M);

triple Um=unit(O-M);

triple Mu=M+10*Um; // (see below)

// real intersect(triple P, triple Q, triple n, triple Z);
//    returns the intersection time of the extension of the line segment PQ
//    with the plane perpendicular to n and passing through Z. 
real t=intersect(M,Mu,(0,0,1),(0,0,-1));
//write(t);
// WARNING: this won't go beyond segment (see above)
triple Mp=point(M--Mu,t);
//write(Mp);

dot("M'",Mp);
draw(M--Mp,dashed);
