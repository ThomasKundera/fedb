#!/usr/bin/env python3
from math import tan,atan, atan2, pi
from tkunits import m, mm, μm
from object_size import kPixelSize

substation_white_box_width_sensor=(3128-3059)*kPixelSize
substation_white_box_height_sensor=(2314-2248)*kPixelSize

substation_white_box_width_m=15.4*m
substation_white_box_height_m=12*m

def compute_angle(l,f):
    return 2*atan2(l,2*f)

def do_it(ssize,rsize):
    print("rsize",rsize)
    print("ssize",ssize)
    α=compute_angle(ssize,70*mm)
    print("Angle α = ",α*180/pi)

    d=rsize/(2*tan(α/2))
    print("Distance d = ",d)


def main():
    do_it(substation_white_box_width_sensor,substation_white_box_width_m)
    do_it(substation_white_box_height_sensor,substation_white_box_height_m)

    


# Calling main
if __name__ == "__main__":
    main()

