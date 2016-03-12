// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
//#include "night_sky.inc"

#declare earthType=2;

#include "flat-earth-simple.inc"

#declare Altitude=1*km;

light_source{<100,Earth_Radius+100,100> color White} 

camera {
  location <0,Altitude,0>
  look_at  <Earth_Radius,Altitude,Earth_Radius>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame}

sky_sphere{
 pigment{ gradient <0,1,0>
          color_map{
          [0.0 color rgb<1,1,1>        ]
          [0.8 color rgb<0.1,0.25,0.75>]
          [1.0 color rgb<0.1,0.25,0.75>]}
        } // end pigment
} // end of sky_sphere -----------------

object {Earth}

