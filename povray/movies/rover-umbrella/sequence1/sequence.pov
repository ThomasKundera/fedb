// --------------------------------------------------------------------------------
// Just a camera on the lunar rover
// --------------------------------------------------------------------------------

#include "colors.inc"
#declare m=.1;
#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"

// Animation stuff
#declare duration=10*s_t;
#declare timeOffset=0*j_t;
#declare seconde=clock*duration+timeOffset;

global_settings { ambient_light 1.2 }

// Trivial lunar ground
plane {<0,1,0>,0  pigment {rgb <.2,.2,.2>}}

// trivial Earth
sphere {<0,100*km,1000*km>,10*km pigment {rgb <.2,.2,2.>}
rotate <0,4,0> // a bit on side
}

// trivial umbrella
sphere {<0,0,0>,50*cm
 	pigment {checker color rgb <1,0,0> color rgb <0,1,0> scale .1*m}
	scale <1,1,0.05> // Flattening it
	translate <-.8*m,1*m,1*m>
}

// Moving the camera in povray is sometimes non-trivial
//#declare camLoc=<10*cm,1*m,-1*m>;

#declare sphereCampos=sphere{ <0,0,0>,1*cm // start position
	translate <0,10*cm,-5*cm>  // focal plane is not on the rotation axis
	rotate    <0*seconde,0,0> // that's the camera panning we want to observe
	translate <0,1*m,0>        // Put the camera on its stick
}

#declare sphereCamLookat=sphere{ <0,0,0>,1*cm // start position
	translate <0,0,100*km>    // Far away
	rotate    <0*seconde,0,0> // that's the camera panning we want to observe
	translate <0,1.1*m,0>     // peace of mind
}


#declare camLoc=yCenter(sphereCampos);
#declare camLookat=yCenter(sphereCamLookat);

camera {
  location camLoc
  look_at  camLookat
  right x*image_width/image_height
}


object {frame scale 1*m translate <-10*cm,0,-10*cm>}

light_source{camLoc color White} 
