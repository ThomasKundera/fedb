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
#declare duration=.5*j_t;
#declare timeOffset=1*j_t;
#declare seconde=clock*duration+timeOffset;


global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>;


#declare mysphere=sphere {<-Earth_Radius*cos(75*pi/180)+1*m,Earth_Radius*sin(75*pi/180)+1*m,0>,1*m
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t+180,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}


#declare finalCameraPos=yCenter(mysphere);
#declare finalCameraVit=<0,0,0>;


#declare CameraPath = create_spline (
      array[6] {Earth_Position+<-50*Mm,10*Mm,-50*Mm>  , <1,0,0>,
                Earth_Position+< 2*Mm ,7*Mm , 2*Mm> , <1,0,0>,
		finalCameraPos                        , finalCameraVit
      },
  create_hermite_spline + spline_sampling (on))
evaluate_spline (CameraPath, spline_clock (clock))
#declare camPos=spline_pos;


#declare CameraUp = create_spline (
      array[4] {<0,1,0>,vnormalize(<0,1,.1>),
                        vnormalize(<.1,1,0>),
                        vnormalize(camPos-Earth_Position)},
  create_default_spline +spline_sampling (on))
  
evaluate_spline (CameraUp, spline_clock (clock))
#declare camUp=spline_pos;
 
 
#declare camAngle=40+60*clock*clock*clock;
 

//sphere { finalCameraPos, 100*km texture {XaxisTextureNT}}


camera {
  location camPos
  look_at .99999999*finalCameraPos
  up camUp
  angle camAngle
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
