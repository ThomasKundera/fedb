// --------------------------------------------------------------------------------
// First sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"

#declare m=.001;
#include "common.inc"
#include "frame.inc"
#declare earthType=1;
#include "earth-simple.inc"

global_settings { ambient_light 2 }

// 0: from ISS, 1: from way up, 2: movie
#declare geneType=1;

// Animation stuff
#declare duration=10*s_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;

#declare camLocStart=<0,0,-Earth_Radius-330*km>;
#declare camLocEnd  =<-1000*km,0,-11000*km>;
#declare camlocSpline =
  spline {
   natural_spline
  -0.2, camLocStart,//control point

   0.0, camLocStart,//start point
   1.0, camLocEnd,//end point

   1.2, camLocEnd //control point
  };
//#declare altitude=vlength(camlocSpline(clock))-Earth_Radius;

#declare camLookatStart=<Earth_Radius/10,0,0>;
#declare camLookatEnd  =<-1000*km,0,0>;
#declare camlookatSpline =
  spline {
   natural_spline
  -0.2, camLookatStart,//control point

   0.0, camLookatStart,//start point
   1.0, camLookatEnd,//end point

   1.2, camLookatEnd //control point
  };

#declare camAngleStart=170;
#declare camAngleEnd  =95;
#declare camAngleVal  = (camAngleEnd-camAngleStart)*clock+camAngleStart;


#switch(geneType)
  #case(0)
    camera {
        fisheye    
        location   camLocStart
        look_at    camLookatStart
        sky        <-1,-.15,0>
        right      <1.77419,0,0>
        angle      camAngleStart
    }
  #break
  #case(1)
     camera {
        location   camLocEnd
        look_at    camLookatEnd
        sky        <-1,-.15,0>
        right      <1.77419,0,0>
        angle      camAngleEnd
    }
  #break
  #case(2)
    camera {
        fisheye    
        location   camlocSpline(clock)
        look_at    camlookatSpline(clock)
        sky        <-1,-.15,0>
        right      <1.77419,0,0>
        angle      camAngleVal
    }
  #break
#end

object {Earth rotate <-47,-46,0>}

/*
#declare camtext= text  {
  ttf "timrom.ttf" concat("Altitude: ", str(Altitude/km,0,1), " km - Lens angle:",str(camAngleVal,0,1),"°") 0.01, <0,0>
  pigment { Red }
  scale <-0.05,0.05,0.05>
  //rotate <0,180,0>
  //translate <.2,.01,0>
}

Screen_Object(camtext,<0.1,0.05>,0,true,.01)
*/
