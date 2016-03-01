// --------------------------------------------------------------------------------
// Altitude
// 
// --------------------------------------------------------------------------------


#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "earth-simple.inc"
#include "sun_simple.inc"


global_settings { ambient_light .5 }

background { color rgb <0.1, 0.1, 0.3> }

camera {
  location <10000*km,15000*km,30000*km>
  look_at  <0,0,0>
  up <0,1,0>
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame}


object {Earth}


object{fastSun()}
