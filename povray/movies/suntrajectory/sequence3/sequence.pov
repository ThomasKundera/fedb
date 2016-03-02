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
#declare timeOffset=0;//1.5*j_t;
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
#declare camUp=vnormalize(camPos-Earth_Position);
#declare camLkat=VProject_Plane(Sun_Loc-camPos,camPos-Earth_Position);

//#debug concat("Value is:",vstr(3,camPos,",", 0,3),"\n")
//#debug concat("Value is:",vstr(3,camLkat,",", 0,3),"\n")
//#debug concat("Value is:",vstr(3,camUp,",", 0,3),"\n")


camera {
  location camPos
  look_at camLkat
  up camUp
  angle 100
  right -x*image_width/image_height
}

//object  {frame scale 10*m translate camPos translate 10*m*vnormalize(camLkat)}
//sphere {camPos, 2*m translate 20*m*vnormalize(camLkat) texture {YaxisTexture}}
//sphere {camPos, 2*m translate 20*m*vnormalize(camLkat) translate <-2*m,-2*m,-2*m> texture {XaxisTexture}}
//sphere {camPos, 2*m translate 20*m*vnormalize(camLkat) translate < 2*m, 2*m, 2*m> texture {XaxisTexture}}




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

object{fastSun() scale .1 translate Sun_Loc*.1}
