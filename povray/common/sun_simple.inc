// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// sun_simple.inc

// Only for a Sun as seen from Earth for now.

#declare Sun_Radius       =    696000*km;


#declare SunTextureSlow=texture {
  Correct_Pigment_Gamma(
    pigment{
      image_map {
	jpeg "data/20111230_004615_304.jpg"
	map_type 1
      }
    },.2)
    finish {
      ambient 2
    }
}

#declare SunTextureFast=texture {
  pigment{
    rgb <1,1,.8>
  }
}


#declare SunBall=sphere {<0,0,0>,1 texture {SunTextureSlow}}

#declare SunLightSource=light_source {
    <0, 0, 0>
    color <10,10,10>
    looks_like { SunBall }
  }
  
#macro fastSun()
  #local scalef=1;
  object {SunLightSource
    scale Sun_Radius/scalef
    //translate <Sun_Distance/scalef,0,0>
  }
#end



