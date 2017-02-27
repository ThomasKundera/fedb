// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// Cupola

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"


#declare m=.001;
#include "common.inc"
#include "frame.inc"

global_settings { ambient_light 1 }

light_source {
    <0, 10*m, 3*m>
    color <1,1,1>
}
light_source {
    <0, -10*m, 3*m>
    color <1,1,1>
}

camera {
  location   <3*m,2*m,-.3*m>
  look_at    <0,1.5*m,0>
  sky        <0,1,0>
  angle 50 // 50mm
}


#declare cpnbr=38.8*inch;
#declare cpnbl=cpnbr*sqrt(3)/2;
#declare cpnhr=19.85*inch;
#declare cpnl=(59.5*inch-36*inch)/sin(radians(180-123.7));
#declare cpna=(cpnbr-cpnhr)/2;
#declare cpnH=sqrt(cpnl*cpnl-cpna*cpna);

#declare cupane=difference {
  prism {
    linear_spline
    0, 1*cm, 5,
    <-cpnbr/2,0>, <cpnbr/2,0>, <cpnhr/2,cpnH>, <-cpnhr/2,cpnH>,<-cpnbr/2,0>
  }
  prism {
    linear_spline
    -1*cm, 2*cm, 5,
    <-(cpnbr-12.5*inch          )/2,    +7.9*inch/2>, < (cpnbr-12.5*inch          )/2,    +7.9*inch/2>,
    < (cpnhr-12.5*inch*sqrt(3)/2)/2,cpnH-7.9*inch/2>, <-(cpnhr-12.5*inch*sqrt(3)/2)/2,cpnH-7.9*inch/2>,
    <-(cpnbr-12.5*inch          )/2,    +7.9*inch/2>
  }
  translate <0,-1*cm,0>
}
 
#declare cupsubbox=box{<-cpnbr/2,36*inch-2*cm,cpnbl>,<cpnbr/2,36*inch+2*cm,cpnbl-36*inch>}
#declare cupola=union{
    difference {
    sphere {<0,0,0>,1*cm}
    cylinder {<0,0           ,0>,<0,36*inch     ,0> 40.6*inch     }
    cylinder {<0,0      -1*cm,0>,<0,36*inch-1*cm,0> 40.6*inch-1*cm}
    //cylinder {<0,36*inch-2*cm,0>,<0,36*inch+1*cm,0> 38.8*inch     }
    union {
      object {cupsubbox rotate <0,  0,0>}
      object {cupsubbox rotate <0, 60,0>}
      object {cupsubbox rotate <0,120,0>}
      object {cupsubbox rotate <0,180,0>}
      object {cupsubbox rotate <0,240,0>}
      object {cupsubbox rotate <0,300,0>}    
    }
  }
  union {
    object {cupane rotate <123.7-180,0,0>translate <0,36*inch,-cpnbl> rotate <0,  0,0>}
    object {cupane rotate <123.7-180,0,0>translate <0,36*inch,-cpnbl> rotate <0, 60,0>}
    object {cupane rotate <123.7-180,0,0>translate <0,36*inch,-cpnbl> rotate <0,120,0>}
    object {cupane rotate <123.7-180,0,0>translate <0,36*inch,-cpnbl> rotate <0,180,0>}
    object {cupane rotate <123.7-180,0,0>translate <0,36*inch,-cpnbl> rotate <0,240,0>}
    object {cupane rotate <123.7-180,0,0>translate <0,36*inch,-cpnbl> rotate <0,300,0>}
  }
  /*
  union {
    object {cupsubbox rotate <0,  0,0>}
    object {cupsubbox rotate <0, 60,0>}
    object {cupsubbox rotate <0,120,0>}
    object {cupsubbox rotate <0,180,0>}
    object {cupsubbox rotate <0,240,0>}
    object {cupsubbox rotate <0,300,0>}    
    texture {
      pigment{ rgbft <1,0,0,.1,.4> }
    }
  }*/
    
    texture {Brushed_Aluminum}
}

object {cupola rotate <0,30,0>}

cylinder {<0,59.5*inch,0>,<0,59.5*inch+ 1*cm,> 18.5*inch           texture {pigment{ rgbft <1,0,0,.1,.4> }}}
cylinder {<0,59.5*inch,0>,<0,59.5*inch+.5*cm,> 18.5*inch*2/sqrt(3) texture {pigment{ rgbft <0,1,0,.1,.4> }}}


object {frame scale 1*m translate <0,30*inch,0>}

box {<-5*cm,59.5*inch,-2*m>,<5*cm,59.5*inch+1*cm,2*m> texture {pigment{ rgbft <1,0,0,.1,.4> }}}
box {<-5*cm,36  *inch,-2*m>,<5*cm,36  *inch+1*cm,2*m> texture {pigment{ rgbft <1,0,0,.1,.4> }}}

box {<-5*cm,0,-2*m>,<5*cm,1*cm,2*m>  rotate <123.7,0,0> translate <0,36*inch,-cpnbr> texture {pigment{ rgbft <1,0,0,.1,.4> }}}
