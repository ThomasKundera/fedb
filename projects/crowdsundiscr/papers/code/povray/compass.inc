//
// File: compass.inc
// POV Ray Version: 3.1
// Descripción: compass (direccion) crea una brújula de 30 unidades de diámetro y 10 de alto. 
// Indicando direccion grados desde el Norte.
// Unidades POV = mm
//
// Description: Create a compass(Direction) with 30 units diameter and 10 units height.
// Indicating "Direction" degrees from North.
// POV units = mm
//
// Date: 24-XI-1999 
//                                         
// Author: Sebastia Jardi Estadella
// e-mail: sje@tinet.fut.es
// URL:    www.fut.es/~sje/

// compass (Diámetro, Altura, Dirección)
//
// Ejemplos de valores de direccion
// Direction values
// 0   = N
// 45  = NE     
// 90  = E
// 135 = SE
// 180 = S
// 225 = sW
// 270 = W
// 315 = NW
// 360 = N         

#include "glass.inc"
#include "metals.inc"
  
#macro compass (Direction) 
  
  // Tapa superior
  // Coverup
union {

  difference {
    torus {
      15,1
      scale <1,10,1>
      translate <0,5,0>
    }
    cylinder {    // Cilindro exterior de la tapa
      <0,0,0>     // External top cylinder
      <0,10,0>
      15
    }
    texture {Copper_Texture}
  }


  difference {
    cylinder {    // Cilindro exterior de la tapa
      <0,0,0>     // External top cylinder
      <0,10,0>
      15
    }
    cylinder {    // Cilindro interior de la tapa
      <0,-0.1,0>  // Internal top cynlinder
      <0,10-2+0.1,0>
      15-1.5
    } 
    pigment { White transmit 0.8 }
    interior{I_Glass}
  }
  
  // Tapa inferior o base
  // Base
  cylinder {
    <0,0,0>
    <0,2,0>
    15-1
    pigment { White }
  }
  
  // Eje de soporte de la aguja
  // Arrow axis 
  cylinder {
    <0,1,0>
    <0,6,0>
    1
    pigment { Brass }
  }
  
  // Aguja
  // Arrow 
  union {
    prism {
      linear_sweep  // or conic_sweep for tapering to a point
      linear_spline // linear_spline | quadratic_spline | cubic_spline
      4.7,          // height 1
      5,            // height 2
      3,            // number of points
      < 0, -2>, < 0, 2>, < -11, 0> 
      pigment { Blue }
    }
    prism {
      linear_sweep  // or conic_sweep for tapering to a point
      linear_spline // linear_spline | quadratic_spline | cubic_spline
      4.7,          // height 1
      5,            // height 2
      3,            // number of points
      // the <u,v> points
      < 0, -2>, < 0, 2>, < 11, 0> 
      pigment { White }
    }
    rotate Direction*y  // Giro de la aguja deseado
  }                     // Arrow rotation
  
  // 4 marcas cada 90 grados
  // 4 marks every 90 degrees
  #local i=0;
  #while (i<4)
    box {
      <-13,1.5,0.5>
      <-9,2.1,-0.5>
      rotate <0,(90*i)+45,0>
      pigment { Black }
    }
  #local i=i+1;
  #end 

  // 8x2 Marcas pequeñas cada 45 grados
  // 8x2 little marks every 45 degrees 
  #local i=0;
  #while (i<8)
    box {
      <-13,1.5,0.25>
      <-11,2.1,-0.25>
      rotate <0,(45*i)+15,0>
      pigment { Black }
    }
    box {
      <-13,1.5,0.25>
      <-11,2.1,-0.25>
      rotate <0,(45*i)+30,0>
      pigment { Black }
    }
  #local i=i+1;
  #end

  text { ttf "timrom.ttf" "N" 0.2, 0
    pigment { Black }
    scale 6
    rotate <90,-90,0>
    translate <-8.5,2.5,-2.2>
  }
  
  text { ttf "timrom.ttf" "S" 0.2, 01.5*mm
    pigment { Black }
    scale 6
    rotate <90,-90,0>
    translate <13,2.5,-1.5>
  }

  text { ttf "timrom.ttf" "E" 0.2, 0
    pigment { Black }
    scale 6
    rotate <90,-90,0>
    translate <2,2.5,9>
  }

  text { ttf "timrom.ttf" "W" 0.2, 0
    pigment { Black }
    scale 6
    rotate <90,-90,0>
    translate <2,2.5,-13>
  }

}
#end
