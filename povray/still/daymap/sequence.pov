// --------------------------------------------------------------------------------

global_settings { ambient_light 0.10 }

#declare tktype=1;
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

// solstice: 21 juin : 23.4°
// equinoxe 23 septembre (94 days) 0°
// 10 september (81 days: 13)
#declare axisangle=13*23.4/94;


#if (tktype = 0)
  sphere { <0,0,0>,1 texture {MappedEarthTexture finish {ambient 10}} scale 1 rotate <0,ang,0> }
#else
  sphere { <0,0,0>,1 pigment {rgb <.8,.8,.8>}     scale 1                                      }
#end

//plane  { <1,0,0> 0 pigment {rgb <0,1,0>} }


#if (tktype = 1)
light_source{ <0,0,-10> color rgb <2,2,2>
              parallel
              point_at<0, 0, 1>
              //fade_distance 2
              //fade_power    3
              rotate <axisangle,0,0>
            } 
#end

camera {
  location <0,0,-10>
  look_at  <0,0,0>
  angle 20
  right x*3/2
#if (tktype = 1)  
  rotate <0,-ang,0>
#end
}
