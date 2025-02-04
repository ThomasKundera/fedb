#!/usr/bin/env python3
import math
import numpy as np

from tkunits import m,km

from size_n_angles import pxtoangle, angletodistance, side_angle

kWing_length_Lynn=(107.0/2) * m
kWing_length_Race=(154.0/2) * m


def wing_search_radius(l):
    return 5*math.sqrt(l/10)

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance2(self, x, y):
        return (self.x-x)**2 + (self.y-y)**2

    def distance(self, x, y):
        return math.sqrt(self.distance2(x, y))

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    # To be able to sort dots
    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __ge__(self, other):
        return self.x >= other.x

    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return self.x != other.x


class TwoDots:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

class Wing(Dot):
    idx = 0

    def __init__(self, x, y, inferred=False):
        super().__init__(x, y)
        self.possible_mill = []
        self.idx = Wing.idx
        Wing.idx += 1

    def mill_candidate(self, m):
        self.possible_mill.append(m)


class Yellow:
    def __init__(self):
        self.l=TwoDots(Dot(0,0),Dot(0,0))
        self.r=TwoDots(Dot(10000,0),Dot(10000,0))

    def evaluate_left(self,x,y):
        d=Dot(x,y)
        l=[d,self.l.d1,self.l.d2]
        l.sort()
        self.l.d1=l[1]
        self.l.d2=l[2]

    def evaluate_right(self,x,y):
        d=Dot(x,y)
        r=[d,self.r.d1,self.r.d2]
        r.sort()
        self.r.d1=r[0]
        self.r.d2=r[1]
    
    def get_top(self):
        xl=(self.l.d1.x+self.l.d2.x)/2
        yl=min(self.l.d1.y,self.l.d2.y)
        xr=(self.r.d1.x+self.r.d2.x)/2
        yr=min(self.r.d1.y,self.r.d2.y)
        ym=(yl+yr)/2
        return (Dot(xl,ym),Dot(xr,ym))

    def get_bottom(self):
        xl=(self.l.d1.x+self.l.d2.x)/2
        yl=max(self.l.d1.y,self.l.d2.y)
        xr=(self.r.d1.x+self.r.d2.x)/2
        yr=max(self.r.d1.y,self.r.d2.y)
        ym=(yl+yr)/2
        return (Dot(xl,ym),Dot(xr,ym))

    def get_height(self):
        yt=min(self.l.d1.y,self.l.d2.y)
        yb=max(self.r.d1.y,self.r.d2.y)
        return yb-yt

    def get_width(self):
        xl=math.fabs(self.l.d1.x+self.l.d2.x)/2
        xr=math.fabs(self.r.d1.x+self.r.d2.x)/2
        return xr-xl

    def draw(self, plt, ax):
        ax.add_patch(plt.Line2D((self.l.d1.x, self.l.d2.x), (self.l.d1.y, self.l.d2.y), color="yellow"))
        ax.add_patch(plt.Line2D((self.r.d1.x, self.r.d2.x), (self.r.d1.y, self.r.d2.y), color="yellow"))

