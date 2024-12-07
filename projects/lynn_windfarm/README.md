# Lynn windfarm pictures analysis

## Goal

Analysing https://www.flickr.com/photos/37012317@N08/51664909026/ to disqualify (once again) flat Earth fallacies.

## Method
We have to do:
- Photogrammetry: measuring object pixel size on the image
- Georeferencing: finding the location of the object in the image
- Geolocation: finding the location of the camera
- Reconstructing the scene

## Photogrammetry

### Basic data
First, some basic data on the image:
Exif:
```
File name       : 51664909026_2877f487d2_o.jpg
File size       : 10955414 Bytes
MIME type       : image/jpeg
Image size      : 6240 x 3510
Thumbnail       : image/jpeg, 6053 Bytes
Camera make     : Canon
Camera model    : Canon EOS 6D Mark II
Image timestamp : 2021:10:30 15:08:54
File number     : (0)
Exposure time   : 1/320 s
Aperture        : F16
Exposure bias   : -1/3 EV
Flash           : No, compulsory
Flash bias      : 0 EV
Focal length    : 600.0 mm
Subject distance: 0 m
ISO speed       : 200
Exposure mode   : Shutter priority (Tv)
Metering mode   : Spot
Macro mode      : Off
Image quality   : Superfine
White balance   : Daylight
Copyright       : 
```

Camera body:
```
Canon EOS 6D Mark II
Captor size: 35.9 × 24.0 mm2 / 6240 × 4160 pixels
```
So the image we have here has been cropped, veritically but not horizontally.

We'll assume that the pixel size hasn't been altered (only crop, no resize), which is likley, and that the image is centered (which should be about correct).


### Pixel size

The pixel size can be computed from pixel count and the sensor size:
$$px=\frac{s}{p}$$

Where:
- $s$ is the sensor size (in mm)
- $p$ is the number of pixels

Numerically:
$$pxx=\frac{35.9}{6240}=5.75μm$$
$$pxy=\frac{24.0}{4160}=5.77μm$$

The pixels are likley squares, but some dead border likley exists on the sensor, we'll take $$px=5.76μm$$ as a good approximation.

### Pixel size of objects with convertion to actual size

#### Crude approximation

We'll start from the simple relation:
$$α=2×\tan^{-1}\left(\frac{l}{2f}\right)$$
Where:
- $f$ is the focal length of the lens (in mm)
- $l$ is the distance (in mm) measured on the sensor
- $α$ is the angle (in radians) of the measured object

This relation is exact only for objects spanning equaly from sensor center. We'll assume it's good enough as the focale is long enough (so the angles are small).


If we reverse the above relation, we'll get:
$$l=2f\tan\left(\frac{α}{2}\right)$$



### Wind farm characteristics

#### Lynn windfarm
Basic data:
https://en.wikipedia.org/wiki/Lynn_and_Inner_Dowsing_Wind_Farms

The farm was completed in 2009, so the picture in 2021 shows a completed farm.

The wind turbine are SWT-3.7-107:
https://en.wind-turbine-models.com/turbines/1272-siemens-swt-3.6-107-offshore

Diameter: 107.0 m

#### Race Bank windfarm
Basic data:
https://en.wikipedia.org/wiki/Race_Bank_wind_farm

The wind turbines are SWT-6.0-154:
https://fr.wind-turbine-models.com/turbines/657-siemens-swt-6.0-154

Diameter: 154.0 m

## Reconstructing the scene

### Some computed data

Horizon distance was estimated as about 11 km from the wind turbines bases.
So, altitude of the camera is about 10m
