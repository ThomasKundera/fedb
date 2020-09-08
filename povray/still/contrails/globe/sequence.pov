// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "common.inc"
#include "frame.inc"
//#include "night_sky.inc"

#declare earthType=2;

#declare Earth_Radius       = 100000*km;

#include "earth-simple.inc"

#declare Altitude=10*m;

light_source{<100,Earth_Radius+100,100> color White} 

camera {
  location <0,Earth_Radius+Altitude,0>
  look_at  <Earth_Radius,Earth_Radius+Altitude+Earth_Radius/5,Earth_Radius>
  sky <0,1,0>
  angle 62 // 30mm
  //angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame}

sky_sphere{
 pigment{ gradient <0,1,0>
          color_map{
          [0.0 color rgb<1,1,1>        ]
          [0.8 color rgb<0.1,0.25,0.75>]
          [1.0 color rgb<0.1,0.25,0.75>]}
        } // end pigment
} // end of sky_sphere -----------------

object {Earth}

#declare ShellHeight=10*km;

#declare EarthShell=difference {
  sphere {<0,0,0>, Earth_Radius+ShellHeight+200*m}
  sphere {<0,0,0>, Earth_Radius+ShellHeight}
}

#declare BlockLineZ=box {
  <-100*m,0,-Earth_Radius-100*km>,
  < 100*m,Earth_Radius+100*km,Earth_Radius+100*km>
}

#declare BlockLineX=object {BlockLineZ rotate <0,90,0>}

#declare BlockGroup=union {
  #local k=-10;

  #while (k<10)
    #local k=k+1;
    object {BlockLineZ translate <k*20*km,0,0>}
    object {BlockLineX translate <0,0,k*20*km>}
  #end
}

intersection {
  object {EarthShell}
  object {BlockGroup}
  pigment{ rgbft <1,0,0,.1,.4> }
  finish {
      ambient .5
  }
}

