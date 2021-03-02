import three;
import math;
texpreamble("\usepackage{bm}");

size(300,0);

pen thickp=linewidth(0.5mm);
real radius=1, theta=37, phi=60;

currentprojection=orthographic((4,1,2));

draw(octant1,material(palegray+opacity(0.25),shininess=0.5));

real r=1.1;
pen p=black;
draw(Label("$x$",1),O--r*X,p,Arrow3);
draw(Label("$y$",1),O--r*Y,p,Arrow3);
draw(Label("$z$",1),O--r*Z,p,Arrow3);
label("$\rm O$",(0,0,0),-1.5Y-X);

triple Q=radius*dir(theta,phi);
dot("$(x,y,z)$",Q);
draw(Q--(Q.x,Q.y,0),dashed+blue);
draw(O--radius*dir(90,phi),dashed+blue);
draw((0,0,Q.z)--Q,dashed+blue);
draw("$\theta$",arc(O,0.15*Z,0.15Q),align=2*dir(theta/2,phi),Arrow3);
draw("$\varphi$",arc(O,0.15*X,0.15*dir(90,phi)),align=5*dir(90,phi/3)+Z,Arrow3);

// Spherical octant
real r=sqrt(Q.x^2+Q.y^2);
draw(arc((0,0,Q.z),(r,0,Q.z),(0,r,Q.z)),dashed+red);
draw(arc(O,radius*Z,radius*dir(90,phi)),dashed+heavygreen);
draw(arc(O,radius*Z,radius*X),thickp);
draw(arc(O,radius*Z,radius*Y),thickp);
draw(arc(O,radius*X,radius*Y),thickp);

draw("$\bm{r}$",O--Q,align=2*dir(90,phi),Arrow3,DotMargin3);
