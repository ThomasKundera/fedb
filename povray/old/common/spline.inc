/*************************************************************************
             SPLINE MACRO FILE FOR PERSISTENCE OF VISION 3.5
**************************************************************************

Created by Chris Colefax, 31 August 1999
Last Updated 6 March 2003

See "QUICKREF.TXT" for more information

*************************************************************************/

#ifndef (debug_progress) #declare debug_progress = false; #end

// INTERNAL SPLINE MACROS
// ***********************************************************************
   #macro atan3 (sV1, sV2) #if (sV1=0 & sV2=0) #local sR = 0; #else #local sR = atan2(sV1, sV2); #end (degrees(sR)) #end
   #macro vequal (sV1, sV2) #local sVC1 = <0,0,0>+sV1; #local sVC2 = <0,0,0>+sV2; (sVC1.x=sVC2.x & sVC1.y=sVC2.y & sVC1.z=sVC2.z) #end
   #macro vzero (sV) #local sVC1 = <0,0,0>+sV; (sVC1.x=0 & sVC1.y=0 & sVC1.z=0) #end

// TCB: Dir = 1 for outgoing, -1 for incoming
   #macro _SP_TCB (Prev, Cur, Next, Dir) ((1-_SP_tens)*((1-_SP_cont*Dir)*(1+_SP_bias)*(Cur-Prev) + (1+_SP_cont*Dir)*(1-_SP_bias)*(Next-Cur))/2) #end

// Returns clock required to give a certain distance or distance fraction (if sDist < 0) along spline length (and modifies sDist to be distance at returned clock value)
   #macro _SP_evenclock (sDist)
      #local sC = (sDist < 0 ? -sDist : sDist/_SP[0][3]); #local sC = (sC=1 ? 1 : sC - floor(sC));
      #switch (sC)
      #case (0) #declare sDist = 0; #break
      #case (1) #declare sDist = _SP[0][3]; #break
      #else #declare sDist = sC*_SP[0][3]; #if (!(_SP[0][5]=0 & _SP[0][6]=0))
         #if (_SP[0][5]=0) #local sIdx = 1; #local sSmp = int(sC*(_SP[0][1]-1));
            #else #local sIdx = 6; #local sSmp = int(sC*_SP[0][5]); #end
         #while (sDist < _SP[sIdx][sSmp].y) #local sSmp = sSmp - 1; #end
         #while (sDist > _SP[sIdx][sSmp+1].y) #local sSmp = sSmp + 1; #end
         #local sDif = (_SP[sIdx][sSmp+1] - _SP[sIdx][sSmp]);
         #local sC = (_SP[sIdx][sSmp].x + (sDist - _SP[sIdx][sSmp].y)*sDif.x/sDif.y); #end
      #end
      (sC)
   #end

   #macro _SP_value (sC)
      #if (sC = 1) #local sS = _SP[0][1]-2; #local sT = 1; #else
         #local sS = int(sC*(_SP[0][1]-1));
         #while (sC < _SP[1][sS].x) #local sS = sS - 1; #end
         #while (sC > _SP[1][sS+1].x) #local sS = sS + 1; #end
         #local sT = (sC - _SP[1][sS].x)/(_SP[1][sS+1].x - _SP[1][sS].x);
      #end
      (_SP[2][sS] + sT*(_SP[3][sS] + sT*(_SP[4][sS] + sT*_SP[5][sS])))
   #end

   #macro spline_points (_SP)      (_SP[0][1]) #end
   #macro spline_looping (_SP)     (_SP[0][2]) #end
   #macro spline_length (_SP)      (_SP[0][3]) #end
   #macro spline_hull_length (_SP) (_SP[0][4]) #end

   #macro spline_value (_SP, sC) (_SP_value ((sC = 1 ? 1 : sC - floor(sC)))) #end
   #macro even_spline_value (_SP, sDist) #local sC = _SP_evenclock(sDist); (_SP_value (sC)) #end

// SPLINE OPTION MACROS: SPLINE CREATION
// ***********************************************************************
   #declare default_options       = 0;
   #declare create_default_spline = 0;
   #declare create_cubic_spline   = 1;
   #declare create_bezier_spline  = 2;
   #declare create_hermite_spline = 3;

   #macro spline_loop (Toggle)       #declare _SP_loop = Toggle; 0 #end
   #macro spline_tension (Amount)    #declare _SP_tens = Amount; 0 #end
   #macro spline_bias (Amount)       #declare _SP_bias = Amount; 0 #end
   #macro spline_continuity (Amount) #declare _SP_cont = Amount; 0 #end
   #macro spline_TCB (T, sI, B)       #declare _SP_tens = T; #declare _SP_cont = sI; #declare _SP_bias = B; 0 #end

   #macro fit_spline_length (Amount)   #declare _SP_fitlength = Amount; 0 #end
   #macro fit_spline_accuracy (Amount) #declare _SP_fitacc    = Amount; 0 #end

   #macro uniform_spline_times (Toggle) #declare _SP_unitimes  = Toggle; 0 #end
   #macro spline_sampling (Amount)      #declare _SP_sampling  = Amount; 0 #end
   #macro spline_cache_file (String)    #declare _SP_file      = String  0 #end
   #macro spline_file_points (Number)   #declare _SP_points    = Number; 0 #end
   #macro spline_scale (Amount)         #declare _SP_scale     = Amount; 0 #end
   #macro spline_rotate (Amount)        #declare _SP_rotate    = Amount; 0 #end
   #macro spline_translate (Amount)     #declare _SP_translate = Amount; 0 #end

