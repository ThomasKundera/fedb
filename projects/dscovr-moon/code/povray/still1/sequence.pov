// --------------------------------------------------------------------------------
// Finding continents as pictured on EPIC_00000.png
// --------------------------------------------------------------------------------
#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "earth-simple.inc"


global_settings { ambient_light 1.2 }

#declare mydist=1475207*km; // That exact values comes from Wikipedia
//#declare al=1.5*(180./pi)*atan2(Earth_Radius+500*km,mydist);

#declare camLoc=<0*km,0,mydist>;

camera {
  location camLoc
  look_at  <0,0,0>
  angle 0.61   // Figure from Wikipedia
  right x*image_width/image_height
}

union {
  object {Earth}
  object {frame scale 1000*km}
  // Rotations were trial and errors, may be simplified.
/*
rotate < 0,-21,  0>
  rotate <18,  0,  0>
  rotate < 0,  0,-33>
  rotate < 0,  2,   0>
  rotate <-2,  0,   0>
  rotate < 0,  0,  -2>
*/
}

//object {frame scale 1000*km}

light_source{camLoc color White} 
