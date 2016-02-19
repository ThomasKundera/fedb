// --------------------------------------------------------------------------------
// Altitude
// 
// --------------------------------------------------------------------------------


#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "earth-simple.inc"

#declare Altitude=30*km;

light_source{<100,Earth_Radius+100,100> color White} 

camera {
  location <-10,Earth_Radius+Altitude,10>
  //look_at  <Earth_Radius,Earth_Radius-Altitude*10,Earth_Radius>
  look_at  <Earth_Radius,Earth_Radius+Altitude,Earth_Radius>
  up <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame}

object {Earth}

