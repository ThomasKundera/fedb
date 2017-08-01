#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://gist.github.com/KillerGoldFisch/5685128

class Vector3D:
  def __init__(self,x=0.0,y=0.0,z=0.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  def __add__(self, other):	# on self + other
    return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

  def __sub__(self, other):	# on self - other
    return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

  def __mul__(self, other):	# on self * other
    a = self
    b = other
    return Vector3D(
      a.y*b.z - a.z*b.y,
      a.z*b.x - a.x*b.z,
      a.x*b.y - a.y*b.x
    )
    
  def __str__( self ):
    return "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"


class Point3D(Vector3D):
  def __init__(self,x=0.0,y=0.0,z=0.0):
    super(Point3D, self).__init__(x,y,z)

