#!/usr/bin/env python3

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance2(self, x, y):
        return (self.x-x)**2 + (self.y-y)**2

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


class Windmill:
    def __init__(self, x, y):
        self.center = Dot(x, y)
        self.bottom1 = Dot(0, 0)
        self.bottom2 = Dot(6000, 0)
        self.wings = []

    def __str__(self):
        s = "Windmill:\n"
        s += "Center: "+str(self.center)+"\n"
        s += "Bottom: "+str(self.bottom1)+" " + str(self.bottom2)
        s+="\nWings:\n"
        for w in self.wings:
            s += "\t"+str(w)

        return s

    def bottom_candidate(self, x, y):
        if (x < self.center.x):
            if (x > self.bottom1.x):
                self.bottom1 = Dot(x, y)
        else:
            if (x < self.bottom2.x):
                self.bottom2 = Dot(x, y)

    def wings_heuristic(self):
        d2M = .9*self.center.y**2
        d2m = 0.5*self.center.y**2
        return (d2m, d2M)

    def wing_candidate(self, x, y):
        d2 = self.center.distance2(x, y)
        (d2m, d2M) = self.wings_heuristic()
        if (d2 < d2M):
            if (d2 > d2m):
                self.wings.append(Dot(x, y))
                print(d2, d2m, d2M)


def main():
    pass


# if main call main
if __name__ == "__main__":
    main()
