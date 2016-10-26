// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------

#include "shapes.inc"

#declare XaxisTexture = texture {
  pigment{ rgbft <1,0,0,.1,.4> }
  finish {
      ambient .5
  }
}
#declare XaxisTextureNT = texture {
  pigment{ rgb <1,0,0> }
  finish {
      ambient .5
  }
}
#declare YaxisTexture = texture {
  pigment{ rgbft <0,1,0,.1,.4> }
  finish {
      ambient .5
  }
}
#declare YaxisTextureNT = texture {
  pigment{ rgb <0,1,0> }
  finish {
      ambient .5
  }
}
#declare ZaxisTexture = texture {
  pigment{ rgbft <0,0,1,.1,.4> }
  finish {
      ambient .5
  }
}
#declare ZaxisTextureNT = texture {
  pigment{ rgb <0,0,1> }
  finish {
      ambient .5
  }
}


#macro FrameTick(Idx,texT,texNt)
  #local txt=concat(str(Idx,0,0)," >");
  difference {
    Round_Box(<-.5,-.1,-.1>,<.5,.1,.1>,.025,1)
    union {
      text {
	ttf "timrom.ttf" txt 2, 0
	texture { texNt }
	translate <-1.6,-.3,-1>
	scale <.3,.15,.2>
      }
      torus {
	.1,.05
	texture { texNt }
	rotate <0,0,90>
      }
    }
    texture {texT}
    scale .5
  }
#end

// Frame
#declare frame=union {
  union {
    cylinder {<50,0,0>,<-50,  0,  0> .005 texture {XaxisTexture}}
    cylinder {<0,50,0>,<  0,-50,  0> .005 texture {YaxisTexture}}
    cylinder {<0,0,50>,<  0,  0,-50> .005 texture {ZaxisTexture}}
    }
  sphere   {<0,0,0>,.001 pigment { color 1}}


  #local k=0;

  #while (k<10)
  #local n = 1;
  #while (n <10)
    #local l=k*10+n;
    object {FrameTick( l,XaxisTexture,XaxisTextureNT)                            translate < l, 0, 0>}
    object {FrameTick( l,YaxisTexture,YaxisTextureNT)          rotate <0,  0,90> translate < 0, l, 0>}
    object {FrameTick( l,ZaxisTexture,ZaxisTextureNT)          rotate <0,-90, 0> translate < 0, 0, l>}
    object {FrameTick(-l,XaxisTexture,XaxisTextureNT) scale .5                   translate <-l, 0, 0>}
    object {FrameTick(-l,YaxisTexture,YaxisTextureNT) scale .5 rotate <0,  0,90> translate < 0,-l, 0>}
    object {FrameTick(-l,ZaxisTexture,ZaxisTextureNT) scale .5 rotate <0,-90, 0> translate < 0, 0,-l>}
    #local n = n + 1;
  #end
    #local l=k*10+n;
    object {FrameTick( l,XaxisTexture,XaxisTextureNT) scale < 1,2,2>                   translate < l, 0, 0>}
    object {FrameTick( l,YaxisTexture,YaxisTextureNT) scale < 1,2,2> rotate <0,  0,90> translate < 0, l, 0>}
    object {FrameTick( l,ZaxisTexture,ZaxisTextureNT) scale < 1,2,2> rotate <0,-90, 0> translate < 0, 0, l>}

    object {FrameTick(-l,XaxisTexture,XaxisTextureNT) scale <.5,1,1>                   translate <-l, 0, 0>}
    object {FrameTick(-l,YaxisTexture,YaxisTextureNT) scale <.5,1,1> rotate <0,  0,90> translate < 0,-l, 0>}
    object {FrameTick(-l,ZaxisTexture,ZaxisTextureNT) scale <.5,1,1> rotate <0,-90, 0> translate < 0, 0,-l>}
    #local k=k+1;
  #end
}

// Frame 2D
#declare frame2D=union {
  union {
    cylinder {<50,0,0>,<-50,  0,  0> .005 texture {XaxisTexture}}
    cylinder {<0,50,0>,<  0,-50,  0> .005 texture {YaxisTexture}}
    }
  sphere   {<0,0,0>,.001 pigment { color 1}}


  #local k=0;

  #while (k<10)
  #local n = 1;
  #while (n <10)
    #local l=k*10+n;
    object {FrameTick( l,XaxisTexture,XaxisTextureNT)                            translate < l, 0, 0>}
    object {FrameTick( l,YaxisTexture,YaxisTextureNT)          rotate <0,  0,90> translate < 0, l, 0>}
    object {FrameTick(-l,XaxisTexture,XaxisTextureNT) scale .5                   translate <-l, 0, 0>}
    object {FrameTick(-l,YaxisTexture,YaxisTextureNT) scale .5 rotate <0,  0,90> translate < 0,-l, 0>}
    #local n = n + 1;
  #end
    #local l=k*10+n;
    object {FrameTick( l,XaxisTexture,XaxisTextureNT) scale < 1,2,2>                   translate < l, 0, 0>}
    object {FrameTick( l,YaxisTexture,YaxisTextureNT) scale < 1,2,2> rotate <0,  0,90> translate < 0, l, 0>}

    object {FrameTick(-l,XaxisTexture,XaxisTextureNT) scale <.5,1,1>                   translate <-l, 0, 0>}
    object {FrameTick(-l,YaxisTexture,YaxisTextureNT) scale <.5,1,1> rotate <0,  0,90> translate < 0,-l, 0>}
    #local k=k+1;
  #end
}

