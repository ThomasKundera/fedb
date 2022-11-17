// --------------------------------------------------------------------------------
// Finding continents as pictured on EPIC_00000.png
// --------------------------------------------------------------------------------
#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "earth-simple.inc"

#declare mystep=3;

global_settings { ambient_light 1.2 }

#declare mydist=1475207*km; // That exact values comes from Wikipedia

#switch ( mystep)
  #case (1)
  #case (2)
    #declare dateH=12;
    #declare dateM=0;
    #declare dateS=0;
  #break
  #case (3)
    #declare dateH=19;
    #declare dateM=50;
    #declare dateS=0;
  #break
#end

// Time is UTC, so noon at 12:00 over Greenwitch.
#declare TimeOfTheDay=360*(-(dateH*3600+dateM*60+dateS)-6*3600)/86400;

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
  rotate < 0,TimeOfTheDay, 0>
}

//object {frame scale 1000*km}

light_source{camLoc color White} 
