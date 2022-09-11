// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-simple.inc

#declare Moon_Distance   = 384000*km; // Distance to Moon

#ifndef ( Moon_Radius )
  #declare Moon_Radius       = 1737.4*km;
#end

#declare fastMoon=sphere {<0,0,0>,Moon_Radius pigment {rgb <.8,.4,.4>}}

#declare MappedMoonTexture=texture {
  pigment{
    image_map {
      jpeg "data/moon_surface_map.jpg"
      map_type 1
      interpolate 2
    }
  }
}

#declare MappedMoon=sphere { <0,0,0>,1 texture {MappedMoonTexture} scale Moon_Radius}


#declare Moon= union{
  #switch (earthType)
   #case (1)
    object {MappedMoon}
   #break
  #else
    object {fastMoon}
  #end
}