class Windmill:
    idx = 0

    def __init__(self, horizon, x, y):
        self.fake = False
        self.horizon = horizon
        self.center = Dot(x, y)
        self.bottom1 = Dot(0, 0)
        self.bottom2 = Dot(10000, 0)
        self.yellow = None
        self.wings = []
        self.wangle = None
        self.wmean = None
        self.idx = Windmill.idx
        self.h=None
        self.distance=0
        Windmill.idx += 1

    def __str__(self):
        s = "Windmill:\n"
        s += "Center: "+str(self.center)+"\n"
        s += "Bottom: "+str(self.bottom1)+" " + str(self.bottom2)
        s += "\nWings:\n"
        for w in self.wings:
            s += "\t"+str(w)
        return s

    def draw(self, plt, ax):
        if (not self.wmean):
            d2m, d2M = self.wings_distance_heuristic()
            # Plot circle around mean of wings
            ax.add_patch(
                plt.Circle((self.center.x, self.center.y), math.sqrt(d2m), color="red", fill=False))
            ax.add_patch(
                plt.Circle((self.center.x, self.center.y), math.sqrt(d2M), color="red", fill=False))
        if (self.wangle != None):
            for i in range(3):
                a = self.wangle+i*2*math.pi/3
                p = Dot(self.center.x+math.cos(a)*self.wmean,
                        self.center.y+math.sin(a)*self.wmean)
                ax.add_patch(plt.Circle((p.x, p.y), wing_search_radius(self.wmean), color="red", fill=False))
                ax.plot([self.center.x, p.x], [self.center.y, p.y], color="red")
        ax.plot([self.center.x, self.bottom1.x], [
            self.center.y, self.bottom1.y], color="white")
        ax.plot([self.center.x, self.bottom2.x], [
                self.center.y, self.bottom2.y], color="white")
        for w in self.wings:
            ax.plot([self.center.x, w.x], [self.center.y, w.y], color="white")
   
        if (self.yellow):
            self.yellow.draw(plt, ax)
            #if (self.h):
            #    ax.text(self.yellow.l.d1.x, self.yellow.get_bottom()[0].y, str(int(self.h)), color="yellow")

        # Print distance
        if (self.wmean):
            ax.text(self.center.x, self.center.y,
                   str(int(self.distance/km))+" km", color="black")

    def to_povray(self):
        if (self.distance < 15*km):
            s="windmill_sw37"
        else:
            s="windmill_sw60"
        s += " ("+ str(self.x_simple) + ", " + str(self.y_simple) + "," + str(180*self.wangle/math.pi) +")\n"
        return s


    def bottom_candidate(self, x, y):
        if (x < self.center.x):
            if (x > self.bottom1.x):
                self.bottom1 = Dot(x, y)
        else:
            if (x < self.bottom2.x):
                self.bottom2 = Dot(x, y)

    def bottom_candidate_yellow(self, x, y):
        if (x < self.center.x):
            if (x > self.bottom1.x):
                if (not self.yellow):
                    self.yellow = Yellow()
                self.yellow.evaluate_left(x, y)
        else:
            if (x < self.bottom2.x):
                if (not self.yellow):
                    self.yellow = Yellow()
                self.yellow.evaluate_right(x, y)
        if (self.yellow):
            self.bottom1, self.bottom2 = self.yellow.get_top()


    def wings_distance_heuristic(self):
        hdata=[178,127,720,834,894]
        ldata=[208,190,482,575,620]
        z=np.polyfit(hdata, ldata, 3)
        p = np.poly1d(z)
        self.local_horizon = self.horizon(self.center.x)
        #print("self.local_horizon = " + str(self.local_horizon))
        h = math.fabs(self.center.y-self.local_horizon)
        d2M = 1.2*p(h)*p(h)
        d2m = 0.8*p(h)*p(h)
        #print("p( "+str(h)+" ) = ",str(p(h)))
        return (d2m, d2M)

    def wings_angle_heuristic(self):
        pl = []
        for i in range(3):
            a = self.wangle+i*2*math.pi/3
            p = Dot(self.center.x+math.cos(a)*self.wmean,
                    self.center.y+math.sin(a)*self.wmean)
            pl.append(p)
        return (pl)

    def wing_candidate(self, w):
        if (len(self.wings) == 0):
            d2 = self.center.distance2(w.x, w.y)
            (d2m, d2M) = self.wings_distance_heuristic()
            #print(d2, d2m, d2M)
            if (d2 < d2M):
                if (d2 > d2m):
                    return True
            return False
        pl = self.wings_angle_heuristic()
        for p in pl:
            if (w.distance2(p.x, p.y) < (wing_search_radius(self.wmean))**2):
                return True
        return False

    def add_wing(self, w):
        if (len(self.wings) == 0):
            self.wings.append(w)
            a=(math.atan2(w.y-self.center.y, w.x-self.center.x)) % (2*math.pi/3)
            self.wangle = a
        if (w not in self.wings):
            self.wings.append(w)
        self.wingstuffing()

    def wingstuffing(self):
        l = 0
        for w in self.wings:
            l += math.sqrt(w.distance2(self.center.x, self.center.y))
        l /= len(self.wings)
        self.wmean = l
 
    def compute_depth_distance(self):
        a=pxtoangle(self.wmean)
        #print("Angle: " + str(a))
        self.distance=angletodistance(a,kWing_length_Lynn)
        if (self.distance>15*km): # Not Lynn, byt Race
            self.distance=angletodistance(a,kWing_length_Race)
        #print("Distance: " + str(self.distance/km)+" km")

    def compute_simple_coordinates(self):
        a=side_angle(self.center.x)
        self.x_simple=self.distance*math.sin(a)
        self.y_simple=self.distance*math.cos(a)

    def compute_size(self):
        scale=kWing_length_Lynn/self.wmean
        self.yellow_height=scale*(self.yellow.get_height())
        self.yellow_width=scale*(self.yellow.get_width())
        self.white_height=scale*(self.local_horizon-self.center.y)

    def compute_distances(self):
        # The following line shouldn't be needed
        self.local_horizon = self.horizon(self.center.x)
 
        self.compute_depth_distance()
        self.compute_simple_coordinates()
        if (self.yellow):
            bottom=self.yellow.get_bottom()[0].y
            h = self.local_horizon-bottom
            #print("h = " + str(h))
            self.h=h
            if (h<-6):
                self.beyond_horizon = False
                self.compute_size()
            else:
                self.beyond_horizon = True


class FakeWindmill(Windmill):
    def __init__(self, horizon, x, y):
        super(FakeWindmill, self).__init__(horizon, x, y)
        self.fake=True
    
    def set_color(self, color):
        self.color = color

    def draw(self, plt, ax):
        ax.add_patch(plt.Circle((self.center.x, self.center.y), 
        10, color=self.color, fill=False))

def main():
    pass


# if main call main
if __name__ == "__main__":
    main()
