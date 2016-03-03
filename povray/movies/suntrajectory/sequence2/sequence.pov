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

#declare Sun_Loc=<-Earth_Distance,0,0>;

// Animation stuff
#declare duration=.5*j_t;
#declare timeOffset=1*j_t;
#declare seconde=clock*duration+timeOffset;


global_settings { ambient_light .1 }

#declare Earth_Sun_Angle=360*seconde/a_t;
#declare Earth_Position=Earth_Distance*<cos(Earth_Sun_Angle*pi/180),0,sin(Earth_Sun_Angle*pi/180)>+Sun_Loc;


#declare mysphere1=sphere {<-(Earth_Radius+100*m)*cos(75*pi/180),(Earth_Radius+100*m)*sin(75*pi/180),0>,1*m
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t+30,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}
#declare mysphere2=sphere {<-(Earth_Radius+30*km)*cos(75*pi/180),(Earth_Radius+30*km)*sin(75*pi/180),0>,1*m
  texture {YaxisTexture}
  rotate <0,360*seconde/j_t+10,0>
  rotate <0,0,23.44>
  translate  Earth_Position
}


#declare finalCameraPos      =yCenter(mysphere1);
#declare almostfinalCameraPos=yCenter(mysphere2);
#declare finalCameraVit      =<0,0,0>;

sphere { finalCameraPos, 50*m texture {XaxisTextureNT}}

#declare CameraPath = create_spline (
      array[8] {Earth_Position+<-50*Mm,10*Mm,-50*Mm>  , <1,0,0>,
                Earth_Position+< 3*Mm ,8*Mm ,-4*Mm>   , <-1,0,0>,
                almostfinalCameraPos                  , <0,0,0>,
		finalCameraPos                        , finalCameraVit
      },
  create_hermite_spline + spline_sampling (on))
evaluate_spline (CameraPath, spline_clock (clock))
#declare camPos=spline_pos;


#declare CameraSky = create_spline (
      array[4] {<0,1,0>,vnormalize(<0,1,.1>),
                        vnormalize(<.1,1,0>),
                        vnormalize(camPos-Earth_Position)},
  create_default_spline +spline_sampling (on))
  
evaluate_spline (CameraSky, spline_clock (clock))
#declare camSky=spline_pos;
 
 
#declare camAngle=40;//+60*clock*clock*clock;
 



camera {
  location camPos
  look_at finalCameraPos+(Sun_Loc-finalCameraPos)*.000000001
  //look_at <0,0,0>
  sky camSky
  angle camAngle
  right -x*image_width/image_height
}

//object  {frame scale 5000*km translate Earth_Position}

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

object{fastSun() translate Sun_Loc}
