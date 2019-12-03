// --------------------------------------------------------------------------------
// Second sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"

global_settings { ambient_light .1 }

// Animation stuff
#declare duration=30*s_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;

#declare f=2;

// Moon
#declare theMoon=sphere {
  <0,0,0>,100*m
  texture {pigment{ rgb <1,1,1> }}
}

#declare moonLoc=<800*m,1800*m,10000*m>;

#declare sonShoulder=<30*cm,2*m,20*cm>;
#declare hisSon=box {<0,0,0>,sonShoulder
  texture {pigment{ rgb <0,0,1> }}
}

object{hisSon}
object{theMoon translate moonLoc}

#declare camPos=sonShoulder+(moonLoc-sonShoulder)*(-f/1000);
#declare camAngle=2*(180./pi)*atan2(1.,2*f);

camera {
  location camPos+<1*m,0,0>
  look_at sonShoulder
  angle camAngle
  sky <0,1,0>
}

light_source {
    <10*m, 10*m,0>
    color <10,10,10>
}

light_source {
    <5*m, 5*m,-2*m>
    color <10,10,10>
}

light_source {
    moonLoc+<100*m,100*m,-500*m>
    color <1,1,1>
 }

//object {frame scale 1*m}

/*
plane { <0, 1, 0>, -1
scale 2*cm
    pigment {
      checker color <1,0,0,.5,.1>, color <0,1,0,.1,.5>
    }
}
*/