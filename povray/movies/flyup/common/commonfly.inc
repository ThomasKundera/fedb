// --------------------------------------------------------------------------------
// Common for upflight
// 
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "common.inc"
#include "frame.inc"
#declare earthType=1;
#include "night_sky.inc"
//#include "screen_new.inc"
#include "screen.inc" // Should use my version, Something I dont understand yet

#declare lat =48.605;
#declare long= 7.709;


// Animation stuff
#declare duration=60*s_t;
#declare seconde=clock*duration;

#declare Altitude=100*m;


#declare Altitude=150*km*(seconde*seconde)/(60*60);

/* next
#switch (seconde)
#range (0*s_t,60*s_t)
#break
#else
  #declare Altitude=150*km
#end
*/

//#declare Altitude=1*km;

#declare camtext= text  {
  ttf "timrom.ttf" concat("Altitude: ", str(Altitude/km,0,1), " km") 0.01, <0,0>
  pigment { Red }
  scale <-0.05,0.05,0.05>
  //rotate <0,180,0>
  //translate <.2,.01,0>
}

