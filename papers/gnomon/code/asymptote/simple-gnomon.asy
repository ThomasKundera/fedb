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


transform3 projxy=planeproject(Z);
triple Mxy=projxy*M;
triple Mpxy=projxy*Mp;

dot("$M_{xy}$" ,Mxy);
dot("$M'_{xy}$",Mpxy);

draw(Mxy--Mpxy,dotted);
draw(Mp--Mpxy,dotted);
draw(M--Mxy,dotted);


transform3 projyz=planeproject(X);
triple Myz=projyz*M;
triple Mpyz=projyz*Mp;

dot("$M_{yz}$" ,Myz);
dot("$M'_{yz}$",Mpyz);

draw(Myz--Mpyz,dotted);
draw(Mp--Mpyz,dotted);
draw(M--Myz,dotted);

triple My=(0,ypart(M),0);
dot("$M_{y}$" ,My);
draw(Myz--My,dotted);

triple Mpy=(0,ypart(Mp),0);
dot("$M'_{y}$" ,Mpy);
draw(Mpyz--Mpy,dotted);
