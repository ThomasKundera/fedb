// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// earth-common.inc



#declare Earth_Distance   = 149600000*km; // Distance to Sun

#ifndef ( Earth_Radius )
  #declare Earth_Radius       = 6371*km;
#end

#declare Cloud_Altitude     = 5*km;


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
                scale .05/Earth_Radius
}

#declare WaterTextureTest=texture {
  pigment { checker pigment{Red}, pigment{Blue} }
  scale <0.8,1,0.3>*0.20  rotate<0,10,0>
  scale .05/Earth_Radius
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

#declare CloudTexture1=texture {
     pigment{ bozo turbulence 0.75
              octaves 6  omega 0.7
              lambda 2  phase 0.15
         color_map {
         [0.00 color rgb <1,1,1>*0.95]
         [0.05 color rgb <1,1,1>*1.25]
         [0.15 color rgb <1,1,1>*0.40]
         [0.25 color rgb <1,1,1>*0.30]
         [0.40 color rgb <1,1,1>*0.10]
         [0.85 color rgbt<1,1,1,1>]
         [1.00 color rgbt<1,1,1,1>]
       } // end color_map
       translate< 3, 10,-1>
       scale<0.3, 0.4, 0.2>*3
     } // end pigment
     finish{emission 1 diffuse 0}
}

#declare CloudTextureA= texture{ pigment {color rgbft<0.1,0.3,0.75,.3,.3>*0.7}
                 #if (version = 3.7 )  finish {emission 1 diffuse 0}
                 #else                 finish { ambient 1 diffuse 0}
                 #end 
}

#declare CloudTextureB= texture{ pigment{ bozo turbulence 0.75
                          octaves 6  omega 0.7 lambda 2 
                          color_map {
                          [0.0   color rgbt <0.95, 0.95, 0.95,.9>      ]
                          [0.05  color rgbt <1   , 1   , 1   ,.9>*1.25 ]
                          [0.15  color rgbt <0.85, 0.85, 0.85,.9>      ]
                          [0.55  color rgbt <1   , 1   , 1   , 1>*1 ]
                          [1.0   color rgbt <1   , 1   , 1   , 1>*1 ]
                          } // end color_map 
                         translate< 3, 0,-1>
                         scale <0.3, 0.4, 0.2>*3
                        } // end pigment
                 #if (version = 3.7 )  finish {emission 1 diffuse 0}
                 #else                 finish { ambient 1 diffuse 0}
                 #end 
}



