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

#declare Moon_Distance     = 38440*km;
 
#include "common.inc"
#include "frame.inc"

global_settings { ambient_light .1 }


light_source {
    <Moon_Distance/2,Moon_Distance/3,Moon_Distance*2>
    color <1,1,1>
    parallel
    point_at <Moon_Distance/2,0,0>
}


#declare MyView=0;
#declare LookAt=0;

#switch (MyView)
 #case (0)
  #declare camloc=<Moon_Distance-10*km,Moon_Radius+100*m,100*m>;
  #declare camlookat=<0,0,0>;
  #declare camangle=60;

 #break
 #case (1)
  #declare camloc=<Moon_Distance*2,Moon_Radius+100*m,100*m>;
  #declare camlookat=<0,0,0>;
  #declare camangle=60;
 #break
 #case (2)
  #declare camloc=<Moon_Distance*2,Moon_Radius+100*m,100*m>;
  #declare camlookat=<0,0,0>;
  #declare camangle=30;
#end

#if (LookAt)
  #declare camlocdraw=camloc;
  #declare camlookatdraw=camlookat;
  #declare camangledraw=camangle;
  
  #declare camloc=<Moon_Distance*2,0,Moon_Distance*1.5>;
  #declare camlookat=<Moon_Distance,0,0>;
  #declare camangle=90;
  
  cone {
    camlocdraw,0
    camlookatdraw,Moon_Distance*tan((pi/180.)*camangledraw/2)
    pigment{ rgbft <1,0,0,0,.9> }
      finish {
      ambient .5
    }
  }
#end



camera {
  location   camloc
  look_at    camlookat
  sky        <0,1,0>
  right <1.5,0,0>
  angle camangle
}


light_source {
    camloc
    color <1,1,1>
}



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

