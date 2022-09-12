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


// Computing dates is too complex in Povray see auxiliary program "YearFraction.py"
// that spits this answer.
#declare YearFraction=-0.4336122195831841;
//#declare YearFraction=-.5;

#declare mydist=1475207*km; // That exact values comes from Wikipedia

#declare camLoc=<0*km,0,mydist>;

#declare declinaison_angle=23.43643; // Value from Wikipedia  23° 26' 11,150" 

#declare inclinaison_angle=5.145; // Wikipedia

camera {
  location camLoc
  look_at  <0,0,0>
  angle 0.65  // FIXME: this is larger than Wikipedia data (0.61)
  //angle 0.2 // Moon full scale
  right x*image_width/image_height
  rotate <0,0,25> // DSCOVR is tilted relative to ecliptic plane 
}


// Time computation: the file name contains data
// it ranges from 0 to 618
// during a real time of  3:50 p.m. to 8:45 p.m
// that is 4:55 h:m
// Frames are 145 464
#declare totalt=4*60+55;
#declare t1 = floor(145*totalt/618);
#declare t2 = floor(464*totalt/618);
#declare deltat=t2;
#declare tm=-138+deltat;

// Time is UTC, so noon at 12:00 over Greenwitch.
#declare TimeOfTheDay=360*(-(dateH*3600+dateM*60+dateS+deltat*60)-6*3600)/86400;

#declare rot=-360*tm/(28*24*60);


//#debug str(rot, 0, 3))

union {
  union {
    object {Moon}
    object {simpleframe scale 1000*km}
    rotate < 0,90+180    ,  0>
//    rotate < 0,         0,-21>
//    rotate < 0,         5,  0>
//    rotate <-4,         0,  0>
 }
 object {simpleframe scale 1800*km}
 translate <0*km,0,Moon_Distance>
 
 rotate <0,         rot,                 0>
 rotate <0,            0,-inclinaison_angle*0.4>
}

union {
  object {Earth}
  rotate < 0,TimeOfTheDay-360*YearFraction, 0>  
  // Put the tilt in, at Winter solstice reference
  rotate < -declinaison_angle,0, 0>
  // Year fraction rotation of the tilt (the time of the day is fixed above)
  rotate < 0,+360*YearFraction, 0>
}

light_source{camLoc color White} 
