#!/usr/bin/env python3
from tkunits import m, mm, μm

kPixelSize=4.8*μm

# See picture for labels.
# For windturbines, Em<n> is the size for the mast, up to the middle of the rotor, not the blades, Ey<n> is the size of teh yellow base.
# Only half of the width of the mast and base is measured.
# For the substation: Sp is the pilar, Sc is the cabin
measuredsizearray=[
    # Name       , Bottom left x, Bottom left y, Top right x, Top right y
    ["Em1" ,  133,2371,  142, 2163],
    ["Ey1" ,  133,2371,  142, 2324],
    ["Em2" ,  263,2371,  271, 2130],
    ["Ey2" ,  263,2371,  271, 2315],
    ["Em3" ,  435,2371,  448, 2088],
    ["Ey3" ,  435,2371,  448, 2307],
    ["Em4" ,  681,2368,  697, 2028],
    ["Ey4" ,  681,2368,  697, 2292],
    ["Em5" , 1060,2370, 1075, 1934],
    ["Ey5" , 1060,2370, 1075, 2271],
    ["Em6" , 1482,2362, 1489, 2153],
    ["Ey6" , 1482,2362, 1489, 2238],
    ["Em7" , 1724,2370, 1742, 1770],
    ["Ey7" , 1724,2370, 1742, 2238],
    ["Em8" , 1815,2360, 1823, 2122],
    ["Ey8" , 1815,2360, 1823, 2305],
    ["Em9" , 2261,2361, 2269, 2078],
    ["Ey9" , 2261,2361, 2269, 2297],
    ["Em10", 2838,2363, 2843, 2150],
    ["Ey10", 2838,2363, 2843, 2313],
    ["Em11", 2908,2366, 2921, 2017],
    ["Ey11", 2908,2366, 2921, 2286],
    ["Em12", 3235,2389, 3261, 1394],
    ["Ey12", 3235,2389, 3261, 2166],
    ["Em13", 3388,2364, 3395, 2121],
    ["Ey13", 3388,2364, 3395, 2308],
    ["Em14", 3938,2371, 3948, 1922],
    ["Ey14", 3938,2371, 3948, 2272],
    ["Em15", 4153,2370, 4160, 2088],
    ["Ey15", 4153,2370, 4160, 2307],
    ["Em16", 4252,2375, 4258, 2156],
    ["Sp1" , 3088,2363, 3109,2317],
    ["Sc1" , 3059,2314, 3128,2248],
]

img1622636543163_objects_size= [
    # Name     , blade length, yellow base length, white mast length 
    ["E1", 478, 185, 551],
    ["E2", 294, 117, 347]
]
blsize=90*m/2

P1020928_objects_size= {
    'ybh': 992,
    'wph': 873,
    'wpl': 1401
}

substation_length=19000*mm

def windturbin_scale():
    yblm=0
    wmlm=0
    for name, bl, ybl, wml in img1622636543163_objects_size:
        scale=blsize/bl
        yblm+=ybl*scale
        wmlm+=wml*scale
        print(name, ybl*scale, wml*scale, wml/ybl)
        print("People: ", 14.0*scale)
    print("yblm", yblm/2, "wmlm", wmlm/2, "ratio", wmlm/yblm)

def substation_scale():
    scale=substation_length/P1020928_objects_size['wpl']
    print("substation yellow height", scale*P1020928_objects_size['ybh'],
    "substation white height", scale*P1020928_objects_size['wph'],
    "substation total height", scale*P1020928_objects_size['ybh']+scale*P1020928_objects_size['wph'])
    
def main():
    substation_scale()

# calling main
if __name__ == "__main__":
    main()

