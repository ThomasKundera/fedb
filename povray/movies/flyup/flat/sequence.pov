// --------------------------------------------------------------------------------
// Flat sequence
// 
// --------------------------------------------------------------------------------

#include "commonfly.inc"
#declare Earth_Radius       = 18500*km;
#include "flat-earth-simple.inc"

//#declare Altitude=100*km;

light_source{<100,Altitude+100,100> color White} 
light_source{<0*km,Altitude,0*km>,color White} 

Set_Camera_Location(<0*km,Altitude,0*km>)
Set_Camera_Look_At( <1,Altitude,1>)
Set_Camera_Aspect(image_width, image_height)
//Set_Camera_Aspect_Ratio(-image_width/image_height) // Should works but doesnt
Set_Camera_Sky(<0,1,0>)
Set_Camera_Angle(40)
//Set_Camera_Right(-x*image_width/image_height) // Should works with the new screen.inc

/*
camera {
  location <0,Altitude,0>
  //look_at  <1,0,1>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}
*/
//object  {frame scale 10*km translate <1*km,1*km,1*km>}

Screen_Object(camtext,<0.1,0.05>,0,true,.01)

object {Earth rotate <0,long,0> translate <0,0,-.2*lat*Earth_Radius/90>}
 