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
    print(City1+" to "+City2+" is "+str(gc_distance(citydict[City1],citydict[City2])))
    
def add_dist(distlist,City1,City2):
    distlist.append([City1,City2,gc_distance(citydict[City1],citydict[City2]).km])

def plot_cities(citylist):
    # Create a graph from the distance list
    n = len(citylist)
    graph = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            graph[i, j] = graph[j, i] = gc_distance(citydict[citylist[i]],citydict[citylist[j]]).km

    print (graph)
    # Use the force-directed algorithm to compute the new positions of the cities
    #cities = np.zeros((n, 2))
    cities = np.random.rand(n, 2)*1000
    for _ in range(1000):
        delta = np.zeros((n, 2))
        for i in range(n):
            for j in range(i+1, n):
                dist = np.linalg.norm(cities[i] - cities[j])
                force = (graph[i, j] - dist) / dist
                force = 1*force
                delta[i] += force
                delta[j] -= force
                if _%100 == 0:
                    # print dist and force
                    print("-------------------")
                    print("{} to {}: dist={}, force={}".format(citylist[i], citylist[j], dist, force))
        cities += delta
        #if _%100 == 0: print (cities)

    # Plot the cities
    fig, ax = plt.subplots()
    ax.scatter([city[0] for city in cities], [city[1] for city in cities], color='blue', label='Cities')
    for i, city in enumerate(cities):
        # Add a text label to the plot with the city name
        ax.text(city[0], city[1], citylist[i], fontsize=12, color='black', ha='center')
    for i in range(n):
        for j in range(i+1, n):
            # Compute the normalized distance between the current and next city
            dist = graph[i, j]
            expected_dist = np.linalg.norm(cities[i] - cities[j])
            norm_dist = 100*abs(dist - expected_dist) / expected_dist
            # Draw a line between the current and next city with a color based on the normalized distance plt.cm.jet(norm_dist)
            ax.plot([cities[i][0], cities[j][0]], [cities[i][1], cities[j][1]], color=plt.cm.jet(norm_dist), label='Repulsion Force: {:.2f}'.format(norm_dist*100), linewidth=2)
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
    citylist=["Paris","Le_Cap","Sydney"]
    #,"Sydney","Osaka"]
    plot_cities(citylist)
    return
    test()

if __name__ == "__main__":
    main()