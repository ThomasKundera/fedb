// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// squared-stuff.inc


#include "horizon-scene.inc"

#declare dv=sin(45)*sin(45)*hd;
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



text {
    ttf "timrom.ttf" "A" thick, 0
    pigment { Green }
    scale 30*m
    rotate <0,-90,0>
    translate <dv,(sin(thetav)-1)*sphere_radius,0*m>
}

text {
    ttf "timrom.ttf" "C" thick, 0
    pigment { Green }
    scale 30*m
    rotate <0,-90,0>
    translate <dv,(sin(thetav)-1)*sphere_radius,0*m>
    rotate <0,2*45,0>
}

text {
    ttf "timrom.ttf" "E" thick, 0
    pigment { Green }
    scale 30*m
    rotate <0,-90,0>
    translate <dv,(sin(thetav)-1)*sphere_radius,0*m>
    rotate <0,4*45,0>
}

text {
    ttf "timrom.ttf" "G" thick, 0
    pigment { Green }
    scale 30*m
    rotate <0,-90,0>
    translate <dv,(sin(thetav)-1)*sphere_radius,0*m>
    rotate <0,6*45,0>
}


