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


light_source{<1*cm,1*m,10*cm> color White} 

camera {
  location <10*cm,2*cm,10*cm>
  look_at  <6,0,6>
  sky <0,1,0>
}


#declare compass_diameter=15*mm;

// Gnomon
#declare gnomon=union{
  difference {
    difference {
      box { <-8.5*cm,0,-8.5*cm>,<8.5*cm,1*cm,8.5*cm>}
      cylinder {<0,2*mm,0>,<0,12*mm,0>,17*mm  translate <6*cm,0,6*cm>}
      texture {pigment { DMFWood3} }
    }
    union {
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
  cone {<0,0,0>,1*cm <0,20*cm,0>,0 texture {pigment { DMFWood3} } translate <0,1*cm,0>}
}

object {gnomon}

object {compass (-30) scale 1*mm translate <6*cm,2*mm,6*cm>} // Compass indicating 30 degrees to West.}                   


// Table
box { <-50*cm,0,-50*cm>,<50*cm,-2*cm,50*cm> texture {pigment { DMFWood2} }}


object  {frame}

