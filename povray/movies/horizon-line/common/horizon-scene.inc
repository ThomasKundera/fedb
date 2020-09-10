// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// horizon-scene.inc


// Sky -------------------------------------
sky_sphere{
       pigment{ bozo turbulence 0.76
                         color_map { [0.5 rgb <0.20, 0.20, 0.9>]
                                     [0.6 rgb <1,1,1>]
                                     [1.0 rgb <0.1,0.1,0.1>]}
                         scale 1*m translate<8,0,11>
              }
      scale .2*m
}



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

// Earth -------------------------------------
/*sphere {<0,-sphere_radius,0>,sphere_radius
	//pigment {rgb <0,0,1>}
	texture {SeaWaterTexture} interior{I_Glass}
}*/


#declare hd=sqrt(Altitude*Altitude+2*Altitude*sphere_radius);

#declare theta=acos(hd/sphere_radius);
torus {
  sphere_radius*cos(theta),10*cm*torusMag
  translate <0,(sin(theta)-1)*sphere_radius-0*cm,0>
  pigment {color Red}
}

#declare thick=.2;

#declare Letters=array[8]{"A","B","C","D","E","F","G","H"};

#for (i,0,7)
  #declare L=Letters[i];
  #declare myL=text {
      ttf "timrom.ttf" L thick, 0
  };
  #declare Lc=yCenter(myL);
  #declare Lc=<Lc.x,0,Lc.z>;
  object {myL
      translate -Lc/2
      pigment { Red }
      scale 30*m
      rotate <0,-90,0>
      translate <hd,(sin(theta)-1)*sphere_radius,0*m>
      rotate <0,45*i,0>
  }

#end

