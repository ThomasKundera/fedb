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

#declare FLAT=false;
#declare VERTICAL=false;

#declare mydist=100000*km;

#declare al=1.5*(180./pi)*atan2(Earth_Radius+500*km,mydist);

#if (FLAT)
  #declare al=0.7*(180./pi)*atan2(Earth_Radius+500*km,mydist);
#else
  #declare al=1.5*(180./pi)*atan2(Earth_Radius+500*km,mydist);
#end

#if (VERTICAL)
#declare camLoc=<0*km,mydist,0>;
#else
#declare camLoc=<0*km,0,mydist>;
#end

camera {
  location camLoc
  look_at  <0,0,0>
  angle 2*al
  right x*image_width/image_height
}

#declare mD=str(floor(seconde/d_t),0,0);
#declare mD0=mD;
#if (floor(seconde/d_t)<10)
  #declare mD0=concat("0",mD0);
#end
#if (floor(seconde/d_t)<100)
  #declare mD0=concat("0",mD0);
#end

#declare pngname=concat("data/oldata/data/out1/",mD0,".jpg");
#declare pngnameflat=concat("data/oldata/data/out2/",mD,"-flat.jpg");

#debug concat(pngname,"\n")

#declare MappedEarthTextureSun=texture {
  pigment{
    image_map {
      jpeg pngname
      map_type 1
      interpolate 2
    }
  }
}
#declare MappedEarthSun=sphere { <0,0,0>,1 texture {MappedEarthTextureSun} scale Earth_Radius}

#declare MappedEarthTextureSunFlat=texture {
  pigment{
    image_map {
      jpeg pngnameflat
      map_type 0
      interpolate 2
      once
    }
    translate <-.5,-.5,0>
  }
}


#declare MappedEarthSunFlat=plane { <0,0,1>,0 texture {MappedEarthTextureSunFlat}  scale Earth_Radius rotate <0,0,0>}

#if (FLAT)
  object {MappedEarthSunFlat}
#else
  object {MappedEarthSun}
#end

//object {frame scale 1000*km}

light_source{camLoc color White} 
