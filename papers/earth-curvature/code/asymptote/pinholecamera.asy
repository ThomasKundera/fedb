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

triple pP=(0,.8,0);
triple pM=(3,2,4);
path3  plP=plane((2,0,0),(0,2,0),(0,0,1));


dot("P",pP);
dot("M",pM);

//triple pMp=intersectionpoint(pP--pM,plP);

real t=intersect(pP,pM,(0,0,1),(0,0,1));

triple pMp=point(pP--pM,t);
dot("M'",pMp);

draw(plP, blue);
draw(pP--pM,dashed);

transform3 projxy=planeproject(Y);
triple pMxy=projxy*pM;
triple pMpxy=projxy*pMp;

dot("$M_{xz}$",pMxy);
dot("$M'_{xz}$",pMpxy);

draw(pMxy--pO,dotted);
draw(pMp--pMpxy,dotted);
draw(pM--pMxy,dotted);


transform3 projyz=planeproject(X);
triple pMyz=projyz*pM;
triple pMpyz=projyz*pMp;

dot("$M_{yz}$",pMyz);
dot("$M'_{yz}$",pMpyz);

draw(pMyz--pP,dotted);
draw(pMp--pMpyz,dotted);
draw(pM--pMyz,dotted);