// SPLINE OPTION MACROS: SPLINE USAGE
// ***********************************************************************
   #macro spline_radius (Amount)           #declare _SP_radius       = Amount;  0 #end
   #macro spline_accuracy (Amount)         #declare _SP_prevcount    = Amount;  0 #end
   #macro show_spline_points (Toggle)      #declare _SP_prevpoints   = Toggle;  0 #end
   #macro show_spline_hull (Toggle)        #declare _SP_prevhull     = Toggle;  0 #end
   #macro show_spline_tangents (Toggle)    #declare _SP_prevtangents = Toggle;  0 #end
   #macro spline_preview_pigment (Pigment) #declare _SP_prevpigment  = Pigment  0 #end
   #macro spline_preview_finish (Finish)   #declare _SP_prevfinish   = Finish   0 #end
   #macro spline_connected (Toggle)        #declare _SP_prevcyls     = Toggle;  0 #end

   #macro even_spline_spacing (Toggle) #declare _SP_evenspace  = Toggle; 0 #end
   #macro spline_clock (Amount)        #declare _SP_useclock   = Amount; 0 #end
   #macro auto_banking (Amount)        #declare _SP_autobank   = Amount; 0 #end
   #macro auto_rotate (Amount)         #declare _SP_autorot    = Amount; 0 #end
   #macro max_banking_angle (Amount)   #declare _SP_maxbanking = Amount; 0 #end
   #macro direction_foresight (Amount) #declare _SP_dforesight = Amount; 0 #end
   #macro banking_foresight (Amount)   #declare _SP_bforesight = Amount; 0 #end

   #macro spline_portion (Start, Finish) #declare _SP_start      = Start; #declare _SP_finish = Finish; 0 #end
   #macro spline_steps (Number)          #declare _SP_steps      = Number; 0 #end
   #macro spline_step_size (Amount)      #declare _SP_stepsize   = Amount; 0 #end
   #macro spline_step_twist (Amount)     #declare _SP_steptwist  = Amount; 0 #end
   #macro spline_total_twist (Amount)    #declare _SP_totaltwist = Amount; 0 #end
   #macro spline_normal_sky (Vector)     #declare _SP_normsky    = Vector; 0 #end

// UNDEFINE GLOBAL OPTIONS (CREATED WITH ABOVE OPTION MACROS)
// ***********************************************************************
   #macro _SP_undefine ()
   #ifdef (_SP_loop) #undef _SP_loop #end             #ifdef (_SP_tens) #undef _SP_tens #end             #ifdef (_SP_bias) #undef _SP_bias #end             #ifdef (_SP_cont) #undef _SP_cont #end
   #ifdef (_SP_fitlength) #undef _SP_fitlength #end   #ifdef (_SP_fitacc) #undef _SP_fitacc #end         #ifdef (_SP_unitimes) #undef _SP_unitimes #end     #ifdef (_SP_sampling) #undef _SP_sampling #end
   #ifdef (_SP_file) #undef _SP_file #end             #ifdef (_SP_points) #undef _SP_points #end         #ifdef (_SP_start) #undef _SP_start #end           #ifdef (_SP_finish) #undef _SP_finish #end
   #ifdef (_SP_steps) #undef _SP_steps #end           #ifdef (_SP_stepsize) #undef _SP_stepsize #end     #ifdef (_SP_steptwist) #undef _SP_steptwist #end   #ifdef (_SP_totaltwist) #undef _SP_totaltwist #end
   #ifdef (_SP_autorot) #undef _SP_autorot #end       #ifdef (_SP_normsky) #undef _SP_normsky #end       #ifdef (_SP_radius) #undef _SP_radius #end         #ifdef (_SP_evenspace) #undef _SP_evenspace #end
   #ifdef (_SP_useclock) #undef _SP_useclock #end     #ifdef (_SP_scale) #undef _SP_scale #end           #ifdef (_SP_rotate) #undef _SP_rotate #end         #ifdef (_SP_translate) #undef _SP_translate #end
   #end

// CREATE SPLINE BY FIRST READING POINTS FROM A FILE
// ***********************************************************************
   #macro create_spline_from_file (FileName, Options)
      #if (debug_progress) #debug concat("\nSPLINE.MCR: Reading points from file \"", FileName, "\"...") #end
      #ifdef (_SP_points) #local sPC = _SP_points #else #local sPC = 1000; #end

      #fopen sFile FileName read #local sPL = array[sPC]
      #local sI = 0; #while (defined(sFile) & sI < sPC) #read (sFile, sV) #local sPL[sI] = sV; #local sI = sI + 1; #end
      #ifdef (sFile) #fclose sFile #end
      #declare sPC = sI; #local _SP_fromfile = true;
      #if (debug_progress) #debug "Done!\n" #end

      create_spline (sPL, Options)
   #end

