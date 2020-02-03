// --------------------------------------------------------------------------------

global_settings { ambient_light 0.10 }

#declare tktype=0;
#declare ang=clock*360;

#declare MappedEarthTexture=texture {
  pigment{
    image_map {
      png "sunmap.php.png"
      map_type 1
      interpolate 2
    }
  }
}

#if (tktype = 0)
  sphere { <0,0,0>,1 texture {MappedEarthTexture finish {ambient 10}} scale 1 rotate <0,ang,0> translate <0,0,0>}
#else
  sphere { <0,0,0>,1 pigment {rgb <.8,.8,.8>}     scale 1                                    translate <0,0,0>}
#end

#plane  { <1,0,0> 0 pigment {rgb <0,1,0>} }


#if (tktype = 1)
light_source{ <2,0,-2> color rgb <1,1,1>
              parallel
              point_at<2, 0, 1>
              //fade_distance 2
              //fade_power    3
            } 
#end

camera {
  location <0,0,-10>
  look_at  <0,0,0>
  angle 20
  right x*3/2
}
