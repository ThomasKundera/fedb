// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-simple.inc

#include "earth-common.inc"

#declare fastEarth=sphere {<0,0,0>,Earth_Radius pigment {rgb <.4,.4,.4>}}

#declare MappedEarthTexture=texture {
  pigment{
    image_map {
      jpeg "data/earth_surface_map.jpg"
      map_type 1
      interpolate 2
    }
  }
}

#declare MappedEarth=sphere { <0,0,0>,1 texture {MappedEarthTexture} scale Earth_Radius}


#declare Earth_Water= sphere {
        <0,0,0>, 1
        texture { WaterTexture }
        scale Earth_Radius
        hollow on
}

#declare Earth_Clouds= sphere{ <0, 0, 0>, Earth_Radius+Cloud_Altitude hollow
  texture{CloudTextureA scale 1}
  texture{CloudTextureB scale 1}
}

#declare Earth= union{
  #switch (earthType)
   #case (1)
    object {MappedEarth}
   #break
   #case (2)
      object {Earth_Water}
   #break
   #case (3)
      object {Earth_Water}
      object {Earth_Clouds}
   #break
   #case (4)
    union {
      object {MappedEarth}
      object {Earth_Clouds}
    }    
   #else
    object {MappedEarth}
   #end
}
