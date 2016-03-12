// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"

#include "common.inc"
#include "frame.inc"
#declare earthType=1;
#include "night_sky.inc"
#include "earth-simple.inc"

#declare lat =48.605;
#declare long= 7.709;


// Animation stuff
#declare duration=40*s_t;
#declare seconde=clock*duration;

#declare Altitude=100*m;

#switch (seconde)
#range (1,10)
  #declare Altitude=1*km*seconde/10;
#break
#range (10,20)
  #declare Altitude=10*km+30*km*(seconde-10)/10;
#break
#range (20,30)
  #declare Altitude=40*km+60*km*(seconde-20)/10;
#break
#range (30,40)
  #declare Altitude=100*km+100*km*(seconde-30)/10;
#break
#end

#declare Altitude=150*km;



light_source{<100,Earth_Radius+100,100> color White} 

camera {
  location <0*km,Earth_Radius+Altitude,0*km>
  look_at  <1,Earth_Radius+Altitude,1>
  //look_at  <0,0,0>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}

//object  {frame scale 1000}

object {Earth rotate <0,long,0> rotate <0,0,lat-90>}

