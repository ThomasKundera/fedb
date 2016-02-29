settings.prc=false;
settings.render = 0;
import three;
import math;
import graph3;
size(10cm,0);
currentprojection = orthographic((6,3,5),(0,0,0),(0,1,0));
//currentprojection = perspective((6,3,5),(0,0,0),(0,1,0));

draw("$x$",project(O--X),Arrow);
draw("$y$",project(O--Y),Arrow);
draw("$z$",project(O--(0,0,4)),Arrow);
dot("O",O);

triple pO=(0,0,0);

triple pP=(0,.6,.8);
triple pM=(2.5,2.2,4);
path3  plP=plane((2,0,0),(0,1,0),(-1,0,0));


dot("P",pP);
dot("M",pM);

//triple pMp=intersectionpoint(pP--pM,plP);

//real intersect(triple P, triple Q, triple n, triple Z);
//    returns the intersection time of the extension of 
//    the line segment PQ with the plane perpendicular
//    to n and passing through Z.

triple V=pP-pM;
//write(V);
//triple pPp=pM+10*V;

//write(pPp);

real t=intersect(pM,pP,(0,0,1),(0,0,0));

//write(t);

triple pMp=pM+t*V;

//write(pMp);

dot("M'",pMp);

draw(plP, blue);
draw(pM--pMp,dashed);

transform3 projxz=planeproject(Y);
triple pMxy=projxz*pM;
triple pMpxy=projxz*pMp;
// 
dot("$M_{xz}$",pMxy);
dot("$M'_{xz}$",pMpxy);
// 
draw(pMxy--pMpxy,dotted);
draw(pMp--pMpxy,dotted);
draw(pM--pMxy,dotted);


transform3 projyz=planeproject(X);
triple pMyz=projyz*pM;
triple pMpyz=projyz*pMp;

dot("$M_{yz}$",pMyz);
dot("$M'_{yz}$",pMpyz);

draw(pMyz--pMpyz,dotted);
draw(pMp--pMpyz,dotted);
draw(pM--pMyz,dotted);


//transform3 projxy=planeproject(Z);
//triple pMy=projxz*pMyz;
//dot("$M_{z}$",pMy);



