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
#declare duration=40*s_t;
#declare seconde=clock*duration;

#declare Altitude=100*m;

/*
#switch (seconde)
#range (1*s_t,5*s_t)
  #declare Altitude=1*km*seconde/5;
#break
#range (5*s_t,20*s_t)
  #declare Altitude=1*km+30*km*(seconde-5)/15;
#break
#range (20*s_t,30*s_t)
  #declare Altitude=31*km+60*km*(seconde-20)/10;
#break
#range (30*s_t,40*s_t)
  #declare Altitude=100*km+50*km*(seconde-30)/10;
#break
#end
*/

#declare Altitude=150*km*(seconde*seconde)/(60*60);


//#declare Altitude=1*km;

#declare camtext= text  {
  ttf "timrom.ttf" concat("Altitude: ", str(Altitude/km,0,1), " km") 0.01, <0,0>
  pigment { Red }
  scale <-0.05,0.05,0.05>
  //rotate <0,180,0>
  //translate <.2,.01,0>
}

