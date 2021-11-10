// --------------------------------------------------------------------------------
// sequence.pov
// 
// --------------------------------------------------------------------------------
#include "colors.inc"
#include "transforms.inc"
#include "golds.inc"

#declare earthType=2;

#include "common.inc"
#include "frame.inc"
#include "earth-simple.inc"
#include "sun_simple.inc"


// Begin
#declare camLoc=< 11*m , 21*m , -51*m >;
#declare camLA =< -1*km, 5*km,   20*km>;

// End
/*#declare camLoc=< 6.5*km , 1*km,   5*km>;
#declare camLA =< -4*km  , 2*km,   5*km>;*/

camera {
  location camLoc
  //location <5*km ,20*m , -50*m >
  look_at  camLA
  up <0,1,0>
  right <1.777777,0,0>
}

#declare SunLoc=<-1*km,3*km,10*km>;

SunFromEarth(SunLoc)

object {Earth translate <0,-Earth_Radius,0>}

//object {frame scale 100*m translate <0,0,0>}

//object {frame scale 200*m translate <-1*km,0,20*km>}
/*
intersection {
  object {frame scale 200*m translate < 10*m , 20*m , -50*m >}
  sphere {< 10*m , 20*m , -50*m >,300*m texture {XaxisTexture}}
}
*/
sky_sphere {EarthSimpleSky}

fog{ fog_type   2   
     distance   10*km 
     color      rgb<1,0.97,0.85>
     fog_offset 0.1 
     fog_alt    0.5 
     turbulence 0.2}


#declare yellowLine=cylinder{<0,-10*km,0>,<0,10*km,0>,5*m texture {T_Gold_3A}}

#declare yellowLines=union{
#local nx     = 1;
#while (nx <10)
  #local nz     = 1;
  #while (nz <10)
    object {yellowLine translate <nx*100*m,0,nz*100*m>}
    #local nz = nz + 1;
  #end
  #local nx = nx + 1;
#end
translate <0,-1*km,-1*km>
}

object {yellowLines Point_At_Trans(SunLoc) translate <0,0,3*km>}
