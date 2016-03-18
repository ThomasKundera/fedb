// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "commonfly.inc"
#include "earth-simple.inc"

light_source{<100,Earth_Radius+100,100> color White} 
light_source{<0*km,Earth_Radius+Altitude,0*km>,color White} 

//#declare Altitude=.11*km;


#declare h=Altitude;
#declare r=Earth_Radius;
#declare hp=r*h/(r+h);
#declare l=r*sqrt(h*(2*r+h))/(r+h);

#declare LookAtHorizon=true;

#if (LookAtHorizon)
  #declare camlookat=<l/sqrt(2),Earth_Radius-hp,l/sqrt(2)>;
#else
  #declare camlookat=<1,Earth_Radius+Altitude,1>;
#end



Set_Camera_Location(<0*km,Earth_Radius+Altitude,0*km>)
Set_Camera_Look_At(camlookat)
Set_Camera_Aspect(image_width, image_height)
//Set_Camera_Aspect_Ratio(-image_width/image_height) // Should works but doesnt
Set_Camera_Sky(<0,1,0>)
Set_Camera_Angle(40)
//Set_Camera_Right(-x*image_width/image_height) // Should works with the new screen.inc


/*
camera {
  location <0*km,Earth_Radius+Altitude,0*km>
  look_at  <1,Earth_Radius+Altitude,1>
  //look_at  <0,0,0>
  sky <0,1,0>
  //angle 62 // 30mm
  angle 40 // 50mm
  right -x*image_width/image_height
}
*/
//object  {frame scale 1000}

Screen_Object(camtext,<0.1,0.05>,0,true,.01)

object {Earth rotate <0,long,0> rotate <0,0,lat-90>}


