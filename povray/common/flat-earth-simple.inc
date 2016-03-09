// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-simple.inc


#declare Earth_Radius       = 10000*km;
#declare Cloud_Altitude     = 5*km;


#declare fastEarth=cylinder { <0,0,0>,<0,-.1,0>,1  pigment {rgb <.4,.4,.4>}  scale Earth_Radius}



#declare EarthTexture=texture {
  pigment{
    image_map {
      jpeg "data/earth_surface_map.jpg"
      map_type 0
    }
  }
}


#declare Earth=cylinder { <0,0,0>,<0,0,.1>,1 texture {EarthTexture} rotate <90,0,0> scale Earth_Radius}

