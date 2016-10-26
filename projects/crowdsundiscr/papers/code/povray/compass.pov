//
// File: compass.pov
// POV Ray Version: 3.1
// Descripci�n: Ejemplo de la macro compass.inc.
// Unidades POV = mm
//
// Description: Sample for compass.inc.
// POV units = mm
//
// Date: 24-XI-1999
//
// Author: Sebastia Jardi Estadella
// e-mail: sje@tinet.fut.es
// URL:    www.fut.es/~sje/

// ==== Standard POV-Ray Includes ====
#include "colors.inc"	// Definiciones de colores
                        // Standard Color definitions
                        
#include "compass.inc"  // Definici�n de la macro para crear una br�jula
                        // Compass macro definition                        
// Adding a camera
// A�adir una c�mara

camera {
  location <5,30,-20>   // Posici�n de la c�mara
  look_at <0, 0, 0>     // Mirando a
}

light_source { <-5, 50, -20> White }

plane { y, -1.5 pigment { Brown }} 

object {
  compass (-30)    // Br�jula indicando 30 grados hacia el oeste.
                   // Compass indicating 30 degrees to West.
}                   


