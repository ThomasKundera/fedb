// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#declare m=1;

#include "colors.inc"
#include "textures.inc"
#include "glass_old.inc"
#include "common.inc"
#include "frame.inc"
//#include "night_sky.inc"

#declare earthType=2;
#include "earth-simple.inc"

// Animation stuff
#declare duration=30*s_t;
#declare timeOffset=0;
#declare seconde=clock*duration+timeOffset;

#declare Altitude=10*m;
#declare torusMag=1;
#declare sphere_radius=Earth_Radius/1000;
#include "squarestuff.inc"


// sun ---------------------------------------------------------------
light_source{<1500*m,2500*m,-2500*m> color White}
// sea water --------------------------
#declare SeaWaterTexture=texture{pigment { rgb <0.2, 0.2, 0.2> } 
               normal {pigment_pattern{ crackle  
                                        colour_map { [0, rgb 0]
                                                     [1, rgb 1] } 
                                          
                       turbulence 1.7 translate<0,0,1>} 0.5}
              finish { ambient 0.15 diffuse 0.65 
                       brilliance 6.0 phong 0.8 phong_size 120
                       reflection 0.6}
	      scale <1.2,0.7,.6>*2*m  rotate<0,10,0>
	      translate< 1.2*m,100*cm,0.6*m>*seconde/20
}// end of texture
//interior{I_Glass}

//-------------------------------------

sphere {<0,-sphere_radius,0>,sphere_radius
	//pigment {rgb <0,0,1>}
	texture {SeaWaterTexture} interior{I_Glass}
}


#for (i,1,5)
  #declare theta=acos(200*i*m/sphere_radius);
  torus {
    sphere_radius*cos(theta),10*sqrt(i)*cm
    translate <0,(sin(theta)-1)*sphere_radius-0*cm,0>
    pigment {color <i/5,(1-i/5),i/5,.3>}
  }
#end



#declare camloc=<0,Altitude,0>;
#declare camlookat=vrotate(<10*m,Altitude,0>,<0,360*(seconde/duration),0>);

camera {
  location camloc
  look_at  camlookat
  sky <0,1,0>
  //angle 62 // 30mm
  //angle 40 // 50mm
  angle 92
  right -x*image_width/image_height
}

object  {frame scale .4*m translate <1*m,0, 2*m>}



sky_sphere{
       pigment{ bozo turbulence 0.76
                         color_map { [0.5 rgb <0.20, 0.20, 0.9>]
                                     [0.6 rgb <1,1,1>]
                                     [1.0 rgb <0.1,0.1,0.1>]}
                         scale 1*m translate<8,0,11>
              }
      scale .2*m
}


