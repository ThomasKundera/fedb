from manim import *
from math import sqrt
from helpers import Point2
from helpers import Xva
from helpers import XvaList

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
        
        xva=Xva(Point2(0,14),Point2(2,0),Point2())
        for i in range(8):
          txt_group = VGroup()
          for j in range(0,min(i,5)):
            text = Text(txtstr[j],slant=ITALIC).scale(.8)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)
          (p0,v0,v1,a1,l1)=xva.graph_step(plane)
          self.add(p0)
          self.add(v1)
          self.wait(1)
          self.play(MoveAlongPath(p0, l1), rate_func=linear, run_time=2)
          self.wait(1)
          self.remove(txt_group)
        self.wait(2)
        

class SpeedAcceleration(Scene):
    def myopenning(self):
        text = Text('A few words about speed and acceleration').scale(0.9)
        self.add(text)
        self.wait(3)
        self.remove(text)
    
    def construct(self):
        self.myopenning()
        plane = NumberPlane(
          x_range=(-2, 8, 1),
          y_range=(-1, 5, 1),
          x_length=15, 
          y_length=10)
        plane.add_coordinates()
        self.add(plane)
        
        txtstr=[
          'If we have an object',
          'with a speed',
          'and a force acting on it',
          'it will modify the speed vector',
          'and so the location',
          ' where the object is heading.',
          ]        
        xva=Xva(Point2(1,4),Point2(4,0),Point2(0,-2))
        xvalist=XvaList()
        xvalist.append(xva)

        objlist=[]
        txt_group = VGroup()
        for i in range(6):
          if (i==0):
            objlist.extend(xvalist.draw_step(self,plane,1,txtstr))
          else:
            txt_group = VGroup()
            for j in range(0,min(i+5,len(txtstr))):
              text = Text(txtstr[j],slant=ITALIC).scale(.7)
              txt_group += text
            txt_group.arrange(DOWN).to_edge(DL)
            self.add(txt_group)
            self.wait(1)
            self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)
        

        
        
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
        xva=Xva(Point2(2,14),Point2(0,0),Point2(0,-1))
        objlist=[]
        for i in range(8):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DR)
          self.add(txt_group)
          (p0,v0,v1,a1,l1)=xva.graph_step(plane)
          self.add(p0)
          self.wait(1)
          self.add(v0)
          self.wait(1)
          self.add(a1)
          self.wait(1)
          self.add(v1)
          self.wait(1)
          self.play(MoveAlongPath(p0, l1), rate_func=linear, run_time=2)
          self.wait(1)
          objlist.extend((p0,v0,v1,a1,l1))
          self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)
       
       
        txtstr=[
          'In those conditions',
          'an object having some speed along x',
          'will touch ground at same time',
          'as those who have not',
          ]
        ps=[ Point2(0,14), Point2(2,14), Point2(4,14),Point2(6,14)]
        vs=[ Point2(6, 0), Point2(4, 0), Point2(2, 0),Point2(0, 0)]
        a=Point2(0,-1)

        xvalist=XvaList()
        for i in range(len(ps)):
          xvalist.append(Xva(ps[i],vs[i],a))

        objlist=[]
        for i in range(8):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)  
          
          objlist.extend(xvalist.draw_step(self,plane,1./(i+1)))
          self.wait(1)
          self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)

        txtstr=[
          'Note that this finite approximation is not correct:',
          'here we are approximating integrals with summations',
          'along finite discrete time steps.',
          'That gives some idea of the real physics',
          'but we would have to use differential equations',
          'to come to anything close to reality.',
          'The goal here is only to feel how it works',
          'whithout having to understand calculus',
          ]
        ps=[ Point2(0,14), Point2(2,14), Point2(4,14),Point2(6,14)]
        vs=[ Point2(6, 0), Point2(4, 0), Point2(2, 0),Point2(0, 0)]
        a=Point2(0,-1)

        xvalist=XvaList()
        for i in range(len(ps)):
          xvalist.append(Xva(ps[i],vs[i],a))

        objlist=[]
        for i in range(8):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)  
          
          objlist.extend(xvalist.draw_step(self,plane,1./(i+1)))
          self.wait(1)
          self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)

        

class RoundEarth(Scene):
  
    def myopenning(self):
        text = Text('Trajectories on central potential').scale(1.1)
        self.add(text)
        self.wait(3)
        self.remove(text)
        
    def construct(self):
        self.myopenning()
        plane = NumberPlane(
          x_range=(-15, 15, 2),
          y_range=(-10, 10, 2),
          x_length=15, 
          y_length=9)
        plane.add_coordinates()
        text = Text(
          '... Now a central gravitational field...',
          slant=ITALIC).scale(0.8).to_edge(DL)
        
        self.add(plane)
        self.add(text)
        self.wait(3)
        self.remove(text)

        txtstr=[
          'Everything is attracted to center',
          'by a force in 1/r²',
          ]
        ps=[ Point2(-8,-8), Point2(-8, 8), Point2( 8,-8),Point2( 8, 8),
             Point2( 0,-8), Point2(-8, 0), Point2( 8, 0),Point2( 0, 8),
            ]
        vs=Point2( 0, 0)
        a=Point2(0,0)

        xvalist=XvaList()
        for i in range(len(ps)):
          xvalist.append(Xva(ps[i],vs,a))

        objlist=[]
        for i in range(5):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)
          for xva in xvalist._list:
            p=xva._x
            xva._a=(-20./p.distance3(Point2()))*p
          
          objlist.extend(xvalist.draw_step(self,plane,1./(i+1)))
          self.wait(1)
          self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)
        
        
        txtstr=[
          'Lets now give some initial speed to all those points...',
          'We start to see that objects are rotating',
          'Around the center when falling...'
          ]
        ps=[ Point2(-8,-8), Point2(-8, 8), Point2( 8,-8),Point2( 8, 8),
             Point2( 0,-8), Point2(-8, 0), Point2( 8, 0),Point2( 0, 8),
            ]
        v0=.2
        vs=[ Point2(   v0, 0), Point2( 2*v0, 0   ), Point2( 3*v0, 0   ),Point2( 4*v0, 0),
             Point2( 5*v0, 0), Point2(    0, 6*v0), Point2( 0   , 7*v0),Point2( 8*v0, 0),
           ]

        xvalist=XvaList()
        for i in range(len(ps)):
          xvalist.append(Xva(ps[i],vs[i],a))

        objlist=[]
        for i in range(7):
          txt_group = VGroup()
          for j in range(0,min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)
          for xva in xvalist._list:
            p=xva._x
            xva._a=(-20./p.distance3(Point2()))*p
          
          objlist.extend(xvalist.draw_step(self,plane,1./(i+1)))
          self.wait(1)
          self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)
        
class Orbiting(Scene):
  
    def myopenning(self):
        text = Text('Orbiting').scale(1.1)
        self.add(text)
        self.wait(3)
        self.remove(text)
        
    def construct(self):
        self.myopenning()
        plane = NumberPlane(
          x_range=(-15, 15, 2),
          y_range=(-10, 10, 2),
          x_length=15, 
          y_length=9)
        plane.add_coordinates()
        text = Text(
          '... Still a gravitational field...',
          slant=ITALIC).scale(0.8).to_edge(DL)
        
        self.add(plane)
        self.add(text)
        self.wait(3)
        self.remove(text)
