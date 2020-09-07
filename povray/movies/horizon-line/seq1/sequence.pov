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

sphere {<0,-sphere_radius,0>,sphere_radius texture {SeaWaterTexture}}


#declare theta=acos(50*m/sphere_radius);

torus {
  sphere_radius*cos(theta),10*cm
  translate <0,(1-sin(theta))*sphere_radius,0>
  pigment {color <1,0,0>}
}



//sphere {<0,sphere_radius +Altitude,0>,100*m pigment {color <1,0,0> }}

camera {
  location <0,Altitude,0>
  look_at  < 10*m,Altitude, 10*m>
  sky <0,1,0>
  angle 62 // 30mm
  //angle 40 // 50mm
  right -x*image_width/image_height
}

object  {frame scale .4*m translate <2*m,0, 2*m>}





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

