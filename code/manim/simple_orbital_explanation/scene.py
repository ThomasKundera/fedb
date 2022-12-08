from manim import *
from math import sqrt
from helpers import Point2
from helpers import Xva
from helpers import XvaList
from helpers import pi

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
        
        comment='''
        Lets have an object moving with some speed,
        advancing 2 units per unit of time
        without any force acting on it.
        That object will continue its trajectory at same speed,
        on a straight line, as long as conditions don't change.
        This is conservation of momentum.
        '''
        
        txtstr=[
          'p=mv [kg m s⁻²]'
          ]
        
        xva=Xva(Point2(0,14),Point2(2,0),Point2())
        text = Text(txtstr[0],slant=ITALIC).scale(.8)
        text.to_edge(DL)
        self.add(text)
        for i in range(8):
          (p0,v0,v1,a1,l1)=xva.graph_step(plane)
          self.add(p0)
          self.add(v1)
          self.wait(1)
          self.play(MoveAlongPath(p0, l1), rate_func=linear, run_time=2)
          self.wait(1)
        self.remove(text)
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
        
        comment='''
          If we have an object with a given speed
          and a force acting on it, that force will
          create an acceleration (in red), and
          it will modify the original speed vector
          (in clear blue), to another value (deeper blue)
          which will affect the move of that object.
        '''
        xva=Xva(Point2(1,4),Point2(4,0),Point2(0,-2))
        xvalist=XvaList()
        xvalist.append(xva)

        objlist=[]
        objlist.extend(xvalist.draw_step(self,plane,1))
        self.wait(1)
        for o in objlist: self.remove(o)
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
          'around the center when falling...'
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
        
        
        txtstr=[
          'We started to see objects rotating,',
          'lets look again at what\'s hapenning',
          'with different initial speeds',
          'The slower ones are falling to ground,',
          'the faster ones are escaping',
          'but some seem to stay in between'
          ]

        xvalist=XvaList()
        a=Point2(0,0)
        v0=.3
        for i in range(8):
          p=Point2()
          p.from_polar(8,i*2.*pi/8.)
          v=Point2()
          v.from_polar((i+2)*v0,i*2.*pi/8.+pi/2.)
          xvalist.append(Xva(p,v,a))

        objlist=[]
        for i in range(12):
          txt_group = VGroup()
          for j in range(max(0,min(i-3,len(txtstr),len(txtstr)-3)),min(i,len(txtstr))):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)
          for xva in xvalist._list:
            p=xva._x
            if (p.norm2()>20):
              xva._a=(-20./p.distance3(Point2()))*p
            else:
              xva._v=Point2()
              xva._a=Point2()
          
          objlist.extend(xvalist.draw_step(self,plane,1./(i+1)))
          self.wait(1)
          self.remove(txt_group)
        self.wait(1)
        for o in objlist: self.remove(o)
        self.wait(1)
        self.remove(txt_group)
        
        
        txtstr=[
          'So we see that only with a central force',
          'we can get three disting behaviors:',
          '- Falling down',
          '- Escaping',
          '- Rotating',
          'Quite something...',
          ]
        
        txt_group = VGroup()
        for j in range(len(txtstr)):
          text = Text(txtstr[j],slant=ITALIC).scale(.7)
          txt_group += text
        txt_group.arrange(DOWN).to_edge(DL)
        self.add(txt_group)
        self.wait(4)
        self.remove(txt_group)
        
        txtstr=[
          'Lets look for orbits now...',
        ]

        xvalist=XvaList()
        a=Point2(0,0)
        v0=.015
        for i in range(8):
          p=Point2()
          p.from_polar(8,i*2.*pi/8.)
          v=Point2()
          v.from_polar(i*v0+1.45,i*2.*pi/8.+pi/2.)
          print(v.norm())
          xvalist.append(Xva(p,v,a))

        objlist=[]
        for i in range(18):
          txt_group = VGroup()
          for j in range(0,1):
            text = Text(txtstr[j],slant=ITALIC).scale(.7)
            txt_group += text
          txt_group.arrange(DOWN).to_edge(DL)
          self.add(txt_group)
          for xva in xvalist._list:
            p=xva._x
            if (p.norm2()>20):
              xva._a=(-20./p.distance3(Point2()))*p
            else:
              xva._v=Point2()
              xva._a=Point2()
          
          objlist.append(xvalist.draw_step(self,plane,1./(i+1)))
          if (len(objlist)>3):
            otd=objlist.pop(0)
            for o in otd: self.remove(o)
            
          self.wait(1)
          self.remove(txt_group)
        self.wait(1)
        for ol in objlist:
          for o in ol:
            self.remove(o)
        self.wait(1)
        self.remove(txt_group)
        
        txtstr=[
          'We have to recall that our computations',
          'using naive step integration',
          'is to the most a crude approximation',
          'of reality.',
          'Our "orbits" cannot be really stable',
          'using such a simple approach',
          'We would have toa ctually do calculus',
          'and we would find out perfect ellipses at solutions'
          ]
        
        txt_group = VGroup()
        for j in range(len(txtstr)):
          text = Text(txtstr[j],slant=ITALIC).scale(.7)
          txt_group += text
        txt_group.arrange(DOWN).to_edge(DL)
        self.add(txt_group)
        self.wait(4)
        self.remove(txt_group)
        
