// --------------------------------------------------------------------------------
// Simple retrograding example
// 
// --------------------------------------------------------------------------------

#include "common.inc"
#include "frame.inc"

// For aesthetic
#include "night_sky.inc"

// Two objects rotating around a same center

// We dont pretend for a realistic Earth/whatever planet
// model yet, just respecting the principle.
r1=100000*km;  // With default units, it makes 100
r2=200000*km;

// relative rotation speed will follow Newton's laws:
// P=-mK/r²
// F= mv²/r
// P1(r1)=F1(r1)
// P2(r2)=F2(r2)
// -mK/r1²=mv1²/r1
// -mK/r2²=mv2²/r2
// -K/r1=v1²
// -K/r2=v2²
// v1²/v2²=r2/r1
// v1/v2=\sqrt(r2/r1)
// speed decrease in square root of radius

vtheta1=2*pi/y_t; // One revolution per year

vheta2=sqrt(r1/r2)*vtheta1; // respecting speed ratio


#include "colors.inc"

#include "spline.mcr"

#declare earthType=1;
#include "earth-simple.inc"
#include "sun_simple.inc"

// Animation stuff
#declare duration=1*j_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;


#declare Sun_Loc=<-Earth_Distance,0,0>;

global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>+Sun_Loc;



#declare mysphere=sphere {<Earth_Radius,0,0>,1*m rotate <0,0,48.5> rotate <0,7.7,0>
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t+180,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}

#declare myspherelk=sphere {
  <Earth_Radius,0,0>,1*m translate <0,-10*m,0> rotate <0,0,48.5> rotate <0,7.7,0>
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t+180,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}

#declare camPos=yCenter(mysphere);
#declare camSky=yCenter(myspherelk);


#declare camLkat=(Sun_Loc+VProject_Plane(Sun_Loc-camPos,camPos-Earth_Position))/2;

/*
#debug concat("Earth_Position is: ",vstr(3,Earth_Position ,",", 0,20),"\n")
#debug concat("Sun_Loc is       : ",vstr(3,Sun_Loc,",", 0,20),"\n")
#debug concat("camPos is        : ",vstr(3,camPos ,",", 0,20),"\n")
#debug concat("camLkat is       : ",vstr(3,camLkat,",", 0,20),"\n")
#debug concat("camSky is        : ",vstr(3,camSky  ,",", 0,20),"\n")
*/

cylinder { camPos-<0,-10*m,0>+10*m*vnormalize(camLkat),
	   camPos-<0, 10*m,0>+10*m*vnormalize(camLkat),
	   1*m
	   texture {ZaxisTexture}
	   }

camera {
  location camPos
  look_at camLkat
  sky camSky
  angle 80
  right -x*image_width/image_height
}


union {
  object {Earth}
  cylinder {
    <0,-Earth_Radius-3*Mm,0>,
    <0, Earth_Radius+3*Mm,0>,
    100*km
    texture {YaxisTexture}
  }
  rotate <0,360*seconde/j_t,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}

object{fastSun() scale 1 translate Sun_Loc*1}
