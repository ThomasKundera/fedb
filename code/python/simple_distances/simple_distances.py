#!/usr/bin/env python3
import math
from dms2dec.dms_convert import dms2dec

def spherical_distance(lat1: float, lon1: float, lat2: float, lon2: float,
                       radius: float = 6371000.0) -> float:
    """Haversine formula - orthodromic distance on sphere (meters)"""
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return radius * c


def main():
    #Point A:
    lata=dms2dec("50°48'44.17\"N")
    lnga=dms2dec("0°21'24.36\"W")
    
    #Point B:
    latb=dms2dec("50°41'47.44\"N")
    lngb=dms2dec("0°19'11.76\"W")

    print(f"The distance between the two points is {round(spherical_distance(lata, lnga, latb, lngb) / 1000, 2)} km")
if __name__ == "__main__":
    main()