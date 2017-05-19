// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "localcommon.inc"

/*
#declare IsoSphere=isosurface {
    function { f_sphere(x, y, z, r)-f_noise3d(x * r, y * r*10, z *r*10)/(10*r) }
    contained_by { box { -2*r, 2*r } }
    //texture {myBrushedAlu}
    texture {Chrome_Metal}
  }
  
#declare IsoSphereSimple=isosurface {
    function { f_sphere(x, y, z, r) }
    contained_by { box { -2*r, 2*r } }
    texture {myBrushedAlu}
  }
*/
//object {IsoSphere}
  
sphere { <0,0,0>,r texture {myBrushedAlu} }
