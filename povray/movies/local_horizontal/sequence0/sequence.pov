// --------------------------------------------------------------------------------
// Just some light through clouds
// 
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "textures.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"

global_settings { ambient_light .3 }

sky_sphere{
   Correct_Pigment_Gamma(pigment {skyPigment},4)
}
sky_sphere{
   pigment {skyPigment}
}


#declare dtime=10;
#declare seconde=dtime*clock;

#declare camloc=<10,0,0>;
#declare camlookat=camloc+<-10,0,0>;

camera {
  location camloc
  look_at  camlookat
  sky <0,1,0>
  //angle 62 // 30mm
  //angle 40 // 50mm
  angle 60
  right -x*image_width/image_height
}

#declare galaxyPigment=pigment {
  image_map {
    png "data/Messier51_alpha.png"
    map_type 1
  }
    rotate <0,0,0>
}

sphere {
  <0,0,0>,1
  pigment {galaxyPigment}
  finish {ambient 2}
  scale <1,2,1>
  rotate <0,0,0>
}

object  {frame scale .4 translate <-5,1,1>}
