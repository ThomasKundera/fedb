#!/usr/bin/env python3

from geopy import distance
import matplotlib.pyplot as plt
import numpy as np

def gc_distance(p1,p2):
    return distance.great_circle(p1,p2)

citydict={
    'Paris':(48.8566, 2.3522),
    'Le_Cap':(-33.925278, 18.423056),
    'Sydney':(-33.856111,151.1925),
    'Osaka':(34.693611,135.5025),
}

def print_distances(City1,City2):
    print(City1+" to "+City2+" is "+str(gc_distance(datdict[City1],datdict[City2])))
    
def add_dist(distlist,City1,City2):
    distlist.append([City1,City2,gc_distance(datdict[City1],datdict[City2])])

def plot_cities(distlist):
    # Create a graph from the distance list
    n = len(distlist)
    graph = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            graph[i, j] = graph[j, i] = distlist[i*n+j]

    # Use the force-directed algorithm to compute the new positions of the cities
    cities = np.zeros((n, 2))
    for _ in range(100):
        delta = np.zeros((n, 2))
        for i in range(n):
            for j in range(i+1, n):
                force = (graph[i, j] - np.linalg.norm(cities[i] - cities[j])) * (cities[j] - cities[i]) / graph[i, j]**2
                delta[i] += force
                delta[j] -= force
        cities += delta

    # Plot the cities
    fig, ax = plt.subplots()
    ax.scatter([city[0] for city in cities], [city[1] for city in cities], color='blue', label='Cities')
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cities and Repulsion Forces')
    plt.show()

def test():
    print_distances("Paris","Le_Cap")
    print_distances("Le_Cap","Sydney")
    print_distances("Sydney","Osaka")
    print_distances("Osaka","Paris")
    print_distances("Paris","Sydney")

def main():
    distlist=[]
    add_dist(distlist,"Paris","Le_Cap")
    plot_cities(distlist)
    return
    test()

if __name__ == "__main__":
    main()