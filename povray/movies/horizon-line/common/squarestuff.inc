// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// squared-stuff.inc


#include "horizon-scene.inc"

#declare dv=hd/sqrt(2);
#declare thetav=acos(dv/sphere_radius);


torus {
  sphere_radius*sin(thetav),10*cm*torusMag
  rotate <90,0,0>
  translate <0,-sphere_radius,-dv>
  pigment {color Green}
}
torus {
  sphere_radius*sin(thetav),10*cm*torusMag
  rotate <90,0,0>
  translate <0,-sphere_radius,dv>
  pigment {color Green}
}
torus {
  sphere_radius*sin(thetav),10*cm*torusMag
  rotate <0,0,90>
  translate <-dv,-sphere_radius,0>
  pigment {color Green}
}
torus {
  sphere_radius*sin(thetav),10*cm*torusMag
  rotate <0,0,90>
  translate <dv,-sphere_radius,0>
  pigment {color Green}
}


#for (i,0,3)
  #declare i2=2*i;
  #declare L=Letters[i2];
  #declare myL=text {
      ttf "timrom.ttf" L thick, 0
  };
  #declare Lc=yCenter(myL);
  #declare Lc=<Lc.x,0,Lc.z>;
  object {myL
      translate -Lc/2
      pigment { Green }
      scale 30*m
      rotate <0,-90,0>
      translate <dv,(sin(thetav)-1)*sphere_radius,0*m>
      rotate <0,45*i2,0>
  }
#end

