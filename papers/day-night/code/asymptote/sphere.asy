import solids;
//settings.render=0; 
//settings.prc=false; // on se restreint à une vue 2d

size(7.5cm,0);

currentprojection=orthographic(10,5,2);

dotfactor=3.5;

real a=3;
triple pO=(0,0,0);
revolution b=sphere(pO,a);

draw(surface(b),.9white+opacity(.15));

skeleton s;
b.transverse(s,reltime(b.g,0.5),P=currentprojection);
draw(s.transverse.back,green+linetype("8 8",8));
draw(s.transverse.front,blue);
dot(pO);

dot(new triple[] {a*X,a*Y,a*Z,O}); 
draw(Label("$x$",align=N),O--a*X,red); 
draw(Label("$y$",align=N),O--a*Y,red); 
draw(Label("$z$",align=E),O--a*Z,red); 

draw(b.silhouette(),blue);

real a=.7; //compris entre 0 et 1
real b=6;
draw(surface(shift(-b/2,-b/2,sin(pi*(a-.5)))*scale3(b)*unitsquare3),white+opacity(.7));

