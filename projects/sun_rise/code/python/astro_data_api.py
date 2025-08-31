#!/usr/bin/env python3

import datetime
import requests
import json

kStellariumUrl = "http://localhost:8090"


def get_sun_diameter(dt,loc):
    dts=dt.strftime("%Y-%m-%dT%H:%M:%S")
    requests.get(f"{kStellariumUrl}/api/main/time?time={dts}")
    requests.get(f"{kStellariumUrl}/api/location/setlocationfields?latitude={loc[0]}&longitude={loc[1]}&altitude=0")

    response = requests.get(f"{kStellariumUrl}/api/objects/info?name=Sun&format=json")
    data = response.json()
    sun_size_deg = data.get("size-dd", 0)
    #sun_size_arcmin = sun_size_deg * 60
    return sun_size_deg
    

if __name__ == "__main__":
    dt = datetime.datetime.now()
    loc = (48.8566, 2.3522)  # Paris
    sun_size_deg = get_sun_diameter(dt, loc)
    print(f"Sun size in degrees: {sun_size_deg}")
