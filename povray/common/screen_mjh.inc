// This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
// To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send a
// letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

//               Persistence of Vision Raytracer Version 3.7
//                           Screen Include File

// Created by Christoph Hormann, Chris Huff, Rune S. Johansen and Michael 
// Horvath.

// Screen.inc will enable you to place objects and textures right in front
// of the camera. One use of this is to place your signature or a logo in
// the corner of the image.

// You can use screen.inc with either a perspective or an orthographic
// camera. Screen.inc will automatically create the camera definition for 
// you when it is included.

// Note that even though objects aligned using screen.inc follow the
// camera, they are still part of the scene. That means that they will be
// affected by perspective, lighting, the surroundings etc.

// For instructions of use, look in the POV-Ray manual, and for an example
// of use, see screen.pov.

// Last updated: June 2019

// NOTES/TO DO
// * Camera_Zoom is ignored by Mode 2. Ideally you should be able to 
//   increase or decrease the scale of a render in both modes without it 
//   necessarily having an effect on other parameters such as Camera_Angle. 
//   However, changing this behavior would break old scenes. -mjh
// * Outputted Camera_Look_At is incorrect when using Mode 2 and an 
//   orthographic camera. Not sure if this can be fixed. Not sure if it is 
//   even possible to determine/calculate the look_at point when using 
//   Mode 2 and an perspective camera. (I was able to do so when when 
//   using Mode 2 and an orthographic camera, however.) -mjh
// * In my opinion, Camera_Angle and Camera_Zoom should ignore the camera's 
//   aspect ratio. Instead, Camera_Aspect_Ratio should IMO be handled 
//   elsewhere in the code. Altering this behavior could break old scenes,
//   however. -mjh
// * The crosshairs in the demo scene look very strange when using an 
//   orthographic camera. (In either Mode 1 or Mode 2, it doesn't matter.)
//   I have no idea why. -mjh

#ifndef (Screen_Inc_Temp)
#declare Screen_Inc_Temp = version;
#version 3.7;

#ifdef(View_POV_Include_Stack)
   #debug "including screen_mjh.inc\n"
#end

#include "transforms.inc"

#macro Update_Camera()
	#ifndef (Camera_Mode)			#declare Camera_Mode			= 1;						#end
	#ifndef (Camera_Orthographic)	#declare Camera_Orthographic	= false;					#end
	#ifndef (Camera_Aspect_Ratio)	#declare Camera_Aspect_Ratio	= image_width/image_height;	#end
	#ifndef (Camera_Location)		#declare Camera_Location		= <0,0,0,>;					#end
	#ifndef (Camera_Look_At) 		#declare Camera_Look_At			= <0,0,1,>;					#end
	#ifndef (Camera_Angle)	 		#declare Camera_Angle			= 67.380135;				#end
	#ifndef (Camera_Zoom)	 		#declare Camera_Zoom			= 1;						#end
	#ifndef (Camera_Sky)	  		#declare Camera_Sky				= +y;						#end
	#ifndef (Camera_Direction)		#declare Camera_Direction		= +z;						#end
	#ifndef (Camera_Right)			#declare Camera_Right			= +x;						#end
	#ifndef (Camera_Up)				#declare Camera_Up				= +y;						#end
	#ifndef (Camera_Transform)		#declare Camera_Transform		= transform{}				#end
	#ifndef (Camera_Transform_Mtx)	#declare Camera_Transform_Mtx	= transform{}				#end
	#ifndef (Camera_Transform_Dec)	#declare Camera_Transform_Dec	= transform{}				#end

	// Mode 1 - location, look_at, and angle
	#if (Camera_Mode = 1)
		#local CamL = Camera_Location;							// wherever you're putting it
		#local CamD = vnormalize(Camera_Look_At - CamL);		// direction of camera view
		#local CamR = vnormalize(vcross(Camera_Sky, CamD));		// to the right
		#local CamU = vnormalize(vcross(CamD, CamR));			// camera up
		#local CamW = vlength(Camera_Look_At - CamL)/Camera_Zoom;

		#if (Camera_Orthographic = true)
			#local CamR = CamR * CamW;
			#local CamU = CamU * CamW;
		#end

		#declare Camera_Direction	= CamD * Camera_Zoom;
		#declare Camera_Right		= CamR * Camera_Aspect_Ratio;
		#declare Camera_Up			= CamU;
	// Mode 2 - location, direction, right, and up
	#elseif (Camera_Mode = 2)
		#local CamU = Camera_Up;
		#local CamR = Camera_Right/Camera_Aspect_Ratio;
		#local CamD = Camera_Direction/Camera_Zoom;
		#local CamL = Camera_Location;
		#local CamW = vlength(CamR);
