settings.prc=false;
settings.render = 0;
import three;
import math;
import graph3;
import fontsize;

defaultpen(fontsize(20pt));
defaultpen(Symbol(series="l",shape="n"));
defaultpen(linewidth(1.4));


size(20cm,0);
currentprojection = orthographic((6,3,5),(0,0,0),(0,1,0));
//currentprojection = perspective((6,3,5),(0,0,0),(0,1,0));

draw("$x$",project(-.5*X--X)      ,Arrow);
draw("$y$",project(-.5*Y--Y)      ,Arrow);
draw("$z$",project(-Z--(0,0,2.5)),Arrow);
dot("O",O);

triple pO=(0,0,0);

triple pP=(0,0,0);
triple pM=(1,1.1,2);
path3  plP=plane((1.7,0,0),(0,1.5,0),(-1,-1,-.5));


//dot("P",pP);
dot("M",pM);

//triple pMp=intersectionpoint(pP--pM,plP);

real t=intersect(pP,pM,(0,0,-1),(0,0,-1));

write(t);

transform3 t1=shift((-1+t)*(pM-pP));

triple pMp=t1*pM;

/*write(pM-pP);
write(t*(pM-pP));
write(t1);
write(pMp);*/


dot("M'",pMp);


draw(plP, blue);
draw(pM--pMp,dashed);


transform3 projxz=planeproject(Y);
triple pMxz=projxz*pM;
triple pMpxz=projxz*pMp;

dot("$M_{xz}$",pMxz);
dot("$M'_{xz}$",pMpxz);

draw(pMxz--pMpxz,dotted);
draw(pMp--pMpxz,dotted);
draw(pM--pMxz,dotted);



transform3 projyz=planeproject(X);
triple pMyz=projyz*pM;
triple pMpyz=projyz*pMp;
triple pMz=(0,0,pM.z);
triple pMpz=(0,0,pMp.z);


dot("$M_{yz}$",pMyz);
dot("$M'_{yz}$",pMpyz);

draw(pMyz--pMpyz,dotted);
draw(pMp--pMpyz,dotted);
draw(pM--pMyz,dotted);


dot("$M_{z}$" ,pMz);
dot("$M'_{z}$",pMpz);
draw(pMyz--pMz,dotted);
draw(pMxz--pMz,dotted);
draw(pMpyz--pMpz,dotted);
draw(pMpxz--pMpz,dotted);



