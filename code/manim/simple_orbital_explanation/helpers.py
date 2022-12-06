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
  
  def tpl(self):
    return [self._x,self._y,0]
  
  def __str__(self):
    return '( '+str(self._x)+' , '+str(self._y)+' )'
  
class Xva:
  def __init__(self,x=Point2(),v=Point2(),a=Point2()):
    print("Xva.__int__()")
    self._x=x
    self._v=v
    self._a=a

  def do_it(self,scene):
    print("Xva.do_it()")
    nx=self._x+self._v+self._a
    nv=self._v+self._a
    print(self._x.tpl())
    p0 = Dot(self._x.tpl(), color=GREEN)
    print(p0)
    v0 = Arrow( self._x.tpl()         ,(self._x+self._v).tpl(), buff=0.1, color=BLUE_A)
    v1 = Arrow( self._x.tpl()         ,(self._x+nv).tpl()     , buff=0.1, color=BLUE_C)
    a  = Arrow((self._x+self._v).tpl(),(self._x+nv).tpl()     , buff=0.1, color=RED_C )
    l1 = Line(self._x.tpl(),nx.tpl())

    scene.add(p0)
    scene.wait(1)
    scene.add(v0)
    scene.wait(1)
    scene.add(a)
    scene.wait(1)
    scene.add(v1)
    scene.wait(1)
    scene.play(MoveAlongPath(p0, l1), rate_func=linear, run_time=2)
    
    return (p0,v0,a,nv)
    

class TestMe(Scene):
  def construct(self):
    plane = NumberPlane(
      x_range=(-15, 15, 2),
      y_range=(-10, 10, 2),
      x_length=15, 
      y_length=9)
    plane.add_coordinates()
    self.add(plane)
    x=Point2(2,2)
    v=Point2(3,2)
    a=Point2(0,-1)
    xva=Xva(x,v,a)
    (p0,v0,a,nv)=xva.do_it(self)
    print(p0)
    
