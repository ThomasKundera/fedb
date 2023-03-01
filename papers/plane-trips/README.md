# Goal is to probe Earth metric using plane time of flight

Unfortunately, there are two totally unrelkated works in that repository.

A small manual test, that is taking some known distances to ensure linearity of distance vs time plane trips.
Files are:
   - code/python/point.py
   - plane-trips.tm
   - code/python/plane-trips.py

A more ambitious code, parsing about 20.000 trips to probe metric using either plane or spherical hypothesis.
File are:
   - data/GlobalAirportDatabase.txt :(taken from http://www.partow.net/miscellaneous/airportdatabase/index.html "The Global Airport Database Release Version 0.0.2 Author: Arash Partow")
   - data/airports.csv  : conversion of the above in csv (by unknown code)
   - data/oneworld.pdf       : Planes schedule PDF
   - data/oneworlds-div.html : conversion of the above in html by unknown mean

   - code/python/flight_data.py
   - code/python/read-oneword.py
   - code/python/routes_analysis.py

Usage:
   - read-oneword.py to read the flight data and dump them in allflights.dat
   - flight_data.py to read alkl flights, sort from the 40.000 ones the 1450 different routes, and 1399 direct routes. Dump them in simpleroutes.dat
   - routes_analysis.py to analyse routes and produce plots.

