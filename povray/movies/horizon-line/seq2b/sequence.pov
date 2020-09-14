// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#declare m=1;

#include "colors.inc"
#include "textures.inc"
#include "glass_old.inc"
#include "common.inc"
#include "frame.inc"
//#include "night_sky.inc"

#declare earthType=2;
#include "earth-simple.inc"

// Animation stuff
#declare duration=30*s_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;

#declare Altitude=1*m;
#declare torusMag=10;
#declare sphere_radius=Earth_Radius/100;
#include "squarestuff.inc"

#declare camloc=<0,530*m,0>;
#declare camlookat=<0,0,0>;

cylinder {<-20*m,10*m,0>,<20*m,10*m,0>,5*m pigment { Red } rotate <0,360*(seconde/duration),0>}


camera {
  location camloc
  look_at  camlookat
  sky <1,0,0>
  angle 70
  right -x*image_width/image_height
}


object  {frame scale .4*m translate <1*m,0, 2*m>}
