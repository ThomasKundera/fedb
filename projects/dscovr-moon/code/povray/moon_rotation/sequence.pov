// --------------------------------------------------------------------------------
// Finding continents as pictured on EPIC_00000.png
// --------------------------------------------------------------------------------
#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "earth-simple.inc"
#declare moonType=1;
#include "moon-simple.inc"

global_settings { ambient_light 1.2 }

#declare dateH=19;
#declare dateM=50;
#declare dateS=0;

// Time is UTC, so noon at 12:00 over Greenwitch.
#declare TimeOfTheDay=360*(-(dateH*3600+dateM*60+dateS)-6*3600)/86400;

// Computing dates is too complex in Povray see auxiliary program "YearFraction.py"
// that spits this answer.
#declare YearFraction=-0.4336122195831841;
//#declare YearFraction=-.5;

#declare mydist=1475207*km; // That exact values comes from Wikipedia

#declare camLoc=<0*km,0,mydist>;

#declare declinaison_angle=23.43643; // Value from Wikipedia  23° 26' 11,150" 


camera {
  location camLoc
  look_at  <0,0,0>
  angle 0.61   // Figure from Wikipedia
  angle 0.2 // Moon full scale
  right x*image_width/image_height
  //rotate <0,0,25> // DSCOVR is tilted relative to ecliptic plane 
}


union {
  union {
    object {Moon}
    object {simpleframe scale 1000*km}
    rotate < 0,90+180,  0>
    rotate < 0,     0,-21>
    rotate < 0,     5,  0>
    rotate <-4,     0,  0>
 }
  object {simpleframe scale 1800*km}
 translate <0*km,0,Moon_Distance>
}


light_source{camLoc color White} 
