// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// common.inc


// 
#declare myFast=1;

// This may change according to what we want to model
#declare m =    1/10000;
// This wont change soon
#declare km=    m*1000;
#declare Mm=   km*1000; // 1000 km
#declare Gm=   Mm*1000; // 1000 000 km
#declare cm=    m/100;
#declare mm=    m/1000;
#declare um=   mm/1000;



// From: http://www.f-lohmueller.de/pov_tut/backgrnd/p_sky8f.htm
// Macro pour corriger les images
// pour image_map avec assumed_gamma = 1.0 ;
#macro Correct_Pigment_Gamma(Orig_Pig, New_G)
  #local Correct_Pig_fn =
      function{ pigment {Orig_Pig} }
  pigment{ average pigment_map{
   [function{ pow(Correct_Pig_fn(x,y,z).x, New_G)}
               color_map{[0 rgb 0][1 rgb<3,0,0>]}]
   [function{ pow(Correct_Pig_fn(x,y,z).y, New_G)}
               color_map{[0 rgb 0][1 rgb<0,3,0>]}]
   [function{ pow(Correct_Pig_fn(x,y,z).z, New_G)}
               color_map{[0 rgb 0][1 rgb<0,0,3>]}]
   }}
#end //
