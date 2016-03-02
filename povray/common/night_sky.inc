// Persistence Of Vision Ray Tracer Scene Description File
// --------------------------------------------------------------------------------
// night_sky.inc



#declare skyPigment=pigment {
  image_map {
    jpeg "data/TychoSkymapII.t5_08192x04096.jpg"
    map_type 1
  }
}
  

sky_sphere{
   Correct_Pigment_Gamma(pigment {skyPigment},2.2)
}