// --------------------------------------------------------------------------------
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "moon-simple.inc"

// Animation stuff
//#declare duration=y_t;
//#declare timeOffset=0;
//#declare seconde=clock*duration+timeOffset;


global_settings { ambient_light 1.2 }

#declare mydist=10000*km;

#declare al=1.5*(180./pi)*atan2(Moon_Radius+500*km,mydist);

#declare camLoc= <1000*km,Moon_Radius+10*km,0>;
camera {
  location camLoc
  look_at  <-1000*km,Moon_Radius,0>
  angle 45
  right x*image_width/image_height
}

object {Moon}

object {frame scale 1000*km}

light_source{camLoc color White} 
