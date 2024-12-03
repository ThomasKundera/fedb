#!/usr/bin/env python3
import math


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance2(self, x, y):
        return (self.x-x)**2 + (self.y-y)**2

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


class Windmill:
    def __init__(self, horizon, x, y):
        self.horizon = horizon
        self.center = Dot(x, y)
        self.bottom1 = Dot(0, 0)
        self.bottom2 = Dot(6000, 0)
        self.wings = []

    def __str__(self):
        s = "Windmill:\n"
        s += "Center: "+str(self.center)+"\n"
        s += "Bottom: "+str(self.bottom1)+" " + str(self.bottom2)
        s += "\nWings:\n"
        for w in self.wings:
            s += "\t"+str(w)
        return s

    def draw(self, plt, ax):
        ax.plot([self.center.x, self.bottom1.x], [
                self.center.y, self.bottom1.y], color="white")
        ax.plot([self.center.x, self.bottom2.x], [
                self.center.y, self.bottom2.y], color="white")
        for w in self.wings:
            ax.plot([self.center.x, w.x], [self.center.y, w.y], color="white")
        if (not self.wmean):
            d2m,d2M = self.wings_heuristic()
            # Plot circle around mean of wings
            ax.add_patch(
                plt.Circle((self.center.x, self.center.y), math.sqrt(d2m), color="red", fill=False))
            ax.add_patch(
                plt.Circle((self.center.x, self.center.y), math.sqrt(d2M), color="red", fill=False))

    def bottom_candidate(self, x, y):
        if (x < self.center.x):
            if (x > self.bottom1.x):
                self.bottom1 = Dot(x, y)
        else:
            if (x < self.bottom2.x):
                self.bottom2 = Dot(x, y)

    def wings_heuristic(self):
        h = self.center.y-self.horizon.predict_y([self.center.x])[0]
        d2M = 3*h*h
        d2m = 0.9*h*h
        return (d2m, d2M)

    def wing_candidate(self, x, y):
        d2 = self.center.distance2(x, y)
        (d2m, d2M) = self.wings_heuristic()
        print(d2, d2m, d2M)
        if (d2 < d2M):
            if (d2 > d2m):
                self.wings.append(Dot(x, y))

    def settle(self):
        self.wmean=0
        if (len(self.wings) == 0):
            print("No wings found")
        elif (len(self.wings) >3):
            print("Too many wings found")
        else:
            # Compute average wing length
            l = 0
            for w in self.wings:
                l += math.sqrt(w.distance2(self.center.x, self.center.y))
            l /= len(self.wings)
            self.wmean=l
            # Test wings being about same length
            for w in self.wings:
                if ((math.sqrt(w.distance2(self.center.x, self.center.y))-l)/l > .1):
                    print("Wings length is incoherent")
                else:
                    print("Wings length is: "+str(l))

            # Compute angle between wings
            if (len(self.wings) == 2):
                a = math.atan2(self.wings[1].y-self.wings[0].y, self.wings[1].x-self.wings[0].x)
                print("Angle between wings: "+str(a*180/math.pi))
            # Compute distance between the two wings

def main():
    pass


# if main call main
if __name__ == "__main__":
    main()
