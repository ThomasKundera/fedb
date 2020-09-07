// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#declare m=1;

#include "colors.inc"
#include "textures.inc"

#include "common.inc"
#include "frame.inc"
//#include "night_sky.inc"

#declare earthType=2;

#include "earth-simple.inc"

#declare Altitude=1*m;

// sun ---------------------------------------------------------------
light_source{<1500*m,2500*m,-2500*m> color White}
// sea water --------------------------
#declare SeaWaterTexture=texture{ Green_Glass
              normal{ripples 1
                     scale 1
                     turbulence 0.75
                     translate< 1*m,0,2*m>}
              finish{ambient 0.45
                     diffuse 0.55
                     reflection 0.3}
              scale 2*m
}// end of texture
//interior{I_Glass}

//-------------------------------------

#declare sphere_radius=Earth_Radius/100;

sphere {<0,-sphere_radius,0>,sphere_radius pigment {rgb <0,0,1>}} //texture {SeaWaterTexture}}


#for (i,1,5)
  #declare theta=acos(200*i*m/sphere_radius);
  torus {
    sphere_radius*cos(theta),10*i*cm
    translate <0,(sin(theta)-1)*sphere_radius-0*cm,0>
    pigment {color <i/5,(1-i/5),i/5,.3>}
  }
#end

#declare camloc=<0,Altitude,0>;
camera {
  location camloc
  look_at  camloc+<10*m,0,10*m>
  sky <0,1,0>
  //angle 62 // 30mm
  //angle 40 // 50mm
  angle 5
  right -x*image_width/image_height
}

object  {frame scale .4*m translate <1*m,0, 2*m>}


sky_sphere{
       pigment{ bozo turbulence 0.76
                         color_map { [0.5 rgb <0.20, 0.20, 0.9>]
                                     [0.6 rgb <1,1,1>]
                                     [1.0 rgb <0.1,0.1,0.1>]}
                         scale 1*m translate<8,0,11>
              }
      scale .2*m
}

//object {Earth}

