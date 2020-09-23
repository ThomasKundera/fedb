// --------------------------------------------------------------------------------
// First sequence
// Very simple case when the camera goes away from the Earth showing
// change in perspective.
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

#declare mydist=100000*km;

#declare al=1.5*(180./pi)*atan2(Earth_Radius+500*km,mydist);

#if (FLAT)
  #declare al=0.7*(180./pi)*atan2(Earth_Radius+500*km,mydist);
#else
  #declare al=1.5*(180./pi)*atan2(Earth_Radius+500*km,mydist);
#end

#declare camLoc=<0*km,0,mydist>;

camera {
  location camLoc
  look_at  <0,0,0>
  angle 2*al
  right x*image_width/image_height
}

#declare Year ="2017";
#declare Month=1+floor(seconde/(d_t*30));
#declare Day  =1+floor((seconde-(Month-1)*30)/d_t);

#declare M=str(Month,0,0);
#if (Month<10)
  #declare M=concat("0",M);
#end

#declare D=str(Day,0,0);
#if (Day<10)
  #declare D=concat("0",D);
#end

#declare mD=str(floor(seconde/d_t),0,0);

#declare jpgname=concat("data/",mD,".jpg");
#declare jpgnameflat=concat("data/",mD,"-flat.jpg");

#debug concat(jpgname,"\n")

#declare MappedEarthTextureSun=texture {
  pigment{
    image_map {
      jpeg jpgname
      map_type 1
      interpolate 2
    }
  }
}
#declare MappedEarthSun=sphere { <0,0,0>,1 texture {MappedEarthTextureSun} scale Earth_Radius}

#declare MappedEarthTextureSunFlat=texture {
  pigment{
    image_map {
      jpeg jpgnameflat
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