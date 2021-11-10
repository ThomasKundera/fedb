// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// sun-simple.inc

#declare SunDistance=150*Gm;
#declare SunRadius=700*Mm;

#declare SunGlobe=sphere {
  <0,0,0>,1
  pigment {rgb <.4,.4,.4>}
}

#macro SunFromEarth(myV)
  union {
    object {SunGlobe scale vlength(v)*SunRadius/SunDistance translate myV}
    light_source {
      myV,color 5
      parallel
      point_at -myV
    }
  }
#end
