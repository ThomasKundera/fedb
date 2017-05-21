// --------------------------------------------------------------------------------
// Simple retrograding example
// 
// --------------------------------------------------------------------------------

#include "common.inc"
#include "frame.inc"
#include "sun_simple.inc"
// For aesthetic
//#include "night_sky.inc"


//#declare TOPCAM=1;

// Animation stuff
#declare duration=100*d_t;                   // 20 days of observation
#declare timeOffset=-100*d_t;                // From -10 to 10 days (0 being the crossing)
#declare seconde=clock*duration+timeOffset;

global_settings { ambient_light .5 }

// Two objects rotating around a same center

// We dont pretend for a realistic Earth/whatever planet
// model yet, just respecting the principle.
#declare r1=100000*km;  // With default units, it makes 100
#declare r2=200000*km;

// relative rotation speed will follow Newton's laws:
// P=-mK/r²
// F= mv²/r
// P1(r1)=F1(r1)
// P2(r2)=F2(r2)
// -mK/r1²=mv1²/r1
// -mK/r2²=mv2²/r2
// -K/r1=v1² v1²r1=K
// -K/r2=v2² v2²r2=K
// v1²/v2²=r2/r1
// linear speed v=2*pi*r*vtheta
// r1²*vt1²/(r2²*vt2²)=r2/r1
// tv1²/tvt²=r2³/r1³
// tv1/tv2=\sqrt(r2³/r1³)

#declare vtheta1=2*pi/y_t;            // 1 revolutions per year
#declare vtheta2=sqrt(r1*r1*r1/(r2*r2*r2))*vtheta1; // respecting speed ratio

// t=0 : planets aligned with Sun
#declare theta1=seconde*vtheta1;
#declare theta2=seconde*vtheta2;

#declare planet1_pos=<r1*cos(theta1),0,r1*sin(theta1)>;
#declare planet2_pos=<r2*cos(theta2),0,r2*sin(theta2)>;

#declare planet1=sphere{ <0,0,0>,10000*km
	texture {
  		pigment{ rgb <1,0,0> }
  		finish {
     		ambient .5
	  		phong .7
  		}
	}
}


#declare planet2=sphere{<0,0,0>,10000*km
	texture {
  		pigment{ rgb <0,1,0> }
  		finish {
     		ambient .5
	  		phong .7
  		}
	}
}

#ifdef ( TOPCAM )
object {planet1 translate planet1_pos}
#else
#declare mysphere=sphere {<0,0,0>,1 hollow translate planet1_pos}
#end
object {planet2 translate planet2_pos}

//object {SunBall scale 20000*km}

#ifdef ( TOPCAM )
camera {
  location   <0,2*r2,0>
  look_at    <0,    0,0>
  sky        <0,    0,1>
  //angle 40 // 50mm
  angle      90
  right -x*image_width/image_height
}
#else
#declare camLoc=yCenter(mysphere);
camera {
  location   camLoc
  look_at    camLoc+<1,    0,0>
  sky        <0,    1,0>
  //angle 40 // 50mm
  angle      90
  right -x*image_width/image_height
}
#end

/*
*/

