// --------------------------------------------------------------------------------
// Globe sequence
// 
// --------------------------------------------------------------------------------

#include "localcommon.inc"


#declare IsoSphere=isosurface {
    function { f_sphere(x, y, z, 1)-f_noise3d(x * 1000, y * 10000, z * 10000) * 0.000005 }
    contained_by { box { -2, 2 } }
    texture {myBrushedAlu}
    scale r
  }
  
#declare IsoSphereSimple=isosurface {
    function { f_sphere(x, y, z, 1) }
    contained_by { box { -2, 2 } }
    texture {myBrushedAlu}
    scale r
  }
  

object {IsoSphere}

box { -r,r texture {myBrushedAlu} }