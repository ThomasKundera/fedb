// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-simple.inc

#include "earth-common.inc"

#declare fastEarth=cylinder { <0,0,0>,<0,-.1,0>,1  pigment {rgb <.4,.4,.4>}  scale Earth_Radius}

#declare MappedEarthTexture=texture {
  pigment{
    image_map {
      jpeg "data/earth_surface_map.jpg"
      map_type 1
    }
  }
}

#declare MappedEarth=cylinder { <0,0,0>,<0,0,.1>,1 texture {MappedEarthTexture} rotate <90,0,0> scale Earth_Radius}


#declare Earth_Water= plane {
        <0,1,0>, 0
        texture { WaterTexture scale 1 }
        scale Earth_Radius
        hollow on
}

#declare Earth_Clouds= plane{ <0, 1 , 0>, Cloud_Altitude hollow
  texture{CloudTextureA scale 1}
  texture{CloudTextureB scale 1}
}

#declare Earth= union{
  #switch (earthType)
   #case (1)
    object {MappedEarth}
   #break
   #case (2)
    union {
      object {Earth_Water}
      object {Earth_Clouds}
    }
   #break
   #else
    object {MappedEarth}
   #end
}
