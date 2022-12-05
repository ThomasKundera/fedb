from manim import *

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
        
        text = Text(
          '... We have an object moving with some speed...',
          slant=ITALIC).scale(.5).to_edge(DL)
        dot = Dot(plane.coords_to_point(0,14), color=GREEN)
        a1 = Arrow(
          plane.coords_to_point(0,14),
          plane.coords_to_point(2,14),
          color=BLUE)
        self.add(text,a1,dot)
        
        l1 = Line (plane.coords_to_point(0,14),plane.coords_to_point(2,14))
        
        self.add(plane) #, dot_scene, ax, dot_axes, lines)
        
        for i in range(10):
          dot = Dot(plane.coords_to_point(2*i,14), color=GREEN)
          l1 = Line(plane.coords_to_point(2*i,14),plane.coords_to_point(2*(i+1),14))
          self.play(MoveAlongPath(dot, l1), rate_func=linear, run_time=1)
        
        
        
