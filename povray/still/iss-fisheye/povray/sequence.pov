// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// Cupola

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"


#declare m=.001;
#include "common.inc"
#include "frame.inc"
#declare earthType=4;
#include "earth-simple.inc"

#declare SideView=false;

global_settings { ambient_light 1 }

light_source {
    <0, 10*m, 3*m>
    color <1,1,1>
}
light_source {
    <0, -10*m, 3*m>
    color <1,1,1>
}

#if (SideView)
  sphere {<0,60*cm,0> 2*cm pigment {rgb <1,0,0>}}
  camera {
    location   <0,60*cm,-3*m>
    look_at    <0,60*cm,0>
    sky        <0,1,0>
    right <1.5,0,0>
    //angle 132 // 8mm
    angle 40
  }
#else
  camera {
    fisheye
    location   <0,60*cm,0>
    look_at    <0,1000*m,0>
    sky        <1,0,0>
    right <1.5,0,0>
    //angle 132 // 8mm
    angle 180
  }
#end

#declare CcH=489*mm+280*mm;
#declare CcR=2025*mm/2;

#declare CpbR=979*mm;
#declare CpbL=CpbR*sqrt(3)/2;

#declare CphR=648*mm;
#declare CphL=CphR*sqrt(3)/2;

#declare CpbH=CcH;
#declare CphH=1320*mm;
#declare CpH=CphH-CpbH;

#declare Cpl=CpH/sin(radians(60));

#declare Cpa=(CpbR-CphR)/2;
#declare CpHr=sqrt(Cpl*Cpl-Cpa*Cpa);

#declare CpWL =670*mm;
#declare CpWLh=430*mm;
#declare CpWbl=100*mm;
#declare CpWhl=150*mm;
#declare CpWll=Cpl-CpWbl-CpWhl;
#declare CpWb =sin(radians(60))*CpWbl;
#declare CpWh =sin(radians(60))*CpWhl;
#declare CpWl =sin(radians(60))*CpWll;

#declare CtwR=900*mm/2;

#declare cupane=difference {
  prism {
    linear_spline
    0, 1*cm, 5,
    <-CpbR/2,0>, <CpbR/2,0>, <CphR/2,CpHr>, <-CphR/2,CpHr>,<-CpbR/2,0>
  }
  prism {
    linear_spline
    -1*cm, 2*cm, 5,
    <-CpWL /2,CpWb     >, < CpWL /2,CpWb     >,
    < CpWLh/2,CpWb+CpWl>, <-CpWLh/2,CpWb+CpWl>,
    <-CpWL /2,CpWb>
  }
  translate <0,-1*cm,0>
}
 
#declare cupsubbox=box{<-CpbR/2,CcH -2*cm,CpbL>,<CpbR/2,CcH +2*cm,0>}
#declare cuptopbox=box{<-CphR/2,CphH-2*cm,CphL>,<CphR/2,CphH+0*cm,0>}

#declare cupanetop=union {
  object {cupane rotate <120-180,0,0> translate <0,CcH,-CpbL>}
  object {cuptopbox}
}

#declare cupola=union{
    difference {
    //sphere {<0,0,0>,1*cm}
    cylinder {<0,0           ,0>,<0,CcH     ,0> CcR     }
    cylinder {<0,0      -1*cm,0>,<0,CcH-1*cm,0> CcR-1*cm}
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
  difference {
    union {
      object {cupanetop rotate <0,  0,0>}
      object {cupanetop rotate <0, 60,0>}
      object {cupanetop rotate <0,120,0>}
      object {cupanetop rotate <0,180,0>}
      object {cupanetop rotate <0,240,0>}
      object {cupanetop rotate <0,300,0>}
    }
    cylinder {<0,CphH-4*cm,0>,<0,CphH+4*cm,0> CtwR}
  }
    
    texture {Brushed_Aluminum}
}

#if (SideView)
difference {
  object {cupola rotate <0,30,0>}
  plane {<0,0,1>,0*cm}
}
#else
  object {cupola rotate <0,0,0>}
#end
//object {frame scale 1*m translate <20*cm,20*cm,20*cm>}


object {Earth rotate <10,20,30> translate <0,Earth_Radius+450*km,0>}