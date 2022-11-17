// --------------------------------------------------------------------------------
// Finding continents as pictured on EPIC_00000.png
// --------------------------------------------------------------------------------
#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "earth-simple.inc"

// 1: Base
// 2: Aligned to Greenwitch
// 3: Rotated at time of first DSCOVR pict
// 4: Axial tilt (but aligned to Greenwitch) at Winter Solstice
// 5: Axial tilt at Winter Solstice at 19:50
// 6: Axial tilt at 19:50 July 16 2015
#declare mystep=7;

global_settings { ambient_light 1.2 }

#declare real_declinaison_angle=23.43643; // Value from Wikipedia  23° 26' 11,150" 

#declare mydist=1475207*km; // That exact values comes from Wikipedia

#declare declinaison_angle=0; // for first images.

// Computing dates is too complex in Povray see auxiliary program "YearFraction.py"
// that spits this answer.
#declare realYearFraction=-0.4336122195831841;
#declare YearFraction=0;
#declare real_dscovr_tilt=<0,0,25>;
#declare dscovr_tilt=<0,0,0>;

#switch ( mystep)
  #case (1)
    #declare dateH=0;
    #declare dateM=0;
    #declare dateS=0;
    #break
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
  #case (4)
    #declare dateH=12;
    #declare dateM=0;
    #declare dateS=0;
    #declare declinaison_angle=real_declinaison_angle;
  #break
  #case (5)
    #declare dateH=19;
    #declare dateM=50;
    #declare dateS=0;
    #declare declinaison_angle=real_declinaison_angle;
  #break
  #case (6)
    #declare dateH=19;
    #declare dateM=50;
    #declare dateS=0;
    #declare declinaison_angle=real_declinaison_angle;
    #declare YearFraction=realYearFraction;
  #break
  #case (7)
    #declare dateH=19;
    #declare dateM=50;
    #declare dateS=0;
    #declare declinaison_angle=real_declinaison_angle;
    #declare YearFraction=realYearFraction;
    #declare dscovr_tilt=real_dscovr_tilt;
  #break
#end

// Time is UTC, so noon at 12:00 over Greenwitch.
#declare TimeOfTheDay=360*(-(dateH*3600+dateM*60+dateS)-6*3600)/86400;

#declare camLoc=<0,0,mydist>;

camera {
  location camLoc
  look_at  <0,0,0>
  angle 0.61   // Figure from Wikipedia
  right x*image_width/image_height
  
  rotate dscovr_tilt // DSCOVR is tilted relative to ecliptic plane 
}


union {
  object {Earth}
  object {simpleframe scale 7000*km} // Faster to render
  // Time of the day - Compensation for Sun orbit rotation included
  rotate < 0,TimeOfTheDay-360*YearFraction, 0>
  // Put the tilt in, at Winter solstice reference
  rotate < -declinaison_angle,0, 0>
  // Year fraction rotation of the tilt (the time of the day is fixed above)
  rotate < 0,+360*YearFraction, 0>
}

object {simpleframeold scale 8000*km}

light_source{camLoc color White} 
