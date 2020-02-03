// --------------------------------------------------------------------------------

global_settings { ambient_light 10 }

#declare MappedEarthTexture=texture {
  pigment{
    image_map {
      png "sunmap.php.png"
      map_type 1
      interpolate 2
    }
  }
}

sphere { <0,0,0>,1 texture {MappedEarthTexture} scale 1 rotate <0,0,0> translate <-2,0,0>}

sphere { <0,0,0>,1 pigment {rgb <.8,.8,.8>}     scale 1                 translate < 2,0,0>}




camera {
  location <0,0,-10>
  look_at  <0,0,0>
  angle 40
}
