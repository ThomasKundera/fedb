#include "colors.inc"

#include "common.inc"
#include "frame.inc"

global_settings { ambient_light 2. }

#declare pos=1;

camera {
  location <-6,0,0>
  look_at  <0,0,0>
  right x*image_width/image_height
}

union {
    difference {
      sphere {<0,0,0>,2}
      plane {<1,0,0>,0}
      texture { pigment { color Red }}
    }
    difference {
      sphere {<0,0,0>,2}
      plane {<-1,0,0>,0}
      texture { pigment { color Green }}
    }
    #switch (pos)
      #case (0)
        rotate <0,90,0>
        #break
      #case (1)
        rotate <40,30,60>
        #break
    #end
}
  

light_source{<0,0,-10> color White} 
light_source{<0,0, 10> color White} 
light_source{<-10,0,0> color White} 

object {simpleframe scale .059 translate <0,0,0>}
