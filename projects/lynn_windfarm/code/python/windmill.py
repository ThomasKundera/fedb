#!/usr/bin/env python3
import math
import numpy as np

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
        self.inferred = inferred
        self.possible_mill = []
        self.idx = Wing.idx
        Wing.idx += 1

    def mill_candidate(self, m):
        self.possible_mill.append(m)


class Yellow:
    def __init__(self):
        self.l=TwoDots(Dot(0,0),Dot(0,0))
        self.r=TwoDots(Dot(6000,0),Dot(6000,0))

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
    
    def get_bottom(self):
        xl=(self.l.d1.x+self.l.d2.x)/2
        yl=min(self.l.d1.y,self.l.d2.y)
        xr=(self.r.d1.x+self.r.d2.x)/2
        yr=min(self.r.d1.y,self.r.d2.y)
        ym=(yl+yr)/2
        return (Dot(xl,ym),Dot(xr,ym))

    def draw(self, plt, ax):
        ax.add_patch(plt.Line2D((self.l.d1.x, self.l.d2.x), (self.l.d1.y, self.l.d2.y), color="yellow"))
        ax.add_patch(plt.Line2D((self.r.d1.x, self.r.d2.x), (self.r.d1.y, self.r.d2.y), color="yellow"))

class Windmill:
    idx = 0

    def __init__(self, horizon, x, y):
        self.horizon = horizon
        self.center = Dot(x, y)
        self.bottom1 = Dot(0, 0)
        self.bottom2 = Dot(6000, 0)
        self.yellow = None
        self.wings = []
        self.wangle = None
        self.wmean = None
        self.idx = Windmill.idx
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
                ax.add_patch(plt.Circle((p.x, p.y), 0.1*self.wmean, color="red", fill=False))
                ax.plot([self.center.x, p.x], [self.center.y, p.y], color="red")
        ax.plot([self.center.x, self.bottom1.x], [
            self.center.y, self.bottom1.y], color="white")
        ax.plot([self.center.x, self.bottom2.x], [
                self.center.y, self.bottom2.y], color="white")
        for w in self.wings:
            ax.plot([self.center.x, w.x], [self.center.y, w.y], color="white")
   
        if (self.yellow):
            self.yellow.draw(plt, ax)


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
            self.bottom1, self.bottom2 = self.yellow.get_bottom()


    def wings_distance_heuristic(self):
        hdata=[178,127,720]
        ldata=[208,190,482]
        z=np.polyfit(hdata, ldata, 2)
        p = np.poly1d(z)
        h = math.fabs(self.center.y-self.horizon.predict_y([self.center.x])[0])
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
            if (w.distance2(p.x, p.y) < (0.1*self.wmean)**2):
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
        #for w in self.wings:
        #    if ((math.sqrt(w.distance2(self.center.x, self.center.y))-l)/l > .1):
        #        print("Wings length is incoherent")
        #    else:
        #        print("Wings length is: "+str(l))
        #a = 0
        #for w in self.wings:
        #    a += (math.atan2(w.y-self.center.y,
        #          w.x-self.center.x)) % (2*math.pi/3)
        #self.wangle = a
        #print("Angle between wings: "+str(self.wangle*180/math.pi))

class FakeWindmill(Windmill):
    def __init__(self, horizon, x, y):
        super(FakeWindmill, self).__init__(horizon, x, y)
    
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

    def settle(self):
        self.wmean = 0
        if (len(self.wings) == 0):
            print("No wings found")
        elif (len(self.wings) > 3):
            print("Too many wings found")
        else:
            # Compute average wing length
            l = 0
            for w in self.wings:
                l += math.sqrt(w.distance2(self.center.x, self.center.y))
            l /= len(self.wings)
            self.wmean = l
            # Test wings being about same length
            for w in self.wings:
                if ((math.sqrt(w.distance2(self.center.x, self.center.y))-l)/l > .1):
                    print("Wings length is incoherent")
                else:
                    print("Wings length is: "+str(l))

            # Compute angle between wings
            if (len(self.wings) == 2):
                a = math.atan2(
                    self.wings[1].y-self.wings[0].y, self.wings[1].x-self.wings[0].x)
                print("Angle between wings: "+str(a*180/math.pi))
            # Compute distance between the two wings
