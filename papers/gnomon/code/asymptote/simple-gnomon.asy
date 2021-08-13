size(14cm,0);

import graph3;

limits((-2,-2,-1),(2,2,2));

xaxis3("$x$",Arrow3);
yaxis3("$y$",Arrow3);
zaxis3("$z$",Arrow3);

currentprojection=perspective(10,10,10);
currentlight=light(white,(2,2,2),(2,-2,-2));

draw(surface(unitcircle3),green+opacity(.6));


dot("O",O);
//linewidth(2)
draw((0,0)--(1,1));
