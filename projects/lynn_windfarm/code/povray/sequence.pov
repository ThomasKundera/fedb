// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
#include "colors.inc"
#include "common.inc"

#declare Windmill_yellow_base= union {
  cylinder {<0,0,0>,<0,15*m,0> 2.5*m}
  cylinder {<0,14*m,0>,<0,15*m,0> 3*m}
  texture {
    pigment {color Yellow}
    finish {phong 0.2}
  }
}

#macro WhiteMastTest (height)
  sphere {
    <0,15*m,0>, height
    texture {
      pigment {color Red}
      finish {phong 0.2}
    }
  }
#end

#macro WhiteMast (height)
  cone {
    <0,15*m,0>, 2.4*m, 
    <0,height,0>, 0.5*m
    texture {
      pigment {color White}
      finish {phong 0.2}
    }
  }
#end

#macro Windmill (wangle,mast_height)
  union {
    object {Windmill_yellow_base}
    object {WhiteMast(mast_height)}
  }
#end

#macro windmill_sw37 (x_simple,z_simple,wangle)
  object {
    Windmill(wangle, 91*m)
    translate <x_simple*m, 0, z_simple*m>
  }
#end

#macro windmill_sw60 (x_simple,z_simple,wangle)
 object {
    Windmill(wangle, 102*m)
    translate <x_simple*m, 0, z_simple*m>
  }
#end


#include "windmill.pov"


light_source {
  <0, 0, 0>
  color <1,1,1>
}

camera {
  location <0, 10*m, 0> // <x, y, z>
  right     x*image_width/image_height // keep propotions regardless of aspect ratio
  look_at  <0, 0, 30*km> // <x, y, z>
  // 600 mm FF equivalent zoom
  angle 3
}