// --------------------------------------------------------------------------------
// Just some light through clouds
// 
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "common.inc"
#include "frame.inc"
#include "earth-common.inc"

#declare m=.2;

#declare CloudAltitude=400*m;


global_settings { ambient_light rgb<0,0,0> }
  global_settings {
    radiosity {
      pretrace_start 0.08
      pretrace_end   0.01
      count 150
      nearest_count 10
      error_bound 0.5
      recursion_limit 3
      low_error_factor 0.5
      gray_threshold 0.0
      minimum_reuse 0.005
      maximum_reuse 0.2
      brightness 1
      adc_bailout 0.005
   }
  }

/*
light_source{ <0,100,0> color rgb <1,1,1>
              parallel
              point_at<0, 0, 0> 
            } 
*/

#declare Angle=-20;

light_source{ <1000*tan(Angle),1000,1000*tan(Angle)> color rgb <1,1,1>
//light_source{ <0,1000,0> color rgb <1,1,1>
              parallel
              point_at<0, 0, 0> 
            } 
//light_source{<10,2,20> color White} 

#declare CamLocXY=3*CloudAltitude;
camera {
  location <CamLocXY,3*m,CamLocXY>
  look_at  <10*m,25*m*m,10*m>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

// Fog
media{
  scattering{
    1,  // scattering media type 1,2,3,4,5
    0.3 // color of the media (no comma!)
    extinction 0.25 //optional 0~1
  }// end of scattering
  intervals 50 //
    density {granite scale 100*m
      color_map {
        [0.0 rgb <1,1,1>*0.0]
        [0.5 rgb <1,1,1>*0.2]
        [1.0 rgb <1,1,1>*1  ]
        } // end of color_map
      }// end of density
}


sphere{ <20*m,1*m,20*m>,1*m
  pigment{color rgb<1,.3,.1>}
  }

/*
sky_sphere{
 pigment{ gradient <0,1,0>
          color_map{
          [0.0 color rgb<1,1,1>        ]
          [0.8 color rgb<0.1,0.25,0.75>]
          [1.0 color rgb<0.1,0.25,0.75>]}
        } // end pigment
} // end of sky_sphere -----------------
*/

//Ground
plane {
  <0,1,0>, 0*m
  //texture { WaterTexture scale 50 }
  pigment{color rgb<.3,.3,.1>}
}


//Clouds
object{
  difference {
    plane {
      <0,-1,0>, 0*m
    }
    union {
      plane {
        <0,-1,0>, -.1*m
      }
     
      #local ix=0;
      #while (ix<10)
        sphere {<0,0,0>,10*m translate <200*m,0,0> rotate <0,ix*360/10,0>}
        #local ix=ix+1;
      #end
      sphere {<0,0,0>,20*m}
    }
  }
  pigment{color rgb<.3,.3,.9>}
  translate <20*m,CloudAltitude,20*m>
}

object {frame scale 50*cm translate <10*m,1*m,10*m>}

  
