// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
#include "colors.inc"
#include "common.inc"

#declare DoFlatEarth=false;

#declare earthType=0;
#if (DoFlatEarth)
#include "flat-earth-simple.inc"
#else
#include "earth-simple.inc"
#end

#declare Windmill_yellow_base= union {
  cylinder {<0,0,0>,<0,15*m,0> 2.5*m}
  cylinder {<0,14*m,0>,<0,15*m,0> 3*m}
  texture {
    pigment {color Yellow}
    finish {phong 0.2}
  }
}

#declare Blade=union {
  cone {
    <0,0,0>, .3,
    <0,20,0>, 2.5
  }
  cone {
    <0,20,0>, 2.5,
    <0,50,0>, .2
  }
  scale <1,1,.2>
  texture {
    pigment {color White}
    finish {phong 0.2}
  }
}

#declare ThreeBlades=union {
  object {Blade}
  object {Blade rotate <0,0,120>}
  object {Blade rotate <0,0,240>}
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

#macro Windmill (wangle,mast_height, blade_length)
  union {
    object {Windmill_yellow_base}
    object {WhiteMast(mast_height)}
    object {
      ThreeBlades
      rotate <0,0,-90-wangle>
      scale blade_length/50
      translate <0,mast_height,-2*m>
    }
  }
#end

#macro on_earth_translate (x_simple,z_simple)
  translate <x_simple*m, 0, z_simple*m>
#end

#macro windmill_sw37 (x_simple,z_simple,wangle)
  object {
    Windmill(wangle, 91*m, 107*m/2)
    on_earth_translate (x_simple,z_simple)
  }
#end

#macro windmill_sw60 (x_simple,z_simple,wangle)
 object {
    Windmill(wangle, 102*m, 154*m/2)
    on_earth_translate (x_simple,z_simple)
  }
#end


#include "windmill.pov"

object {
  Earth
  translate <0,-Earth_Radius,0>
}


light_source {
  <0, 0, 0>
  color <1,1,1>
}

camera {
  location <0, 10*m, 0> // <x, y, z>
  right     x*image_width/image_height // keep propotions regardless of aspect ratio
  look_at  <0, 10*m, 30*km> // <x, y, z>
  // 600 mm FF equivalent zoom
  angle 4
}