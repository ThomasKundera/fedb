// --------------------------------------------------------------------------------
// Second sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "spline.mcr"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#include "earth-simple.inc"
#include "sun_simple.inc"

// Animation stuff
#declare duration=2.5*j_t;
#declare timeOffset=1.5*j_t;
#declare seconde=clock*duration+timeOffset;


#declare Sun_Loc=<-Earth_Distance,0,0>;

global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>+Sun_Loc;



#declare mysphere=sphere {<-(Earth_Radius+100*m)*cos(75*pi/180),(Earth_Radius+100*m)*sin(75*pi/180),0>,1*m
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t+180,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}

#declare camPos=yCenter(mysphere);
#declare camSky=vnormalize(camPos-Earth_Position);


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
  angle 40
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
