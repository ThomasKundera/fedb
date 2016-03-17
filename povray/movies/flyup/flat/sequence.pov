// --------------------------------------------------------------------------------
// Flat sequence
// 
// --------------------------------------------------------------------------------

#include "commonfly.inc"
#declare Earth_Radius       = 18500*km;
#include "flat-earth-simple.inc"

//#declare Altitude=100*km;

light_source{<100,Altitude+100,100> color White} 

camera {
  location <0,Altitude,0>
  //look_at  <1,0,1>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame scale 10*km translate <1*km,1*km,1*km>}

object {Earth rotate <0,long,0> translate <0,0,-.2*lat*Earth_Radius/90>}
 