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


global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>;



#declare mysphere=sphere {<-Earth_Radius*cos(75*pi/180)-20*m,Earth_Radius*sin(75*pi/180)+20*m,0>,10*m
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}


#declare CamPos=yCenter(mysphere);

#debug concat("Value is:",vstr(3,CamPos-Earth_Position,",", 0,1),"\n")

camera {
  location CamPos
  look_at <0,0,0>
  up vnormalize(CamPos-Earth_Position)
  angle 100
  right -x*image_width/image_height
}

// object  {frame scale 1*Gm}


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

object{fastSun() translate Earth_Position*.9}
