# Belwind pictures analysis

## Goal

Analysing https://commons.wikimedia.org/wiki/File:Belwind.jpg to disqualify (once again) flat Earth fallacies.

## Method
We have to do:
- Photogrammetry: measuring object pixel size on the image
- Georeferencing: finding the location of the object in the image

## Photogrammetry

### Basic data
First, some basic data on the image:
Exif:
```
hFile name       : Belwind.jpg
File size       : 6530162 Bytes
MIME type       : image/jpeg
Image size      : 4490 x 3215
Thumbnail       : image/jpeg, 4839 Bytes
Camera make     : NIKON CORPORATION
Camera model    : NIKON D7000
Image timestamp : 2012:10:02 14:26:22
File number     : 
Exposure time   : 1/320 s
Aperture        : F9
Exposure bias   : 0 EV
Flash           : No, compulsory
Flash bias      : 
Focal length    : 70.0 mm
Subject distance: 
ISO speed       : 100
Exposure mode   : Not defined
Metering mode   : Multi-segment
Macro mode      : 
Image quality   : 
White balance   : Auto
Copyright       : Hans Hillewaert                                       
Exif comment    : charset=Ascii   
```

Camera body:
```
Nikon D7000
Body type	Mid-size SLR
Captor size: 23.6 x 15.7 mm
```
The NIKON D7000 is a mid-size SLR, with a sensor of 4928 x 3264 pixels.
So the image we have here has been slightly cropped. Hopefully not too much.

We'll assume that the pixel size hasn't been altered (only crop, no resize), which is likley, and that the image is centered (which should be about correct).

### Crude approximation

We'll start from the simple relation:
$$α=2×\tan^{-1}\left(\frac{l}{2f}\right)$$
Where:
- $f$ is the focal length of the lens (in mm)
- $l$ is the distance (in mm) measured on the sensor
- $α$ is the angle (in radians) of the measured object

This relation is exact only for objects spanning equaly from sensor center. We'll assume it's good enough for objects further away for now.

### Pixel size

The pixel size can be computed from pixel count and the sensor size:
$$px=\frac{s}{p}$$

Where:
- $s$ is the sensor size (in mm)
- $p$ is the number of pixels

Numerically:
$$pxx=\frac{23.6}{4928}=4.79μm$$
$$pxy=\frac{15.7}{3264}=4.81μm$$

The pixels are likley squares, but some dead border likley exists on the sensor, we'll take $$px=4.8μm$$ as a good approximation.

### Gathering data about apparent size of objects in the image

Done. See code/python/object_size.py and crosscheck with code/python/representation.py

### Gathering data about actual size of objects in the scene

The turbines are Vestas V90/3000 Offshore models (https://www.commissiemer.nl/docs/mer/p29/p2959/2959-022generalspecification.pdf).
Exact specifications of the mast are hard to guess, I couldn't get the exact offshore setup.
However, rotor diameter is exactly specidfied and that's 90m. Which will allow us to get the rest from pictures.

We'll use https://parkwind.eu/assets/uploads/general/_2048x1365_fit_center-center_80_none/1622636543163.jpg picture for the tubines.

From ./code/python/object_size.py we get:
- Height of yellow base: 17.5m
- Height of white mast: 52.5m
- Total height: 70m
- White/Yellow ratio: 3

#FIXME: we could slightly enhance those values if knowing the tide height.

There are some data about the substation there: http://www.pianc-aipcn.be/figuren/5%20BTV/vrijdag/Presentation%20%20Haven%20Gent%2008%20May%202015.pdf

We find (see ./code/python/object_size.py):
- Substation total height: 25.3m
- Substation height of yellow base: 13.5m
- Substation height of white block: 12m
- substation width: 15.4m (from data)

### Extracting distances
See ./code/python/object_distance.py

- Distance to substation: about 2.5 km to 3.5 km




