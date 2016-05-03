// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
//#include "night_sky.inc"
#include "sun_simple.inc"

#declare earthType=2;

#include "earth-simple.inc"

#declare Altitude=10*m;

global_settings { ambient_light 0 }

camera {
  location < 0   ,Earth_Radius+Altitude,0>
  look_at  <100*m,Earth_Radius+Altitude,0>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

object  {frame scale 5*m translate <0,Earth_Radius,0> translate <100*m,1*m,10*m>}
/*
sky_sphere{
 pigment{ gradient <0,1,0>
          color_map{
          [0.0 color rgb<1,1,1>        ]
          [0.8 color rgb<0.1,0.25,0.75>]
          [1.0 color rgb<0.1,0.25,0.75>]}
        } // end pigment
} // end of sky_sphere -----------------
*/
//object {Earth}
object {fastEarth}

object {fastSun(1000) translate <Earth_Distance/1000,0,0> rotate <0,0,3>}
//light_source{<Earth_Distance/1000,0,0> color White  rotate <0,0,4>} 
//light_source{<1000*m,Earth_Radius+Altitude,0> color White} 
