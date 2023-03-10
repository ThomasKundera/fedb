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

// Animation stuff
#declare duration=3*j_t;
#declare seconde=clock*duration;


global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>;

#declare camPos=Earth_Position+<20*Mm,10*Mm,20*Mm>;


camera {
  location camPos
  //look_at  <0,0,0> //Earth_Position+<0,5*Mm,0>
  look_at  Earth_Position
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
  rotate <0,360*seconde/j_t,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}

object{fastSun()}
