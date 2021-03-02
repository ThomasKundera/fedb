size(12cm,0);
import solids;

currentlight=Headlamp; // inutile car Headlamp est la valeur par défaut

nslice=4*nslice;
revolution boule=sphere(O,1);
draw(surface(boule),lightgrey+white+opacity(.5));

skeleton s;

for(real i=.5; i<1; i+=.1){
boule.transverse(s,reltime(boule.g,i),P=currentprojection);
draw(s.transverse.back,linetype("10 10",10));
draw(s.transverse.front);
}