//		#local CamW = 44.399729;		// the optimal value for the demo scene is ~44.399729

		// this is currently only correct when orthographic mode is enabled, need to fix
		#declare Camera_Look_At = CamW * Camera_Direction + CamL;
	#end
/*
#declare Message_Count = 0;
#declare TVec = CamR/CamU;
#declare TVal = vlength(TVec);
Screen_Message(concat("CamU = (", vstr(3,CamU,	",",0,-1), ")"))
Screen_Message(concat("CamR = (", vstr(3,CamR,	",",0,-1), ")"))
Screen_Message(concat("CamD = (", vstr(3,CamD,	",",0,-1), ")"))
Screen_Message(concat("CamL = (", vstr(3,CamL,	",",0,-1), ")"))
Screen_Message(concat("CamW = ", str(CamW,			0,-1)))
Screen_Message(concat("TVec = (", vstr(3,TVec,	",",0,-1), ")"))
Screen_Message(concat("TVal = ", str(TVal,			0,-1)))
Screen_Message("")
*/
	#declare Camera_Transform_Mtx = transform
	{
		matrix
		<
			CamR.x, CamR.y, CamR.z,
			CamU.x, CamU.y, CamU.z,
			CamD.x, CamD.y, CamD.z,
			CamL.x, CamL.y, CamL.z
		>
	}

	#declare Camera_Transform = transform
	{
		transform {Camera_Transform_Mtx}
		transform {Camera_Transform_Dec}
	}

	camera
	{
		#if (Camera_Orthographic = true)
			orthographic
		#else
			perspective
		#end
		location	Camera_Location
		direction	Camera_Direction
		right		Camera_Right
		up			Camera_Up
		sky			Camera_Sky
		transform {Camera_Transform_Dec}
	}
#end

#macro Get_Screen_XY(Loc)
	#local temp_val = vinv_transform(Loc, Camera_Transform);
	#if (Camera_Orthographic = true)
		#local temp_val = <1/2 + temp_val.x/Camera_Aspect_Ratio, 1/2 - temp_val.y>;
	#else
		#local temp_val = <1/2 + temp_val.x/temp_val.z/Camera_Aspect_Ratio * Camera_Zoom, 1/2 - temp_val.y/temp_val.z * Camera_Zoom>;
	#end
	temp_val * <image_width, image_height>
#end
#macro Set_Camera_Location(Loc)
	#declare Camera_Location = Loc;
	Update_Camera()
#end
#macro Set_Camera_Look_At(LookAt)
	#declare Camera_Look_At = LookAt;
	Update_Camera()
#end
#macro Set_Camera_Aspect_Ratio(Aspect)
	#declare Camera_Aspect_Ratio = Aspect;
	Update_Camera()
#end
#macro Set_Camera_Aspect(Width,Height)
	#declare Camera_Aspect_Ratio = Width/Height;
	Update_Camera()
#end
#macro Set_Camera_Sky(Sky)
	#declare Camera_Sky = Sky;
	Update_Camera()
#end
#macro Set_Camera_Zoom(Zoom)
	// Camera_Angle is meant to be read-only, otherwise it will conflict with Camera_Zoom.
	#declare Camera_Angle = 2 * atand(Camera_Aspect_Ratio/Zoom/2);
	#declare Camera_Zoom = Zoom;
	Update_Camera()
#end
#macro Set_Camera_Angle(Angle)
	// Camera_Angle is meant to be read-only, otherwise it will conflict with Camera_Zoom.
	#declare Camera_Angle = Angle;
	#declare Camera_Zoom = 1/2/tand(Angle/2)*Camera_Aspect_Ratio;
	Update_Camera()
#end
#macro Set_Camera_Direction(Direction)
	#declare Camera_Direction = Direction;
	Update_Camera()
