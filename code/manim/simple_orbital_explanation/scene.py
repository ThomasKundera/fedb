from manim import *

class Point2:
  def __init__(self,x=0,y=0):
    self._x=x
    self._y=y
  
  def __add__(self,o):
    return Point2(self._x+o._x,self._y+o._y)
    


class Momentum(Scene):
  
    def myopenning(self):
        text = Text('Conservation of momentum').scale(1.5)
        self.add(text)
        self.wait(3)
        self.remove(text)
    
    def construct(self):
        self.myopenning()
        plane = NumberPlane(
          x_range=(-2, 28, 2),
          y_range=(-2, 18, 2),
          x_length=15, 
          y_length=9)
        plane.add_coordinates()
        text = Text(
          '... Lets suppose no forcefield anywhere...',
          slant=ITALIC).scale(1).to_edge(DL)
        
        self.add(plane)
        self.add(text)
        self.wait(3)
        self.remove(text)
        
        txtstr=[
          'We have an object moving with some speed',
          'advancing 2 units per unit of time',
          'without any force acting on it.',
          'That object will continue at same speed',
          'on a straight line.'
          ]
        
        for i in range(10):
          txt_group = VGroup()
          for j in range(0,min(i,5)):
            text = Text(txtstr[j],slant=ITALIC).scale(.8)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          dot = Dot(plane.coords_to_point(2*i,14), color=GREEN)
          l1 = Line(plane.coords_to_point(2*i,14),plane.coords_to_point(2*(i+1),14))
          a1 = Arrow(
            plane.coords_to_point(2*i,14),
            plane.coords_to_point(2*(i+1),14),
            color=BLUE)
          self.add(txt_group,a1,dot)
          self.play(MoveAlongPath(dot, l1), rate_func=linear, run_time=2)
          self.remove(txt_group)
        self.wait(1)
        
        
        
class FlatGravity(Scene):
  
    def myopenning(self):
        text = Text('Trajectories on flat Earth').scale(1.1)
        self.add(text)
        self.wait(3)
        self.remove(text)
    
    def construct(self):
        self.myopenning()
        plane = NumberPlane(
          x_range=(-2, 28, 2),
          y_range=(-2, 18, 2),
          x_length=15, 
          y_length=9)
        plane.add_coordinates()
        text = Text(
          '... Lets suppose a constant gravitational field...',
          slant=ITALIC).scale(0.8).to_edge(DL)
        
        self.add(plane)
        self.add(text)
        self.wait(3)
        self.remove(text)
        
        txtstr=[
          'At small scale, on Earth everything happens',
          'like Earth would be flat',
          'and gravitation would be constant.',
          'Newtonnian gravity acts like a force',
          '(called weight), and thus',
          'is accelerating things down,',
          'so speed increasse with time.',
          ]
        y=14
        v=0
        a=-1
        plist=[]
        alist=[]
        for i in range(8):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DR)
          dot = Dot(plane.coords_to_point(2,y), color=GREEN)
          plist.append(dot)
          l1 = Line(plane.coords_to_point(2,y),plane.coords_to_point(2,y+v))
          a1 = Arrow(
            plane.coords_to_point(2,y),
            plane.coords_to_point(2,y+v),
            color=BLUE)
          alist.append(a1)
          self.add(txt_group,a1,dot)
          self.play(MoveAlongPath(dot, l1), rate_func=linear, run_time=2)
          self.remove(txt_group)
          y=y+v
          v=v+a
        self.wait(1)
        self.remove(txt_group)
        for a in alist: self.remove(a)
        for p in plist: self.remove(p)
        self.wait(1)
       
       
        txtstr=[
          'In those conditions',
          'an object having some speed along x',
          'will touch ground at same time',
          'as those who have not',
          ]
        ps=[ Point2(0,14), Point2(2,14), Point2(4,14),Point2(6,14)]
        vs=[ Point2(6, 0), Point2(4, 0), Point2(2, 0),Point2(0, 0)]
        a=Point2(0,-1)

        plist=[]
        alist=[]
        for i in range(8):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DR)
          playlist=[]
          for j in range(len(ps)):
            p=ps[j]
            v=vs[j]
            dot = Dot(plane.coords_to_point(p._x,p._y), color=GREEN)
            plist.append(dot)
            pn=p+v
            l1 = Line(plane.coords_to_point(p._x,p._y),plane.coords_to_point(pn._x,pn._y))
            a1 = Arrow(
              plane.coords_to_point( p._x, p._y),
              plane.coords_to_point(pn._x,pn._y),
              color=BLUE)
            alist.append(a1)
            self.add(txt_group,a1,dot)
            playlist.append(MoveAlongPath(dot, l1))
            ps[j]=p+v
            vs[j]=v+a
          self.play(*playlist, rate_func=linear, run_time=2)
          self.remove(txt_group)
        self.wait(1)
        self.remove(txt_group)
        for a in alist: self.remove(a)
        for p in plist: self.remove(p)
        self.wait(1)

        
