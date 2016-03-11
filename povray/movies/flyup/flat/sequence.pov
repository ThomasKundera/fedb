// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#include "flat-earth-simple.inc"

#declare Altitude=50000*km;

light_source{<100,Altitude+100,100> color White} 

camera {
  location <0,Altitude,0>
  look_at  <1,0,1>
  //sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame}

object {Earth}
 