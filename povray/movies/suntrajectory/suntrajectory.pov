// --------------------------------------------------------------------------------
// Altitude
// 
// --------------------------------------------------------------------------------


#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#include "earth-simple.inc"
#include "sun_simple.inc"


#declare Earth_Distance   = 149600000*km;

global_settings { ambient_light .5 }

#declare Earth_Angle=45;
#declare Earth_Position=Earth_Distance*<cos(Earth_Angle*pi/180),0,sin(Earth_Angle*pi/180)>;

#declare camPos=Earth_Position+<20*Mm,10*Mm,20*Mm>;


camera {
  location camPos
  look_at  <0,0,0> //Earth_Position+<0,5*Mm,0>
  up <0,1,0>
  angle 40 // 50mm
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
  rotate <-23.44,0,0>
  translate  Earth_Position
}

object{fastSun()}
