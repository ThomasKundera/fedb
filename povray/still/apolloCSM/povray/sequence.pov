// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// CSM

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"


#declare m=1;

#include "common.inc"
#include "frame.inc"

global_settings { ambient_light 1 }

light_source {
    <10*m, 10*m, 30*m>
    color <1,1,1>
}
light_source {
    <-10*m, -10*m, 30*m>
    color <1,1,1>
}


#declare MyView=2;

#switch (MyView)
 #case (0)
  camera {
    location   <20*m,0*m,5*m>
    look_at    <0,0,5*m>
    sky        <0,1,0>
    right <1.5,0,0>
    angle 40
  }
 #break
 #case (1)
  camera {
    location   <-1*m,-5*m,30*m>
    look_at    <0,-.5*m,5*m>
    sky        <0,1,0>
    right <1.5,0,0>
    angle 16
  }
 #break
 #case (2)
  camera {
    location   < 1*m,-1*m,10*m>
    look_at    <0,-.25*m,5*m>
    sky        <0,1,0>
    right <1.5,0,0>
    angle 60
  }
#end

#declare Ccl =14.68*foot;
#declare CcR =(12.83/2)*foot;
#declare Ccol=5.94*foot;
#declare Ccor=(3.47/2)*foot;
#declare Ccogap=.38*foot;

#declare csmc=cylinder {<0,0,0>,<0,0,Ccl>,CcR
  texture {Brushed_Aluminum scale .1}
}

#declare csmco=cone {<0,0,0>,CcR,<0,0,Ccol>,Ccor
  translate <0,0,Ccl+Ccogap>
  texture {Chrome_Metal scale .1 rotate <4,5,6>}
}


object {csmc}
object {csmco}

object {frame scale 3*foot translate <0*cm,0*cm,0*cm>}


