// --------------------------------------------------------------------------------
// sequence
// Day and night on Earh
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "earth-simple.inc"
#include "sun_simple.inc"

// Animation stuff
#declare duration=3*d_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;


#declare Sun_Loc=<-Earth_Distance,0,0>;

global_settings { ambient_light .05 }


camera {
  location <0,0,5*Earth_Radius>
  look_at <0,0,0>
  angle 40
  right -x*image_width/image_height
  rotate <360*seconde/(3*d_t),0,0>
}

union {
  object {Earth}
  cylinder {
    <0,-Earth_Radius-3*Mm,0>,
    <0, Earth_Radius+3*Mm,0>,
    100*km
    texture {YaxisTexture}
  }
  #local i=0;
  #local s=24;
  #local s2=s/2;
  #while (i <s)
    object {
      sphere  {<0,Earth_Radius+0*km,0> 100*km  rotate  <360*i/s,0,0>}
      texture {
        pigment{rgb <i/s,1-i/s,abs(i/s-.5)>}
        finish {ambient .8}
      }
      no_shadow
    }
    #if (((i/2)-floor(i/2))<.001)
      torus {
        Earth_Radius*abs(sin(180*i/s)),1*km
        scale <1,25,1>
        translate<0,Earth_Radius*cos(180*i/s),0>
        texture {
          pigment{rgb <i/s,1-i/s,abs(i/s-.5)>}
          finish {ambient .5}
        }
        no_shadow
      }
      //#warning str(i,3,1)
    #end
    #local i = i + 1;
  #end
  rotate <0,360*seconde/d_t,0>
  rotate <0,0,23.44>
  translate  <0,0,0>
}

object{fastSun(1) scale 1 translate Sun_Loc*1}