// MAIN SPLINE CREATION MACRO
// ***********************************************************************
   #macro create_spline (PointArray, Options)
      #if (debug_progress) #debug "\nSPLINE.MCR: Creating spline: " #end

      // LOAD SPLINE FROM CACHE IF AVAILABLE
      #local sLoaded = false; #ifdef (_SP_file)
         #if (file_exists(_SP_file))
            #if (debug_progress) #debug concat("Loading from file \"", _SP_file, "\"...") #end
            #include _SP_file #declare sLoaded = true; #end #end
      #if (!sLoaded)

      // GET POINT COUNT, FIRST POINT, POINT INTERVALS
      #ifndef (_SP_fromfile) #local sPC = dimension_size(PointArray,1); #end
      #switch (Options)
      #case (create_cubic_spline)   #declare sPC = sPC-2;            #if (sPC < 2) #error "Cubic splines must have at least 4 points!" #end   #local sFP = 1; #local sPI = 1; #break
      #case (create_bezier_spline)  #declare sPC = int((sPC-1)/3)+1; #if (sPC < 2) #error "Bezier splines must have at least 4 points!" #end  #local sFP = 0; #local sPI = 3; #break
      #case (create_hermite_spline) #declare sPC = int(sPC/2);       #if (sPC < 2) #error "Hermite splines must have at least 4 points!" #end #local sFP = 0; #local sPI = 2; #break
      #else                                                          #if (sPC < 3) #error "Splines must have at least 3 points!" #end         #local sFP = 0; #local sPI = 1; #end

      // CHECK OPTIONS AND ASSIGN DEFAULTS
      #ifdef (_SP_loop) #local sLoop = (_SP_loop=false ? 0 : 1);
         #else #if (vequal(PointArray[sFP], PointArray[sFP + (sPC-1)*sPI])) #local sLoop = 1; #declare sPC = sPC - 1;
         #else #local sLoop = 0; #end #end
      #ifndef (_SP_sampling) #local sSamples = 0; #else #local sSampPerSeg = int(10*_SP_sampling); #local sSamples = (sSampPerSeg < 2 ? 0 : sSampPerSeg*(sPC+sLoop-1)); #end
      #ifndef (_SP_unitimes) #local _SP_unitimes = false; #end
      #ifndef (_SP_tens) #local _SP_tens = 0; #end
      #ifndef (_SP_cont) #local _SP_cont = 0; #end
      #ifndef (_SP_bias) #local _SP_bias = 0; #end

      // LOOP TO ADJUST TENSION FOR DESIRED LENGTH
      #ifdef (_SP_fitlength)
         #ifndef (_SP_fitacc) #local _SP_fitacc = _SP_fitlength/100; #end
         #if (_SP_tens = 1) #declare _SP_tens = 0; #end
      #end
      #local _SP_recalc = 1; #while (_SP_recalc > 0)

      // SAVE CONTROL POINTS INTO NEW ARRAY
      #if (debug_progress) #debug concat("\n    Getting control points (", str(sPC, 0, 0), ") and tangents...") #end
      #local _SP = array[(sSamples=0 ? 6 : 7)] #declare _SP[2] = array[sPC + sLoop]
      #local sI = 0; #while (sI < sPC) #declare _SP[2][sI] = PointArray[sFP + sI*sPI]; #local sI = sI + 1; #end
      #if (sLoop) #declare _SP[2][sI] = PointArray[sFP]; #declare sPC = sPC + 1; #end

      // SAVE TANGENTS INTO ARRAY:
      #declare _SP[3] = array[sPC-1] #declare _SP[4] = array[sPC-1] #declare _SP[5] = array[sPC-1]
      #switch (Options)

      // SET TANGENTS DIRECTLY
      #case (create_hermite_spline)
         #declare _SP[3][0] = PointArray[1]*(1-_SP_tens)*(1+_SP_bias);
         #local sI = 1; #while (sI < sPC-1)
            #declare _SP[3][sI] = PointArray[sI*2+1]*(1-_SP_tens)*(1+_SP_bias);
            #declare _SP[4][sI-1] = PointArray[sI*2+1]*(1-_SP_tens)*(1-_SP_bias);
         #local sI = sI + 1; #end 
         #if (sLoop) #declare _SP[4][sPC-2] = PointArray[1]*(1-_SP_tens)*(1-_SP_bias);
            #else #declare _SP[4][sI-1] = PointArray[sI*2+1]*(1-_SP_tens)*(1-_SP_bias); #end
         #break

      // SET TANGENTS FROM BEZIER HULL
      #case (create_bezier_spline)
         #declare _SP[3][0] = (PointArray[1]-PointArray[0])*3*(1-_SP_tens)*(1+_SP_bias);
         #local sI = 1; #while (sI < sPC-1-sLoop)
            #declare _SP[3][sI] = (PointArray[sI*3+1]-PointArray[sI*3])*3*(1-_SP_tens)*(1+_SP_bias);
            #declare _SP[4][sI-1] = (PointArray[sI*3]-PointArray[sI*3-1])*3*(1-_SP_tens)*(1-_SP_bias);
         #local sI = sI + 1; #end
         #declare _SP[4][sI-1] = (PointArray[sI*3]-PointArray[sI*3-1])*3*(1-_SP_tens)*(1-_SP_bias);
         #if (sLoop)
            #declare _SP[3][sPC-2] = (PointArray[sI*3]-PointArray[sI*3-1])*3*(1-_SP_tens)*(1+_SP_bias);
            #declare _SP[4][sPC-2] = (PointArray[1]-PointArray[0])*3*(1-_SP_tens)*(1-_SP_bias);
         #end #break

      // CALCULATE TANGENTS, WITH FIRST AND LAST SET BY EXTRA POINTS
      #case (create_cubic_spline)
         #declare _SP[3][0] = _SP_TCB(PointArray[0], _SP[2][0], _SP[2][1], 1);
         #local sI = 1; #while (sI < sPC-1-sLoop)
            #declare _SP[3][sI] = _SP_TCB(_SP[2][sI-1], _SP[2][sI], _SP[2][sI+1], 1);
            #declare _SP[4][sI-1] = _SP_TCB(_SP[2][sI-1], _SP[2][sI], _SP[2][sI+1], -1);
         #local sI = sI + 1; #end
         #declare _SP[4][sI-1] = _SP_TCB(_SP[2][sI-1], _SP[2][sI], PointArray[sI+2], -1);
         #if (sLoop)
            #declare _SP[3][sPC-2] = _SP_TCB(_SP[2][sPC-3], _SP[2][sPC-2], PointArray[sPC], 1);
            #declare _SP[4][sPC-2] = _SP_TCB(PointArray[0], _SP[2][sPC-1], _SP[2][1], -1);
         #end #break

      // CALCULATE ALL TANGENTS WHEN NONE SPECIFIED
      #else
         #local sI = 1; #while (sI < sPC-1)
            #declare _SP[3][sI] = _SP_TCB(_SP[2][sI-1], _SP[2][sI], _SP[2][sI+1], 1);
            #declare _SP[4][sI-1] = _SP_TCB(_SP[2][sI-1], _SP[2][sI], _SP[2][sI+1], -1);
         #local sI = sI + 1; #end
         #if (sLoop)
            #declare _SP[3][0] = _SP_TCB(_SP[2][sPC-2], _SP[2][0], _SP[2][1], 1);
            #declare _SP[4][sPC-2] = _SP_TCB(_SP[2][sPC-2], _SP[2][sPC-1], _SP[2][1], -1);
         #else
            #declare _SP[3][0] = _SP_TCB(_SP[2][0] + _SP[2][2]-_SP[2][1], _SP[2][0], _SP[2][1], 1);
            #declare _SP[4][sPC-2] = _SP_TCB(_SP[2][sPC-2], _SP[2][sPC-1], _SP[2][sPC-1] + _SP[2][sPC-3] - _SP[2][sPC-2], -1);
         #end
      #end

      // TRANSFORM SPLINE POINTS AND TANGENTS
      #if (defined(_SP_scale) | defined(_SP_rotate) | defined(_SP_translate))
      #if (debug_progress) #debug "Done!\n    Transforming spline..." #end
         #ifndef (_SP_scale) #local _SP_scale = 1; #end
         #ifndef (_SP_rotate) #local _SP_rotate = 0; #end
         #ifndef (_SP_translate) #local _SP_translate = 0; #end
         #local sI = 0; #while (sI < sPC-1)
            #declare _SP[2][sI] = vrotate(_SP[2][sI]*_SP_scale, _SP_rotate) + _SP_translate;
            #declare _SP[3][sI] = vrotate(_SP[3][sI]*_SP_scale, _SP_rotate);
            #declare _SP[4][sI] = vrotate(_SP[4][sI]*_SP_scale, _SP_rotate);
         #local sI = sI + 1; #end
         #declare _SP[2][sI] = vrotate(_SP[2][sI]*_SP_scale, _SP_rotate) + _SP_translate;
      #end

      // SAVE TIMES AND APPROXIMATED SEGMENT LENGTHS INTO ARRAY
      #if (debug_progress) #debug "Done!\n    Getting control times..." #end
      #declare _SP[1] = array[sPC] #declare _SP[1][0] = <0, 0, 0>; #local sHullLength = 0;
      #local sI = 0; #while (sI < sPC-1)
         #local sSegHull = vlength(_SP[2][sI+1] - _SP[2][sI]); #local sHullLength = sHullLength + sSegHull;
         #local sSegLength = .5*(sSegHull + vlength(_SP[3][sI])/3 + vlength(_SP[4][sI])/3 + vlength((_SP[2][sI+1]-(_SP[4][sI]/3)) - (_SP[2][sI]+(_SP[3][sI]/3))));
         #declare _SP[1][sI+1] = _SP[1][sI] + <(_SP_unitimes ? 1 : sSegLength), sSegLength, 0>;
      #local sI = sI + 1; #end
      #if (_SP[1][sI].x = 0) #declare _SP[1][sI] = _SP[1][sI] + x; #end

      // NORMALIZE SPLINE TIMES FROM RANGE 0 TO 1
      #local sI = 1; #while (sI < sPC-1) #declare _SP[1][sI] = <_SP[1][sI].x/_SP[1][sPC-1].x, _SP[1][sI].y, 0>; #local sI = sI + 1; #end
      #local sLength = _SP[1][sI].y; #declare _SP[1][sI] = <1, sLength, 0>;

      // GET SPLINE COEFFICIENTS
      #if (debug_progress) #debug "Done!\n    Precalculating spline coefficients..." #end
      #local sS = 0; #while (sS < sPC-1)
         #declare _SP[5][sS] = (2*_SP[2][sS] - 2*_SP[2][sS+1] +   _SP[3][sS] + _SP[4][sS]);
         #declare _SP[4][sS] = (3*_SP[2][sS+1] - 3*_SP[2][sS] - 2*_SP[3][sS] - _SP[4][sS]);
      #declare sS = sS + 1; #end

      // SAVE SAMPLED SPLINE LENGTHS INTO ARRAY
      #if (sSamples > 0)
         #if (debug_progress) #debug concat("Done!\n    Sampling spline (", str(sSamples, 0, 0), " samples)...") #end
         #declare _SP[6] = array[sSamples+1] #declare _SP[6][0] = <0, 0, 0>;
         #local pPos = _SP[2][0]; #local sLength = 0;
         #local sS = 0; #while (sS < sPC-1)
            #local sI = (sS=0 ? 1 : 0); #while (sI < sSampPerSeg + (sS=sPC-2 ? 1 : 0))
               #local sT = sI/sSampPerSeg;
               #local sC = _SP[1][sS].x + sT*(_SP[1][sS+1].x-_SP[1][sS].x);
               #local sPos = _SP[2][sS] + sT*(_SP[3][sS] + sT*(_SP[4][sS] + sT*_SP[5][sS]));
               #local sLength = sLength + vlength(sPos-pPos);
               #declare _SP[6][sS*sSampPerSeg + sI] = <sC, sLength, 0>;
            #local pPos = sPos; #local sI = sI + 1; #end
         #local sS = sS + 1; #end
      #end

      // SAVE GENERAL SPLINE PROPERTIES
      #declare _SP[0] = array[7] {0, sPC, sLoop, sLength, sHullLength, sSamples, _SP_unitimes}

      // LOOP TO ADJUST TENSION FOR DESIRED LENGTH
      #ifdef (_SP_fitlength)
         #if (_SP_fitlength < sHullLength)
            #warning concat("SPLINE.MCR: The desired spline length you specified is shorter than the minimum hull length!  The spline is ", str(sLength, 0, 4), " units long.\n")
            #declare _SP_recalc = 0;
         #else
            #local sAccuracy = sLength - _SP_fitlength;
            #if (debug_progress) #debug concat("Done!\n    Tension = ", str(_SP_tens, 0, 4), ", Length = ", str(sLength, 0, 4), ", Accuracy = ", str(sAccuracy, 0, 4), " units...") #end
            #if (abs(sAccuracy) <= abs(_SP_fitacc))
               #declare _SP_recalc = 0;
            #else
               #declare _SP_tens = 1 - _SP_tens;
               #if (_SP_recalc = 1) #local _SP_exp = 1.5; #else #local _SP_exp = log((sLength - sHullLength)/_SP_len1) / log (_SP_tens/_SP_tens1); #end
               #local _SP_tens1 = _SP_tens; #local _SP_len1 = sLength - sHullLength;
               #local _SP_coeff = _SP_len1 / pow(_SP_tens1, _SP_exp);
               #declare _SP_tens = pow((_SP_fitlength - sHullLength)/_SP_coeff, 1/_SP_exp);
               #declare _SP_tens = 1 - _SP_tens;
               #if (debug_progress) #debug "\n\n    Recalculating spline:" #end
               #declare _SP_recalc = _SP_recalc + 1;
            #end
         #end
      #else #declare _SP_recalc = 0; #end
      #end

      // SAVE SPLINE TO CACHE FILE
      #ifdef (_SP_file)
         #if (debug_progress) #debug concat("Done!\n    Saving spline to file \"", _SP_file, "\"...") #end
         #fopen sFile _SP_file write
         #write (sFile, "// Spline Cache File, created by SPLINE.MCR: this file may be deleted when finished rendering\n")
         #local sMC = dimension_size(_SP, 1); #write (sFile, "array[", str(sMC, 0, 0), "] {\n")
         #local sI = 0; #while (sI < sMC) #local sMC2 = dimension_size (_SP[sI], 1);
            #write (sFile, "array[", str(sMC2, 0, 0), "] {")
            #local sI2 = 0; #while (sI2 < sMC2) #write (sFile, _SP[sI][sI2]) #if (sI2 < sMC2-1) #write (sFile, ",") #end #local sI2 = sI2 + 1; #end
            #write (sFile "}")
         #if (sI < sMC-1) #write (sFile, ",\n") #end #local sI = sI + 1; #end
         #write (sFile "}\n") #fclose sFile
      #end

      // RETURN DEFINED SPLINE ARRAY
      _SP #end
      _SP_undefine () #if (debug_progress) #debug "Done!\n" #end
   #end


