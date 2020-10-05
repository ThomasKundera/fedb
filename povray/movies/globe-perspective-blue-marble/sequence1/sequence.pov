// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "colors.inc"
#include "screen_mjh.inc"

#include "common.inc"
#declare earthType=1;
#include "earth-simple.inc"
#include "night_sky.inc"

//#include "frame.inc"

#declare lat =48.605;
#declare long= 7.709;


// Animation stuff
#declare duration=60*s_t;
#declare seconde=clock*duration;

#declare Altitude=10000*km;

//#declare Altitude=150*km*(seconde*seconde)/(60*60);

#declare camtext= text  {
  ttf "timrom.ttf" concat("Altitude: ", str(Altitude/km,0,1), " km") 0.01, <0,0>
  pigment { Red }
  scale <-0.05,0.05,0.05>
}


light_source{<100*km,Earth_Radius+100*km,100*km> color White} 
light_source{<0*km,Earth_Radius+Altitude,0*km>,color White} 


#declare h=Altitude;
#declare r=Earth_Radius;
#declare a=3*degrees(atan(r/(r+h)));

#declare camlookat=<1*km,1*km,1*km>;



Set_Camera_Location(<0*km,Earth_Radius+Altitude,0*km>)
Set_Camera_Look_At(camlookat)
//Set_Camera_Aspect(image_width, image_height)
//Set_Camera_Aspect_Ratio(-image_width/image_height) // Should works but doesnt
//Set_Camera_Sky(<0,1,0>)
Set_Camera_Angle(a)
//Set_Camera_Right(-x*image_width/image_height) // Should works with the new screen.inc



//Screen_Object(camtext,<0.1,0.05>,0,true,.01)

object {Earth rotate <0,long,0> rotate <0,0,lat-90>}


