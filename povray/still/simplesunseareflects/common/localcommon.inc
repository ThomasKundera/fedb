// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// localcommon.inc

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"

#include "common.inc"
#include "frame.inc"
#include "sun_simple.inc"



#declare myBrushedAlu=texture {
    Chrome_Metal
    normal {
        bumps -0.5
        scale <1, 0.01, 0.01>
    }
    scale .001
}

#declare r=1000;

#declare SunTextureFast=texture {
  pigment{
    rgb <1,1,.8>
  }
  finish {
     specular 0.9 roughness 0.02
     ambient 2
  }
  
}

#declare SunBall=sphere {<0,0,0>,1 texture {SunTextureFast} no_shadow}

#declare SunLightSource=light_source {
    <0, 0, 0>
    color <100,100,100>
    looks_like { SunBall }
    parallel
    point_at <0,r*1.00001,0>
  }

object {SunLightSource scale r translate <0,r,100*r> rotate <-5.4,0,0>}

camera {
  location   <0,r*1.00001,0>
  look_at    <0,r*1.00001,r>
  sky        <0,1,0>
  angle 40 // 50mm
  right -x*image_width/image_height
}
