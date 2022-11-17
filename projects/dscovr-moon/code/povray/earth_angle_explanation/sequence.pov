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

#declare camLoc=<0*km,0,mydist>;

camera {
  location camLoc
  look_at  <0,0,0>
  angle 0.61   // Figure from Wikipedia
  right x*image_width/image_height
}


union {
  object {Earth}
  object {simpleframe scale 7000*km} // Faster to render
}

//object {frame scale 1000*km}

light_source{camLoc color White} 
