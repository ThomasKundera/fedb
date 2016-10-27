// --------------------------------------------------------------------------------
// Altitude
// 
// --------------------------------------------------------------------------------


#include "colors.inc"
#include "textures.inc"
#include "woods.inc"
#include "compass.inc"
#include "common.inc"
#include "frame.inc"


light_source{< 1*cm,1*m,10*cm> color  .3} 
light_source{<40*cm,1*m,30*cm> color 2  } 

camera {
  location <2*cm,30*cm,20*cm>
  look_at  <0,0,0>
  angle 41
  sky <0,1,0>
}


#declare compass_diameter=15*mm;


#declare levelbubble=union{
  difference {
    object{
      Round_Cylinder(<-.6,0,0>,<.6,0,0>,0.2001,0.2,1)
    }
    object{
      Round_Cylinder(<-.6,0,0>,<.6,0,0>,0.2001,0.2,1)
      scale .9
    }
    material {
      texture{ T_Glass3
        pigment{ color rgbt<1,0.1,0.9,0.6>}
        finish { phong 1}
      } // end of texture
      interior{ ior 1.35 caustics 0.025}
    } // end of material
  }
  difference {
    cylinder {<-.6,0,  0>,<.6, 0,0>,.2 scale .899}
    cylinder {<  0,.1,-1>,< 0,.1,1>,.2         }
    texture { Water }
  }
  rotate <0,0,0>
}

object {levelbubble scale 1*cm                 translate <-7.5*cm,1*cm,8*cm>}
object {levelbubble scale 1*cm rotate <0,90,0> translate <-8. *cm,1*cm,7*cm>}

// Gnomon
#declare gnomon=union{
  difference {
    difference {
      box { <-8.5*cm,0,-8.5*cm>,<8.5*cm,1*cm,8.5*cm>}
      cylinder {<0,2*mm,0>,<0,12*mm,0>,17*mm  translate <6*cm,0,6*cm>}
      cylinder {<-.6*cm,0,0>,<.6*cm,0,0>,0.2*cm scale 1.2                 translate <-7.5  *cm,1*cm,8*cm>}
      cylinder {<-.6*cm,0,0>,<.6*cm,0,0>,0.2*cm scale 1.2 rotate <0,90,0> translate <-8.   *cm,1*cm,7*cm>}

      texture {pigment { DMFWood3} rotate <3,25,10> }
    }
    
    union { // Central marks
      // Circles every cm
      #local i=1;
      #while (i<8)
        #if ( (i=7))
          #local d=0.3*mm;
        #else
          #local d=0.1*mm;
        #end
        torus { 10*i*mm,d }
        #local i=i+1;
      #end
      // Lines every 10°
      #local i=0;

      #while (i<18)
        #if ( (i=0) | (i=9) )
          #local d=0.3*mm;
        #else
          #local d=0.1*mm;
        #end
        cylinder { <-7*cm,0,0>,<7*cm,0,0> d rotate <0,10*i,0>}
        #local i=i+1;
      #end
      translate <0,1*cm,0>
      pigment { Black }
    }
    
    union { // Text
      #local i=0;
      #while (i<36)
        text { ttf "timrom.ttf" str(i*10,0,0) 0.2, 0
          scale <5*mm,5*mm,10*mm>
          translate <7.5*cm,-1*mm,-2.2*mm>
          rotate <90,180-i*10,0>
        }
        #local i=i+1;
      #end
      translate <0,.9*cm,0>
      pigment { Black }
    }
    
    union { // Compass marks
      // 4 marks every 90 degrees
      #local i=0;
      #while (i<4)
        box {
          <-compass_diameter-2*mm,-1  *mm, 0.5*mm>
          <-compass_diameter-5*mm, 0.1*mm,-0.5*mm>
          rotate <0,(90*i)+45,0>
        }
      #local i=i+1;
      #end
      // 8x2 Marcas pequeñas cada 45 grados
      // 8x2 little marks every 45 degrees 
      #local i=0;
      #while (i<8)
        box {
          <-compass_diameter-2*mm,-1  *mm, 0.25*mm>
          <-compass_diameter-4*mm, 0.1*mm,-0.25*mm>
          rotate <0,(45*i)+15,0>
        }
        box {
          <-compass_diameter-2*mm,-1  *mm, 0.25*mm>
          <-compass_diameter-4*mm, 0.1*mm,-0.25*mm>
          rotate <0,(45*i)+30,0>
        }
      #local i=i+1;
      #end

      text { ttf "timrom.ttf" "N" 0.2, 0
        scale 8*mm
        rotate <90,-90,0>
        translate <-compass_diameter-4*mm,0.1*mm,-2.2*mm>
      }
      
      text { ttf "timrom.ttf" "S" 0.2, 0
        scale 8*mm
        rotate <90,-90,0>
        translate <compass_diameter+9*mm,0.1*mm,-1.5*mm>
      }

      text { ttf "timrom.ttf" "E" 0.2, 0
        scale 8*mm
        rotate <90,-90,0>
        translate <3*mm,0.1*mm,compass_diameter+3*mm>
      }

      text { ttf "timrom.ttf" "W" 0.2, 0
        scale 8*mm
        rotate <90,-90,0>
        translate <3*mm,0.1*mm,-compass_diameter-10*mm>
      }
      pigment { Black }
      translate <6*cm,1*cm,6*cm>
    }
  }
  cone {<0,0,0>,5*mm <0,10*cm,0>,0 texture {pigment { DMFWood3} } translate <0,1*cm,0>}
}

object {gnomon}

object {compass (-30) scale 1*mm translate <6*cm,2*mm,6*cm>} // Compass indicating 30 degrees to West.}                   


// Table
box { <-50*cm,0,-50*cm>,<50*cm,-2*cm,50*cm> texture {pigment { DMFWood2}  rotate <-5,-30,-20> }}


//object  {frame}