// SPLINE PREVIEW MACROS
// ***********************************************************************
   #macro preview_spline (_SP, Options)
      #local sPC = _SP[0][1];
      #ifdef (_SP_steps) #local sSteps = max(int(_SP_steps), sPC*3);
      #else #ifndef (_SP_prevcount) #local _SP_prevcount = 1; #end
         #local sSteps = (_SP_prevcount < .3 ? 0 : int(10*_SP_prevcount*(sPC-1))); #end
      #ifndef (_SP_radius)       #local _SP_radius       = spline_length(_SP)/(sSteps=0 ? 1000 : sSteps*10); #end
      #ifndef (_SP_prevcyls)     #local _SP_prevcyls     = true; #end
      #ifndef (_SP_prevpoints)   #local _SP_prevpoints   = true; #end
      #ifndef (_SP_prevhull)     #local _SP_prevhull     = (sSteps ? false : true); #end
      #ifndef (_SP_prevtangents) #local _SP_prevtangents = _SP_prevhull; #end
      #ifndef (_SP_prevfinish)   #local _SP_prevfinish   = finish {ambient .5 diffuse 1} #end

   #if (debug_progress) #debug "\nSPLINE.MCR: Previewing spline" #if (sSteps > 0) #debug concat(" (", str(sSteps, 0, 0), " points)") #end #debug "..." #end
   union {
   #local sColour = <1, 0, 0>; #local sS = 0; #while (sS < sPC)

   // SHOW SPLINE POINTS, TANGENTS, HULL
   #if (_SP_prevpoints) sphere {_SP[2][sS], _SP_radius*1.5 pigment {rgb <1, 1, 0>} finish {_SP_prevfinish}} #end
   #if (sS < sPC-1)
      #if (_SP_prevtangents)
         #local sTangent = _SP[3][sS] + 2*_SP[4][sS] + 3*_SP[5][sS];
         #if (!vzero(sTangent)) cone {_SP[2][sS+1], 0, _SP[2][sS+1]-(sTangent/3), _SP_radius pigment {rgb <0, 0, 1>} finish {_SP_prevfinish}} #end
         #if (!vzero(_SP[3][sS])) cone {_SP[2][sS], _SP_radius, _SP[2][sS]+(_SP[3][sS]/3), 0 pigment {rgb <1, 0, 1>} finish {_SP_prevfinish}} #end
      #end
      #if (_SP_prevhull) #if (!vequal(_SP[2][sS], _SP[2][sS+1]))
         cylinder {_SP[2][sS], _SP[2][sS+1], _SP_radius/2 pigment {rgb <0, 1, 0>} finish {_SP_prevfinish}}
      #end #end

      // SHOW SEGMENT CURVE
      #if (sSteps > 0)
         #local sS = sS; #local pPos = _SP[2][sS]; #local sI2 = ceil(sSteps/(sPC-1));
         #local sI1 = 1; #while (sI1 <= sI2)
            #local sT = sI1/sI2; #local sPos = _SP[2][sS] + sT*(_SP[3][sS] + sT*(_SP[4][sS] + sT*_SP[5][sS]));
            sphere {sPos, _SP_radius #ifndef (_SP_prevpigment) pigment {rgb sColour} finish {_SP_prevfinish} #end }
            #if (_SP_prevcyls) cylinder {pPos, sPos, _SP_radius #ifndef (_SP_prevpigment) pigment {rgb sColour} finish {_SP_prevfinish} #end } #end
            #local pPos = sPos; #local sColour = sColour + <0, 1, 1>/sSteps;
         #local sI1 = sI1 + 1; #end
      #end #end
   #local sS = sS + 1; #end

   #ifdef (_SP_prevpigment) pigment {_SP_prevpigment} finish {_SP_prevfinish} #end
   #ifdef (_SP_scale) scale _SP_scale #end  #ifdef (_SP_rotate) rotate _SP_rotate #end  #ifdef (_SP_translate) translate _SP_translate #end
   }
   _SP_undefine () #if (debug_progress) #debug "Done!\n" #end
   #end

// SPLINE EVALUATION AND ANIMATION MACROS
// ***********************************************************************
   #macro _SP_evaluate ()
      #if (debug_progress) #debug "\nSPLINE.MCR: Evaluating spline..." #end
      #ifndef (_SP_useclock)     #local _SP_useclock     = clock; #end
      #ifndef (_SP_evenspace)    #local _SP_evenspace    = true;  #end
      #ifndef (_SP_autobank)     #local _SP_autobank     = 1;     #end
      #ifndef (_SP_autorot)      #local _SP_autorot      = 1;     #end
      #ifndef (_SP_maxbanking)   #local _SP_maxbanking   = 90;    #end
      #ifndef (_SP_dforesight)   #local _SP_dforesight   = .01;   #end
      #ifndef (_SP_bforesight)   #local _SP_bforesight   = .05;   #end

      // GET SPLINE CLOCK (FOR EVEN SPACING CONVERT FROM DISTANCE FRACTION)
      #local sC = (_SP_useclock=1 ? 1 : _SP_useclock - floor(_SP_useclock));
      #if (_SP_evenspace) #local sDist = -sC; #local sC = _SP_evenclock (sDist); #else #local sDist = -1; #end

      // CALCULATE NEW SPLINE VALUES (UNDEFINE OLD VALUES IF NECESSARY)
      #ifdef (spline_pos) #undef spline_pos #end      #ifdef (spline_tangent) #undef spline_tangent #end
      #ifdef (spline_accel) #undef spline_accel #end  #ifdef (spline_distance) #undef spline_distance #end

      // FIND CURRENT SEGMENT AND GET SEGMENT TIME
      #local sS = 0; #while (sC > _SP[1][sS+1].x) #local sS = sS + 1; #end
      #local sT = (sC - _SP[1][sS].x) / (_SP[1][sS+1].x - _SP[1][sS].x);

      // CALCULATE SPLINE VALUES
      #declare spline_pos     = _SP[2][sS] + sT*(_SP[3][sS] + sT*(  _SP[4][sS] +   sT*_SP[5][sS]));
      #declare spline_tangent =                 _SP[3][sS] + sT*(2*_SP[4][sS] + 3*sT*_SP[5][sS]);
      #declare spline_accel   =                                 2*_SP[4][sS] + 6*sT*_SP[5][sS];
      #if (sDist = -1) #declare spline_distance = _SP[1][sS].y + sT*(_SP[1][sS+1].y - _SP[1][sS].y);
         #else #declare spline_distance = sDist; #end

      // GET HEADING AND BANKING DIRECTIONS (BASED ON FUTURE TURNING)
      #local sHDir = spline_tangent; #local sBDir = 0*sHDir;
      #local sHClock = sC; #local sBClock = sC; #local sLoop = _SP[0][2];
      #if (!(_SP_autobank=0 & vzero(_SP_autorot)) & vzero(sHDir)) _SP_lookahead (sHClock, _SP_dforesight, sHDir) #end
      #if (!_SP_autobank=0)                                       _SP_lookahead (sBClock, _SP_bforesight, sBDir) #end

      // TRANSFORM SPLINE VALUES
      #ifdef (_SP_scale)
         #declare spline_pos      = spline_pos*_SP_scale;
         #declare spline_tangent  = spline_tangent*_SP_scale;
         #declare spline_accel    = spline_accel*_SP_scale;
         #declare spline_distance = spline_distance*vlength(_SP_scale)/vlength(_SP_scale*0 + 1);
         #declare sHDir = sHDir*_SP_scale; #declare sBDir = sBDir*_SP_scale;
      #end
      #ifdef (_SP_rotate)
         #declare spline_pos     = vrotate(spline_pos, _SP_rotate);
         #declare spline_tangent = vrotate(spline_tangent, _SP_rotate);
         #declare spline_accel   = vrotate(spline_accel, _SP_rotate);
         #declare sHDir = vrotate(sHDir, _SP_rotate); #declare sBDir = vrotate(sBDir, _SP_rotate);
      #end
      #ifdef (_SP_translate) #declare spline_pos = spline_pos + _SP_translate; #end

      // CALCULATE ROTATION ANGLES
      #local sHA = atan3(sHDir.x, sHDir.z);
      #if (vzero(_SP_autorot))
         #declare spline_heading = <0, 0, 0>; #declare spline_pitch = <0, 0, 0>;
      #else
         #declare spline_heading = y*_SP_autorot*sHA;
         #declare spline_pitch = -x*_SP_autorot*atan3(sHDir.y, vlength(sHDir*<1,0,1>));
      #end

      #if (_SP_autobank = 0)
         #declare spline_roll = <0, 0, 0>;
      #else
         #local sRA = _SP_autobank*90*sin(radians(atan3(sBDir.x, sBDir.z) - sHA));
         #declare spline_roll = -z*(sRA < -_SP_maxbanking ? -_SP_maxbanking : (sRA > _SP_maxbanking ? _SP_maxbanking : sRA));
      #end

      _SP_undefine () #if (debug_progress) #debug "Done!\n" #end
   #end

   #macro _SP_lookahead (sC, sInc, sDir)
      #while (vzero(sDir)) #local sC = sC + sInc;
      #if (!sLoop & (sC < 0 | sC > 1))  #if (sC > 1)
         // GET FINAL POINT AND TANGENT OF SPLINE
         #local sS = _SP[0][1] - 2;
         #local sPos = _SP[2][sS] + _SP[3][sS] + _SP[4][sS] + _SP[5][sS];
         #local sTangent = _SP[3][sS] + 2*_SP[4][sS] + 3*_SP[5][sS];
         #if (vzero(sTangent)) #local sPos = sPos - (_SP_value(2-sC - floor(2-sC)) - sPos);
            #else #local sPos = sPos + (sC-1)*sTangent; #end
      #else
         // USE FIRST POINT AND INVERTED FIRST TANGENT
         #local sPos = _SP[2][0]; #local sTangent = -_SP[3][sS];
         #if (vzero(sTangent)) #local sPos = sPos - (_SP_value(-sC - floor(-sC)) - sPos);
            #else #local sPos = sPos + -sC*sTangent; #end
      #end #else
         #if (sC < 0 | sC > 1) #local sC = sC - floor(sC); #end
         #local sPos = _SP_value(sC);
      #end
      #declare sDir = sPos - spline_pos;
   #end #end

   #macro evaluate_spline (_SP, Options) _SP_evaluate () #end
   #macro animate_by_spline (_SP, Options) _SP_evaluate ()
      rotate spline_roll rotate spline_pitch rotate spline_heading
      translate spline_pos
   #end


// MAIN SPLINE OBJECT CREATION MACRO
// ***********************************************************************
   #macro _SP_createobj ()
      #ifndef (spline_object) #macro spline_object () sphere {sPos, abs(sRad) pigment {rgb 1}} #end #end
      #ifndef (_SP_evenspace) #local _SP_evenspace = true; #end
      #ifndef (_SP_start)     #local _SP_start     = 0;    #end
      #ifndef (_SP_finish)    #local _SP_finish    = 1;    #end

      #if (_SP_finish = _SP_start) #local _SP_start = 0; #local _SP_finish = 1; #warning "SPLINE.MCR: Invalid spline portion values specified!\n" #end
      #local _SP_duration = _SP_finish - _SP_start;

      #local sPC = _SP[0][1]; #local sLoop = _SP[0][2]; #local _SP_length = _SP[0][3];
      #local sLength = _SP_length*_SP_duration;

      #ifdef (_SP_scale) #local sLength = sLength*vlength(_SP_scale)/vlength(_SP_scale*0 + 1); #end
      #ifdef (_SP_stepsize) #if (_SP_stepsize > 0) #local _SP_steps = ceil(abs(sLength/_SP_stepsize)); #end #end
      #ifndef (_SP_steps) #local _SP_steps = 50; #end
      #if (_SP_steps < 1) #local _SP_steps = 50; #warning "SPLINE.MCR: Invalid spline steps value specified!\n" #end
      #ifndef (_SP_radius) #ifdef (spline_radius_function) #local _SP_radius = 1; #else #local _SP_radius = _SP_length/(2*_SP_steps); #end #end

      #ifndef (_SP_normsky) #local _SP_normsky = y; #end
      #local _SP_convexnorm = vzero(_SP_normsky); #if (_SP_convexnorm) #undef _SP_normsky #local _SP_normsky = y; #end
      #local _SP_normsky2 = _SP_normsky + x*.01; #if (vzero(vcross(_SP_normsky, _SP_normsky2))) #local _SP_normsky2 = _SP_normsky + y*.01; #end

      #ifdef (_SP_steptwist) #local sStepTwist = (_SP_steptwist * (abs(_SP_steptwist) <= 1 ? 180 : 1));
         #else #ifdef (_SP_totaltwist) #local sStepTwist = _SP_totaltwist/_SP_steps;
         #else #local sStepTwist = 0; #end #end

      #if (debug_progress) #debug concat("\nSPLINE.MCR: Evaluating spline (", str(_SP_steps, 0, 0), " steps)...") #end
      #local sSteps = _SP_steps; #local sStepSize = abs(sLength/_SP_steps);
      #local sRad = _SP_radius; #local sTwist = 0; #local sS = 0; #local pS = -1; #local pC = 0;

   // LOOP THROUGH SPLINE
   #local _SP_step = 0; #while (_SP_step >= 0 & _SP_step <= _SP_steps)
      #local sStep = _SP_step; #local sProgress = _SP_step/_SP_steps;
      #local sClock = _SP_start + _SP_duration*sProgress;
      #local sC = (sClock = 1 ? 1 : sClock - floor(sClock));
      #if (sC < pC) #local sS = 0; #end

      // REPARAMETIZE BY SPLINE LENGTH
      #if (_SP_evenspace) #local sDist = -sC; #local sC = _SP_evenclock (sDist); #else #local sDist = -1; #end

      // FIND SEGMENT AND GET COEFFICIENTS
      #while (sC > _SP[1][sS+1].x) #local sS = sS + 1; #end

      // GET SPLINE VALUES
      #local sT = (sC - _SP[1][sS].x) / (_SP[1][sS+1].x - _SP[1][sS].x);
      #local sPos = _SP[2][sS] + sT*(_SP[3][sS] + sT*(  _SP[4][sS] +   sT*_SP[5][sS]));
      #local sTangent =             _SP[3][sS] + sT*(2*_SP[4][sS] + 3*sT*_SP[5][sS]);
      #local sAccel =                               2*_SP[4][sS] + 6*sT*_SP[5][sS];
      #if (sDist = -1) #local sDist = _SP[1][sS].y + sT*(_SP[1][sS+1].y - _SP[1][sS].y); #end

      // TRANSFORM SPLINE VALUES
      #ifdef (_SP_scale) #declare sPos = sPos*_SP_scale; #declare sTangent = sTangent*_SP_scale; #declare sAccel = sAccel*_SP_scale; #declare sDist = sDist*vlength(_SP_scale)/vlength(_SP_scale*0 + 1); #end
      #ifdef (_SP_rotate) #declare sPos = vrotate(sPos, _SP_rotate); #declare sTangent = vrotate(sTangent, _SP_rotate); #declare sAccel = vrotate(sAccel, _SP_rotate); #end
      #ifdef (_SP_translate) #declare sPos = sPos + _SP_translate; #end
      
      // CALL SPLINE OBJECT MACRO
      #if (debug_progress) #debug concat(str(sProgress*100, 5, 1), "%\b\b\b\b\b\b") #end
      #local _SP_sprogress = sProgress; #local _SP_sclock = sClock; #local _SP_sdist = sDist;
      #ifdef (spline_radius_function) #local sRad = _SP_radius*spline_radius_function(); #end
      #ifdef (spline_object) spline_object () #end

      // INCREMENT STEPS
      #local pStep = _SP_step;
      #if (sStep != _SP_step)                   #local _SP_step = sStep;
         #else #if (sProgress != _SP_sprogress) #local _SP_step = sProgress*_SP_steps;
         #else #if (sDist != _SP_sdist)         #local _SP_step = _SP_step + ((sDist - _SP_sdist)/sStepSize);
         #else #if (sClock != _SP_sclock)       #local _SP_step = _SP_step + ((sClock - _SP_sclock)/_SP_duration)*_SP_steps;
         #end #end #end #end

      #if (pStep = _SP_step) #local _SP_step = _SP_step + 1; #end
      #local sTwist = mod(_SP_step * sStepTwist, 360);

      // SAVE CURRENT VALUES AS PREVIOUS AND END LOOP THROUGH SPLINE
      #local pC = sC; #local pClock = _SP_sclock; #local pProgress = _SP_sprogress; #local pDist = _SP_sdist;
      #local pPos = sPos; #local pTangent = sTangent; #local pAccel = sAccel; #local pRad = sRad;
   #end

   _SP_undefine () #if (debug_progress) #debug "Done! \n" #end
   #end

   #macro create_spline_object (_SP, Options) _SP_createobj () #end

// INTERNAL SPLINE OBJECT CREATION MACROS
// ***********************************************************************
   #macro torus_arc (Tangent, From, To, Radius)
      #local aNorm = vcross(Tangent, To - From);
      #if (vzero(aNorm)) cylinder {From, To, Radius} #else
         #local aNorm = vnormalize(aNorm);
         #local aSpoke = vnormalize(vcross(aNorm, Tangent));
         #local aCos = vdot(vnormalize(To-From), vnormalize(Tangent));
         #local aRadius = vlength(To - From)*.5/sqrt(1 - (aCos*aCos));
         #local aCentre = From + aRadius*aSpoke;
         #local aAngle = 2*degrees(acos(aCos));
         #declare Tangent = vaxis_rotate(Tangent, aNorm, aAngle);

         torus {aRadius, Radius clipped_by {
         #local aQtrBox = box {<0, -Radius, 0>-.001, <aRadius, 0, aRadius>+Radius+.001}
         #local aHlfBox = box {<-aRadius-Radius, -Radius, 0>-.001, <aRadius, 0, aRadius>+Radius+.001}
         #switch (aAngle)
         #case (90) object {aQtrBox} #break   #range (0, 90) object {aQtrBox} object {aQtrBox rotate y*(90 - aAngle)} #break
         #case (180) object {aHlfBox} #break  #range (90, 180) union {object {aQtrBox} object {aQtrBox rotate -y*(aAngle - 90)}} #break
         #range (180, 270) union {object {aHlfBox} object {aQtrBox rotate -y*(aAngle - 90)}} #break
         #else union {object {aHlfBox} object {aQtrBox rotate y*180} object {aQtrBox rotate y*(90 - aAngle)}} #end }

         #local aNX = vnormalize(From - aCentre); #local aNY = aNorm; #local aNZ = vnormalize(vcross(aNY, aNX));
         matrix <aNX.x, aNX.y, aNX.z, aNY.x, aNY.y, aNY.z, aNZ.x, aNZ.y, aNZ.z, aCentre.x, aCentre.y, aCentre.z>}
   #end #end

   #macro fit_to_spline_step ()
      #local aNO = (pPos + sPos)/2; #local aNX = vnormalize(sPos - pPos);
      #if (_SP_convexnorm) #local aNZ = vcross(pAccel + sAccel, aNX); #else #local aNZ = vcross(aNX, _SP_normsky); #end #if (vzero(aNZ)) #local aNZ = vcross(aNX, _SP_normsky2); #end
      #local aNZ = vnormalize(aNZ); #local aNY = vnormalize(vcross(aNZ, aNX));
      matrix <aNX.x, aNX.y, aNX.z, aNY.x, aNY.y, aNY.z, aNZ.x, aNZ.y, aNZ.z, aNO.x, aNO.y, aNO.z>
   #end

   #macro pipe_spline_object () sphere {sPos, abs(sRad)}
      #if (sStep > 0) #if (pRad=sRad) cylinder {pPos, sPos, abs(sRad)}
      #else #local sD = vlength(sPos-pPos); #local sRD = pRad-sRad; #local sD2 = sD*sD - sRD*sRD;
         #if (sD2 > 0) #local sD2 = sqrt(sD2)/sD; #local sD1 = (sPos-pPos)*sRD/(sD*sD); cone {pPos + pRad*sD1, abs(pRad*sD2), sPos + sRad*sD1, abs(sRad*sD2)} #end
   #end #end #end

   #macro link_spline_object (AutoRotate)
      #if (sStep > 0) object {link_object scale sStepSize rotate x*sTwist
         #if (AutoRotate) fit_to_spline_step () #else translate (pPos + sPos)/2 #end }
   #end #end

   #macro coil_spline_object (MinRad) #if (sStep > 0)
      #local sNorm = vcross(sPos - pPos, _SP_normsky); #if (vzero(sNorm)) #local sNorm = vcross(sPos - pPos, x); #end
      #local sNorm = vnormalize(sNorm)*(mod(sStep, 2) = 0 ? 1 : -1);
      #ifndef (_SP0) #declare _SP0 = pPos - sNorm*pRad; sphere {_SP0, MinRad} #end
      #local _SP1 = sPos + sNorm*sRad; sphere {_SP1, MinRad} torus_arc (vcross(sNorm, sPos - pPos), _SP0, _SP1, MinRad)
      #declare _SP0 = _SP1;
   #end #end

// PREDEFINED SPLINE OBJECT CREATION MACROS
// ***********************************************************************
   #macro pipe_spline (_SP, Options)
      #ifndef (_SP_evenspace) #local _SP_evenspace = false; #end
      #macro spline_object () pipe_spline_object () #end _SP_createobj ()
   #end

   #macro blob_threshold (Amount)      #declare _SP_blbthresh  = Amount; 0 #end
   #macro blob_stretch_factor (Amount) #declare _SP_blbstretch = Amount; 0 #end
   #macro blob_spline (_SP, Options)
      #ifndef (_SP_blbthresh)  #declare _SP_blbthresh  = .5;    #end
      #ifndef (_SP_blbstretch) #declare _SP_blbstretch = 1.5;   #end
      #ifndef (_SP_evenspace)  #declare _SP_evenspace  = false; #end
      #macro spline_object () #if (sStep > 0) sphere {0, 1, 1
         scale sRad*<1, 1, 0> + z*vlength(sPos - pPos)*_SP_blbstretch
         rotate z*sTwist rotate y*90 fit_to_spline_step ()}
      #end #end
      blob {threshold _SP_blbthresh _SP_createobj () }
      #undef _SP_blbstretch #undef _SP_blbthresh
   #end

   #macro link_spline (_SP, Options)
      #if (!(defined (link_objects) | defined(link_object))) #declare link_object = cone {-x, 1, x, 0 scale <.5, .15, .5> pigment {rgb 1}} #end
      #ifndef (_SP_autorot) #local _SP_autorot = true; #end
      #ifdef (link_objects)
         #local sObjIndex = 0; #local sObjCount = dimension_size (link_objects, 1);
         #macro spline_object ()
            #local link_object = link_objects[sObjIndex] #declare sObjIndex = mod(sObjIndex+1, sObjCount);
            link_spline_object (_SP_autorot)
         #end
      #else
         #macro spline_object () link_spline_object (_SP_autorot) #end
      #end
      _SP_createobj ()
   #end

   #macro initial_torus_tangent (Vector) #declare _SP_inittan = Vector; 0 #end
   #macro torus_pipe_spline (_SP, Options)
      #ifndef (_SP_evenspace) #local _SP_evenspace = false; #end
      #macro spline_object () sphere {sPos, abs(sRad)}
         #if (sStep = 0) #ifndef (_SP_inittan) #declare _SP_tortan = sTangent; #else #declare _SP_tortan = _SP_inittan; #end
         #else torus_arc (_SP_tortan, pPos, sPos, pRad) #if (sRad < pRad) sphere {sPos, abs(pRad)} #end #end
      #end
      _SP_createobj ()
      #undef _SP_inittan
   #end

   #macro coil_radius (Float) #declare _SP_minorrad = Float; 0 #end
   #macro coil_spline (_SP, Options)
      #ifndef (_SP_minorrad) #local _SP_minorrad = _SP[0][3]/400; #end
      #macro spline_object () coil_spline_object (_SP_minorrad) #end
      #ifdef (_SP0) #undef _SP0 #end
      _SP_createobj ()
      #undef _SP_minorrad #undef _SP0
   #end
