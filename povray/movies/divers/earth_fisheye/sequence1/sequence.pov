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

global_settings { ambient_light 1 }

#declare camLookat=<Earth_Radius/6,0,0>;

// Animation stuff
#declare duration=30*s_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;

  camera {
    fisheye    
    location   <0,0,-Earth_Radius-400*km>
    look_at    camLookat
    sky        <-1,0,0>
    right      <1.77419,0,0>
    //right      <1.5,0,0>
    angle 160
  }



object {Earth rotate <-47,-46,0>}

