// --------------------------------------------------------------------------------
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#include "night_sky.inc"
#declare earthType=1;
#include "earth-simple.inc"

// Animation stuff
#declare duration=y_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;


global_settings { ambient_light 1.2 }

#declare mydist=500000*km;

#declare al=1.5*(180./pi)*atan2(Earth_Radius+500*km,mydist);

#declare camLoc= <0*km,0,mydist>;
camera {
  location camLoc
  look_at  <0,0,0>
  angle 1.9*al
  right x*image_width/image_height
}


#declare MappedEarthTextureSun=texture {
  pigment{
    image_map {
      png "data/World_Time_Zones_Map.png"
      map_type 1
      interpolate 2
    }
  }
}
#declare MappedEarthSun=sphere { <0,0,0>,1 texture {MappedEarthTextureSun} scale Earth_Radius}

object {MappedEarthSun}


//object {frame scale 1000*km}

light_source{camLoc color White} 
