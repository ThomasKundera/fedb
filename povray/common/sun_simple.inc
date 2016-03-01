// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// sun_simple.inc

// Only for a Sun as seen from Earth for now.

// ========== advanced settings ===========
#declare Sun_Distance     = 149600000*km;
#declare Sun_Radius       = 696000*km;


#declare SunBall=sphere {<0,0,0>,1 pigment {rgb <1,1,.8>}}

#declare SunLightSource=light_source {
    <0, 0, 0>
    color <1,1,.8>
    looks_like { SunBall }
    parallel
    point_at <-1,0,0>
  }
  
#macro fastSun()
  #local scalef=5000;
  object {SunLightSource
    scale Sun_Radius/scalef
    translate <Sun_Distance/scalef,0,0>
  }
#end



