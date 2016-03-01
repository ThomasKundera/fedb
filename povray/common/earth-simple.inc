// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-simple.inc


// ========== advanced settings ===========
#declare Earth_Radius       = 6371*km;
#declare Cloud_Altitude     = 5*km;


#declare fastEarth=sphere {<0,0,0>,Earth_Radius pigment {rgb <.4,.4,.4>}}


// ----------------------------------------
// water
// ----------------------------------------

#declare WaterTexture=texture{
  pigment { rgb <0.2, 0.2, 0.2> } 
		normal { bozo 1.75 
			turbulence 0.9 translate<0,0,-2>}
		finish { ambient 0.15 diffuse 0.65 
			brilliance 6.0 phong 0.8 phong_size 120
			reflection 0.6}
		scale <2.0,1,0.3>*0.20  rotate<0,10,0>
		scale 2/Earth_Radius
}



#declare Earth_Water= sphere {
	<0,0,0>, 1
	texture { WaterTexture }
	scale Earth_Radius
	hollow on
}


#declare EarthSimpleSky=sky_sphere {
    pigment {
      gradient y
      color_map {
        [ 0.5  color CornflowerBlue ]
        [ 1.0  color MidnightBlue ]
      }
      scale 2
      translate -1
    }
}

#declare CloudTexture0=texture {
pigment {
    marble
    turbulence 0.5
    lambda 1.5
    omega 0.8
    octaves 5
    frequency 3
    color_map {
      [0.00 color Red]
      [0.33 color Blue]
      [0.66 color Yellow]
      [1.00 color Red]
    }
    rotate 45*z
  }
}

#declare CloudTexture=texture {
     pigment{ bozo turbulence 0.75
              octaves 6  omega 0.7
              lambda 2  phase 0.15
         color_map {
         [0.00 color rgb <1,1,1>*0.95]
         [0.05 color rgb <1,1,1>*1.25]
         [0.15 color rgb <1,1,1>*0.85]
         [0.25 color rgb <1,1,1>*0.65]
         [0.40 color rgb <1,1,1>*0.45]
         [0.85 color rgbt<1,1,1,1>]
         [1.00 color rgbt<1,1,1,1>]
       } // end color_map
       translate< 3, 10,-1>
       scale<0.3, 0.4, 0.2>*3
     } // end pigment
     finish{emission 1 diffuse 0}
}

#declare Earth_Clouds= sphere{ <0, 0, 0>, Earth_Radius+Cloud_Altitude hollow
  texture{CloudTexture
     scale 500
  } // end texture
   // no_shadow // optional!!
 } // end of sphere


#declare Earth= union{
  #switch (myFast)
   #case (1)
    object {fastEarth}
    #break
   #case (2)
    union {
     //object {fastEarth}
     object {Earth_Water}
     #break
    }
   #case (3)
    union {
     //object {fastEarth}
     object {Earth_Water}
     object {Earth_Clouds}
     #break
    }
   #break
   #else
    //object {Earth_Surface}
    //object {Earth_Clouds}
    //object {Earth_Atmosphere}
    //object {Earth_Water}
  #end
}

// ----------------------------------------