#end
#macro Set_Camera_Right(Right)
	#declare Camera_Right = Right;
	Update_Camera()
#end
#macro Set_Camera_Up(Up)
	#declare Camera_Up = Up;
	Update_Camera()
#end
#macro Set_Camera_Transform(Transform)
	#declare Camera_Transform_Dec = Transform;
	Update_Camera()
#end
#macro Set_Camera_Mode(Mode)
	#declare Camera_Mode = Mode;
	Update_Camera()
#end
#macro Set_Camera_Orthographic(Ortho)
	#declare Camera_Orthographic = Ortho;
	Update_Camera()
#end
#macro Set_Camera(Location, LookAt, Angle)
	#declare Camera_Mode = 1;
	#declare Camera_Location = Location;
	#declare Camera_Look_At = LookAt;
	Set_Camera_Angle(Angle)
	Update_Camera()
#end
#macro Set_Camera_Alt(Location, Direction, Right, Up)
	#declare Camera_Mode = 2;
	#declare Camera_Location = Location;
	#declare Camera_Direction = Direction;
	#declare Camera_Right = Right;
	#declare Camera_Up = Up;
	Set_Camera_Zoom(vlength(Direction))	
	Update_Camera()
#end
#macro Reset_Camera()
	#undef Camera_Mode
	#undef Camera_Orthographic
	#undef Camera_Location
	#undef Camera_Aspect_Ratio
	#undef Camera_Location
	#undef Camera_Look_At
	#undef Camera_Angle
	#undef Camera_Sky
	#undef Camera_Zoom
	#undef Camera_Direction
	#undef Camera_Right
	#undef Camera_Up
	Update_Camera()
#end
#macro Screen_Object(Object, Position, Spacing, Confine, Scaling)
	#local Obj_Max = max_extent(Object);
	#local Obj_Min = min_extent(Object);
	#local Obj_Cen = (Obj_Max + Obj_Min)/2;
	#local Obj_Dim = (Obj_Max - Obj_Min)/2;
	#local Pos = (Position - 1/2) * 2;
	#local Pos =
	(
		+ <Pos.x*Camera_Aspect_Ratio/2,Pos.y/2,Camera_Zoom>
		+ (0 - Obj_Cen - Pos * (Obj_Dim + Spacing)) * Confine
	);
	object
	{
		Object
		translate	Pos
		#if (Camera_Orthographic = true)
			translate	+z * Scaling
		#else
			scale		Scaling
		#end
		transform {Camera_Transform}
		no_shadow			// shouldn't cast shadows in the scene
		no_reflection		// shouldn't be reflected in scene elements
		no_radiosity		// also make the object invisible to radiosity rays
	}
#end
#macro Screen_Plane(Texture, Scaling, BLCorner, TRCorner)
	box
	{
		<-0.000001,-0.000001,0>, <+1.000001,+1.000001,0>
		texture {Texture}
		scale		TRCorner * <1,1,0> - BLCorner * <1,1,0> + z
		translate	BLCorner * <1,1,0> + <-1/2,-1/2,0>
		scale		<Camera_Aspect_Ratio,1,1>
		translate	+z * Camera_Zoom
		#if (Camera_Orthographic = true)
			translate	+z * Scaling
		#else
			scale		Scaling
		#end
		transform {Camera_Transform}
		hollow		on		// for media/fog
		no_shadow			// shouldn't cast shadows in the scene
		no_reflection		// shouldn't be reflected in scene elements
		no_radiosity		// also make the object invisible to radiosity rays
	}
#end
#declare Message_Count = 0;
#macro Screen_Message(Message)
	// All these parameters should be made configurable from outside the macro.
	#local Font_Size = 0.02;
	#local Font_Color = <1,0,1>*3/4;
	#local Text_Position = <0,1>;
	#local Text_Object = text
	{
		ttf "crystal.ttf", Message, 0.01, <0,0>
		pigment {color srgb Font_Color}
		finish {emission 1 diffuse 0}
		scale Font_Size
	}
	Screen_Object(Text_Object, Text_Position, <Font_Size/2,Font_Size/2 + Message_Count * Font_Size>, true, 0.01)
	#debug concat(Message, "\n")
	#declare Message_Count = Message_Count + 1;
#end

Update_Camera()

#version Screen_Inc_Temp;
#end
