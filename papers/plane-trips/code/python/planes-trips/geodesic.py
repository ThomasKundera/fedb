import math

def great_circle_distance(r,longitude1,latitude1,longitude2,latitude2)

  ptlon1 = longitude1
  ptlat1 = latitude1
  ptlon2 = longitude2
  ptlat2 = latitude2

  numberofsegments = num_of_segments
  onelessthansegments = numberofsegments - 1
  fractionalincrement = (1.0/onelessthansegments)

  ptlon1_radians = math.radians(ptlon1)
  ptlat1_radians = math.radians(ptlat1)
  ptlon2_radians = math.radians(ptlon2)
  ptlat2_radians = math.radians(ptlat2)

  distance_radians=2*math.asin(math.sqrt(math.pow((math.sin((ptlat1_radians-ptlat2_radians)/2)),2) + math.cos(ptlat1_radians)*math.cos(ptlat2_radians)*math.pow((math.sin((ptlon1_radians-ptlon2_radians)/2)),2)))
  # 6371.009 represents the mean radius of the earth
  # shortest path distance
  distance_km = r * distance_radians

  return distance_km



# from here : http://gis.stackexchange.com/questions/47/what-tools-in-python-are-available-for-doing-great-circle-distance-line-creati

def great_circle_stuff(r,longitude1,latitude1,longitude2,latitude2)

  ptlon1 = longitude1
  ptlat1 = latitude1
  ptlon2 = longitude2
  ptlat2 = latitude2

  numberofsegments = num_of_segments
  onelessthansegments = numberofsegments - 1
  fractionalincrement = (1.0/onelessthansegments)

  ptlon1_radians = math.radians(ptlon1)
  ptlat1_radians = math.radians(ptlat1)
  ptlon2_radians = math.radians(ptlon2)
  ptlat2_radians = math.radians(ptlat2)

  distance_radians=2*math.asin(math.sqrt(math.pow((math.sin((ptlat1_radians-ptlat2_radians)/2)),2) + math.cos(ptlat1_radians)*math.cos(ptlat2_radians)*math.pow((math.sin((ptlon1_radians-ptlon2_radians)/2)),2)))
  # 6371.009 represents the mean radius of the earth
  # shortest path distance
  distance_km = r * distance_radians

  mylats = []
  mylons = []

  # write the starting coordinates
  mylats.append([])
  mylons.append([])
  mylats[0] = ptlat1
  mylons[0] = ptlon1 

  f = fractionalincrement
  icounter = 1
  while (icounter <  onelessthansegments):
          icountmin1 = icounter - 1
          mylats.append([])
          mylons.append([])
          # f is expressed as a fraction along the route from point 1 to point 2
          A=math.sin((1-f)*distance_radians)/math.sin(distance_radians)
          B=math.sin(f*distance_radians)/math.sin(distance_radians)
          x = A*math.cos(ptlat1_radians)*math.cos(ptlon1_radians) + B*math.cos(ptlat2_radians)*math.cos(ptlon2_radians)
          y = A*math.cos(ptlat1_radians)*math.sin(ptlon1_radians) +  B*math.cos(ptlat2_radians)*math.sin(ptlon2_radians)
          z = A*math.sin(ptlat1_radians) + B*math.sin(ptlat2_radians)
          newlat=math.atan2(z,math.sqrt(math.pow(x,2)+math.pow(y,2)))
          newlon=math.atan2(y,x)
          newlat_degrees = math.degrees(newlat)
          newlon_degrees = math.degrees(newlon)
          mylats[icounter] = newlat_degrees
          mylons[icounter] = newlon_degrees
          icounter += 1
          f = f + fractionalincrement

  # write the ending coordinates
  mylats.append([])
  mylons.append([])
  mylats[onelessthansegments] = ptlat2
  mylons[onelessthansegments] = ptlon2

  # Now, the array mylats[] and mylons[] have the coordinate pairs for intermediate points along the geodesic
  # My mylat[0],mylat[0] and mylat[num_of_segments-1],mylat[num_of_segments-1] are the geodesic end points

  # write a kml of the results
  zipcounter = 0
  kmlheader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>LineString.kml</name><open>1</open><Placemark><name>unextruded</name><LineString><extrude>1</extrude><tessellate>1</tessellate><coordinates>"
  print kmlheader
  while (zipcounter < numberofsegments):
          outputstuff = repr(mylons[zipcounter]) + "," + repr(mylats[zipcounter]) + ",0 "
          print outputstuff
          zipcounter += 1
  kmlfooter = "</coordinates></LineString></Placemark></Document></kml>"
  print kmlfooter











# From here https://gist.github.com/gabesmed/1826175

def great_circle_distance(r,latlong_a, latlong_b):
    """
    >>> coord_pairs = [
    ...     # between eighth and 31st and eighth and 30th
    ...     [(40.750307,-73.994819), (40.749641,-73.99527)],
    ...     # sanfran to NYC ~2568 miles
    ...     [(37.784750,-122.421180), (40.714585,-74.007202)],
    ...     # about 10 feet apart
    ...     [(40.714732,-74.008091), (40.714753,-74.008074)],
    ...     # inches apart
    ...     [(40.754850,-73.975560), (40.754851,-73.975561)],
    ... ]
    
    >>> for pair in coord_pairs:
    ...     great_circle_distance(pair[0], pair[1]) # doctest: +ELLIPSIS
    83.325362855055...
    4133342.6554530...
    2.7426970360283...
    0.1396525521278...
    """
    lat1, lon1 = latlong_a
    lat2, lon2 = latlong_b

    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = (math.sin(dLat / 2) * math.sin(dLat / 2) +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
            math.sin(dLon / 2) * math.sin(dLon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = EARTH_CIRCUMFERENCE * c
    
    return d