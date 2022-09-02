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

#declare dateH=19;
#declare dateM=50;
#declare dateS=0;

// Time is UTC, so noon at 12:00 over Greenwitch.
#declare TimeOfTheDay=360*(-(dateH*3600+dateM*60+dateS)-6*3600)/86400;

#declare mydist=1475207*km; // That exact values comes from Wikipedia

#declare camLoc=<0*km,0,mydist>;

#declare declinaison_angle=23.43643; // Value from Wikipedia  23° 26' 11,150" 


camera {
  location camLoc
  look_at  <0,0,0>
  angle 0.61   // Figure from Wikipedia
  right x*image_width/image_height
}


#declare simpleframe=union {
    #local l=1.1*Earth_Radius/(1000*km);
    cylinder {<l,0,0>,<-l,  0,  0> .1 texture {XaxisTexture}}
    cylinder {<0,l,0>,<  0,-l,  0> .1 texture {YaxisTexture}}
    cylinder {<0,0,l>,<  0,  0,-l> .1 texture {ZaxisTexture}}
}

union {
  object {Earth}
  object {simpleframe scale 1000*km} // Faster to render
  /* // This is slowing render by an order of magnitude
  intersection { // The lines are too big and clouding the picture
    object {frame scale 1000*km}
    sphere {<0,0,0> Earth_Radius+1000*km}
  }
  */
  // Time of the day
  rotate < 0,TimeOfTheDay, 0>
  
  // Winter solstice reference
  //rotate < -declinaison_angle,0, 0>

}

//object {frame scale 1000*km}

light_source{camLoc color White} 
