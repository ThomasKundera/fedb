from manim import *
from math import sqrt

class Point2:
  def __init__(self,x=0,y=0):
    self._x=x
    self._y=y

  def norm2(self):
    return (self._x*self._x+self._y*self._y)
  
  def norm(self):
    return sqrt(self.norm2())
  
  def __add__(self,o):
    return Point2(self._x+o._x,self._y+o._y)
    
  def __sub__(self,o):
    return Point2(self._x-o._x,self._y-o._y)

  def __rmul__(self,o):
    return Point2(o*self._x,o*self._y)

  def distance3(self,o):
    n=self-o
    d=n.norm()
    return d*d*d
  
class Xva:
  def __init__(self,x=Point2(),v=Point2(),a=Point2()):
    self._x=x
    self._v=v
    self._a=a

  def do_it(self):
    dot = Dot((p._x,p._y), color=GREEN)
    a1 = Arrow(
      (p._x, p._y),
      plane.coords_to_point(pn._x,pn._y),
      color=BLUE)
    l1 = Line(p._x,p._y,p._x+v._x,p._y+v._y)
    

class TestMe(Scene):
  def construct(self):
    self.myopenning()
    plane = NumberPlane(
      x_range=(-15, 15, 2),
      y_range=(-10, 10, 2),
      x_length=15, 
      y_length=9)
    plane.add_coordinates()
    
    
