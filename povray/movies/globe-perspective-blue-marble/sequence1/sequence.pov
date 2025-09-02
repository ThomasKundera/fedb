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

#include "frame.inc"


// Animation stuff
#declare duration=60*s_t;
#declare seconde=clock*duration;

#declare Altitude=1000*km+55000*km*(seconde*seconde)/(duration*duration);

// 1972 Blue Marble
#declare Altitude=29000*km;

// 2012 Blue Marble
//#declare Altitude=2415*km;


#declare camtext= text  {
  ttf "timrom.ttf" concat("Altitude: ", str(Altitude/km,0,1), " km") 0.01, <0,0>
  pigment { Red }
  scale <0.05,0.05,0.05>
}


light_source{<Earth_Radius+100*km  ,100*km,100*km> color White} 
light_source{<Earth_Radius+Altitude,  0*km,  0*km>,color White} 


#declare h=Altitude;
#declare r=Earth_Radius;

// 1972 Blue Marble
#declare a=3*degrees(atan(r/(r+h)));
// 2012 Blue Marble
//#declare a=3.3*degrees(atan(r/(r+h)));

#declare camlookat=<1*km,1*km,1*km>;



Set_Camera_Location(<Earth_Radius+Altitude,0*km,0*km>)
Set_Camera_Look_At(camlookat)
//Set_Camera_Aspect(image_width, image_height)
//Set_Camera_Aspect_Ratio(-image_width/image_height) // Should works but doesnt
//Set_Camera_Sky(<0,1,0>)
Set_Camera_Angle(a)
//Set_Camera_Right(-x*image_width/image_height) // Should works with the new screen.inc



//Screen_Object(camtext,<0.1,0.05>,0,true,.01)

// Those are 1972 Blue Marble coordinates (at about +/- 1° only)
object {Earth
rotate < 0,-141.5,  0>
rotate < 0,     0, 29>
rotate <-3,     0,  0>
}

// Those are 2012 Blue Marble coordinates (not so good, but enough)
/*
object {Earth
rotate < 0,    80,  0>
rotate < 0,     0, -20>
rotate <-3,     0,  0>
}
*/

