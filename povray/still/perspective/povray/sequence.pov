// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// CSM

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"

#declare m=0.000001;

#include "common.inc"

#declare Earth_Radius      = 6371*km;
#declare Moon_Radius       = 1737*km;

#declare Moon_Distance     = 384400*km;
 
#include "common.inc"
#include "frame.inc"

global_settings { ambient_light 1 }

light_source {
    <10000*km, 1000*km, 3000*km>
    color <1,1,1>
}


#declare MyView=0;

#switch (MyView)
 #case (0)
  camera {
    location   <Moon_Distance+1*km,Moon_Radius+1*km,Moon_Radius+1*km>
    look_at    <0,0,0>
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

sphere {<0,0,0>,Earth_Radius texture {
  pigment{ rgb <.2,.3,.6> }
    finish {
      ambient .5
    }
  }
}


sphere {<Moon_Distance,0,0>,Moon_Radius texture {
  pigment{ rgb <.2,.2,.2> }
    finish {
        ambient .5
    }
  }
}

