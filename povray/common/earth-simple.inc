// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-simple.inc


#declare Earth_Distance   = 149600000*km; // Distance to Sun

#declare Earth_Radius       = 6371*km;
#declare Cloud_Altitude     = 5*km;


#declare fastEarth=sphere {<0,0,0>,Earth_Radius pigment {rgb <.4,.4,.4>}}



#declare EarthTexture=texture {
  pigment{
    image_map {
      jpeg "data/earth_surface_map.jpg"
      map_type 1
    }
  }
}


#declare Earth=sphere { <0,0,0>,1 texture {EarthTexture} scale Earth_Radius}

