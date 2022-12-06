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
  
  def ipl(self,plane):
    return plane.coords_to_point(self._x,self._y)
  
  def __str__(self):
    return '( '+str(self._x)+' , '+str(self._y)+' )'
  
class Xva:
  def __init__(self,x=Point2(),v=Point2(),a=Point2()):
    #print("Xva.__int__()")
    self._x=x
    self._v=v
    self._a=a
    
  def comp_step(self):
    x=self._x
    v=self._v
    a=self._a

    nx=x+v+a
    nv=v+a
    
    self._x=nx
    self._v=nv
    
    return (x,v,a,nx,nv)
  
  def graph_step(self,pl):
    (x,v,a,nx,nv)=self.comp_step()

    p0 = Dot(x.ipl(pl), color=GREEN)
    v0 = Arrow( x.ipl(pl)         ,(x+v ).ipl(pl)     , buff=0.1, color=BLUE_A)
    v1 = Arrow( x.ipl(pl)         ,(x+nv).ipl(pl)     , buff=0.1, color=BLUE_C)
    a1 = Arrow((x+v).ipl(pl)      ,(x+nv).ipl(pl)     , buff=.01, color=RED_C )
    l1 = Line ( x.ipl(pl)         ,nx.ipl(pl))
    
    return (p0,v0,v1,a1,l1)

  def play_step(self,pl):
    (p0,v0,v1,a1,l1)=self.graph_step(pl)
    
    

  def do_it(self,scene,pl):
    (p0,v0,v1,a1,l1)=self.graph_step(pl)

    scene.add(p0)
    scene.wait(1)
    scene.add(v0)
    scene.wait(1)
    scene.add(a1)
    scene.wait(1)
    scene.add(v1)
    scene.wait(1)
    scene.play(MoveAlongPath(p0, l1), rate_func=linear, run_time=2)
    scene.wait(5)    
    

class XvaList:
  def __init__(self):
    self._list=[]
  
  def append(self,o):
    self._list.append(o)
  
  
  def draw_txt(self,scene,txtstr,i):
    txt_group = VGroup()
    for j in range(0,min(i,len(txtstr))):
      text = Text(txtstr[j],slant=ITALIC).scale(.7)
      txt_group += text
    txt_group.arrange(DOWN).to_edge(DL)
    scene.add(txt_group)
    return txt_group

  def draw_step(self,scene,plane,wtime=1,txtstr=None):
    objlist=[]
    p0list=[]
    v0list=[]
    v1list=[]
    a1list=[]
    l1list=[]
    for xva in self._list:
      (p0,v0,v1,a1,l1)=xva.graph_step(plane)
      p0list.append(p0)
      v0list.append(v0)
      v1list.append(v1)
      a1list.append(a1)
      l1list.append(l1)
    
    for p0 in p0list:
      scene.add(p0)
      objlist.append(p0)
    if (txtstr):
      txt_group=self.draw_txt(scene,txtstr,1)
    scene.wait(wtime)

    for v0 in v0list:
      scene.add(v0)
      objlist.append(v0)
    if (txtstr):
      scene.remove(txt_group)
      txt_group=self.draw_txt(scene,txtstr,2)
    scene.wait(wtime)
      
    for a1 in a1list:
      scene.add(a1)
      objlist.append(a1)
    if (txtstr):
      scene.remove(txt_group)
      txt_group=self.draw_txt(scene,txtstr,3)
    scene.wait(wtime)
    
    for v1 in v1list:
      scene.add(v1)
      objlist.append(v1)
    if (txtstr):
      scene.remove(txt_group)
      txt_group=self.draw_txt(scene,txtstr,4)
    scene.wait(wtime)
    playlist=[]
    for p0,l1 in zip(p0list,l1list):
      playlist.append(MoveAlongPath(p0, l1))
    
    scene.play(*playlist, rate_func=linear, run_time=2*wtime)
    scene.remove(txt_group)
    return(objlist)


class TestMe(Scene):
  def construct(self):
    plane = NumberPlane(
      x_range=(-2, 28, 2),
      y_range=(-2, 18, 2),
      x_length=15, 
      y_length=9)
    plane.add_coordinates()
    self.add(plane)
    x=Point2(2,2)
    v=Point2(3,2)
    a=Point2(0,-1)
    xva=Xva(x,v,a)
    xva.do_it(self,plane)
    
    
