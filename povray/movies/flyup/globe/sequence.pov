// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#include "earth-simple.inc"

#declare Altitude=100*km;

light_source{<100,Earth_Radius+100,100> color White} 

camera {
  location <0,Earth_Radius+Altitude,0>
  look_at  <Earth_Radius,Earth_Radius+Altitude,Earth_Radius>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame}

object {Earth}

