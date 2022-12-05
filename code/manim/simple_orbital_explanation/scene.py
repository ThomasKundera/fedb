from manim import *

class mYNumberPlane(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-2, 28, 2),y_range=(-2, 18, 2),x_length=15, y_length=9)
        axes = plane.get_axes()
        #x_axis = axes[0]
        #y_axis = axes[1]
        plane.add_coordinates()
        #x_axis.add_coordinates()
        #y_axis.add_coordinates()
        #ax = Axes(unit_size=1)
        text = Text('Conservation of momentum').scale(2)
        self.add(text)
        self.wait(2)
        self.remove(text)
        dot = Dot(plane.coords_to_point(0,14), color=GREEN)
        
        l1 = Line(plane.coords_to_point(0,14),plane.coords_to_point(2,14))
        
        
        #ax = Axes(x_range=(-1,20,1)).add_coordinates()

        # a dot with respect to the axes
        #dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        #lines = ax.get_lines_to_point(ax.c2p(2,2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        #plane = NumberPlane()
        #plane.align_to(ax)
        #dot_scene = Dot((2,2,0), color=RED)

        self.add(plane,dot) #, dot_scene, ax, dot_axes, lines)
        
        for i in range(10):
          dot = Dot(plane.coords_to_point(2*i,14), color=GREEN)
          l1 = Line(plane.coords_to_point(2*i,14),plane.coords_to_point(2*(i+1),14))
          self.play(MoveAlongPath(dot, l1), rate_func=linear)
        
        
        
