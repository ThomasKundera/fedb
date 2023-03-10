// --------------------------------------------------------------------------------
// First sequence
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
#declare duration=1*j_t;
#declare seconde=clock*duration;


global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>;

#declare CameraPath = create_spline (
   array[6] { -Earth_Position-<0,0,Earth_Distance/4>   , <0,0,0>,
              <0,1*Gm,100*km>                          , <1,0,0>,
               Earth_Position+<-50*Mm,10*Mm,-50*Mm>    , <0,0,0>},
   create_hermite_spline + spline_sampling (on))
   
#declare camClock=min(1,clock*1.1);
   
evaluate_spline (CameraPath, spline_clock (camClock))


#declare camPos=spline_pos;
#declare camlook=spline_tangent;


camera {
  location camPos
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
