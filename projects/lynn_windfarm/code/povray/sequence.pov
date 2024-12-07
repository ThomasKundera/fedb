// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------

#declare Windmill_base=union {
  cylinder {<0,0,0>,<0,0,1> .01 texture {XaxisTexture}}
  cylinder {<0,0,0>,<0,1,0> .01 texture {YaxisTexture}}
  cylinder {<0,0,0>,<1,0,0> .01 texture {ZaxisTexture}}
}

#macro Windmill (x_simple,y_simple,wangle)

#end