// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// localcommon.inc

#include "colors.inc"
#include "textures.inc"
#include "functions.inc"

#include "common.inc"
#include "frame.inc"
#include "sun_simple.inc"


global_settings { ambient_light 1 }

#declare myBrushedAlu=texture {
    Chrome_Metal
    normal {
        bumps -.5
        scale <1, 0.01, 0.01>
    }
    scale .001
}

#declare r=1000;

#declare SunTextureFast=texture {
  pigment{
    rgb <2.12,1.7,0.47>
  }
  finish {
     specular 0.9 roughness 0.02
     ambient 1
  }
  
}

#declare SunBall=sphere {<0,0,0>,1 texture {SunTextureFast} no_shadow scale r}

#declare SunLightSource=light_source {
    <0, 0, 0>
    color <1000,600,600>
    looks_like { SunBall }
    parallel
    point_at <0,r*1.00001,0>
  }

//object {SunLightSource scale r translate <0,r,100*r> rotate <-1,0,0>}


light_source {
    <0,r*2.5,100*r>
    color <1.5,1,1>
    looks_like { SunBall }
    parallel
    point_at <0,r*1.00001,0>
}

camera {
  location   <0,r*1.00001,0>
  look_at    <0,r*1.00001,r>
  sky        <0,1,0>
  angle 40 // 50mm
  right -x*image_width/image_height
}

// From http://povray.tashcorp.net/tutorials/qd_realskysphere/pass3.pov
// Create an infinite sphere around scene and allow any pigment on it
sky_sphere {
    pigment {
        function { max(min(y+.015,1),0) }
        color_map {
            [  0/269 color rgb <120/255, 79/255, 51/255>]
            [  1/269 color rgb <141/255, 83/255, 46/255>]
            [  2/269 color rgb <177/255, 86/255, 41/255>]
            [  3/269 color rgb <235/255,128/255, 72/255>]
            [  5/269 color rgb <255/255,159/255, 72/255>]
            [  8/269 color rgb <255/255,203/255, 94/255>] // New
            [ 10/269 color rgb <255/255,218/255,112/255>]
            [ 13/269 color rgb <255/255,233/255,148/255>] // New
            [ 15/269 color rgb <251/255,241/255,172/255>] // New
            [ 20/269 color rgb <255/255,246/255,203/255>]
            [ 30/269 color rgb <255/255,240/255,219/255>]
            [ 40/269 color rgb <236/255,223/255,214/255>]
            [ 50/269 color rgb <205/255,204/255,212/255>]
            [ 55/269 color rgb <185/255,190/255,209/255>] // New
            [ 60/269 color rgb <166/255,176/255,201/255>]
            [ 65/269 color rgb <149/255,163/255,190/255>] // New
            [ 70/269 color rgb <129/255,149/255,182/255>]
            [ 80/269 color rgb <103/255,127/255,171/255>]
            [ 90/269 color rgb < 79/255,110/255,154/255>]
            [100/269 color rgb < 66/255, 97/255,143/255>]
            [110/269 color rgb < 52/255, 84/255,131/255>]
            [120/269 color rgb < 47/255, 75/255,122/255>]
            [140/269 color rgb < 37/255, 60/255,102/255>]
            [160/269 color rgb < 32/255, 51/255, 84/255>]
            [180/269 color rgb < 27/255, 42/255, 71/255>]
            [200/269 color rgb < 25/255, 36/255, 58/255>]
            [220/269 color rgb < 22/255, 31/255, 48/255>]
            [240/269 color rgb < 18/255, 27/255, 42/255>]
            [260/269 color rgb < 15/255, 21/255, 33/255>]
            [269/269 color rgb < 15/255, 21/255, 33/255>]
        }
    }
    scale (1/2)
}
