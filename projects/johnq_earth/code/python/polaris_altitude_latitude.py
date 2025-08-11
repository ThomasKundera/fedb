#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Constants
miles_per_degree = 69  # Miles per degree of latitude
north_pole_latitude = 90  # North Pole latitude in degrees

# Function to plot triangle for a given elevation angle (latitude) and color
def plot_triangle(ax, angle, color):
    # Convert angle to radians
    elevation_angle = np.radians(angle)
    
    # Calculate distances
    # Ground distance (NP-O): Distance from North Pole (90°) to observation point (angle°)
    ground_distance = (north_pole_latitude - angle) * miles_per_degree
    # Altitude of Polaris (P-NP): Vertical distance above North Pole
    altitude_polaris = ground_distance * np.tan(elevation_angle)
    # Line-of-sight distance (P-O): From observation point to Polaris
    line_of_sight = ground_distance / np.cos(elevation_angle)
    
    # Coordinates for the triangle
    points = {
        'NP': (0, 0),  # North Pole
        'O': (ground_distance, 0),  # Observation point
        'P': (0, altitude_polaris)  # Polaris
    }
    
    # Plot the triangle lines
    ax.plot([points['NP'][0], points['O'][0]], [points['NP'][1], points['O'][1]], 
            color=color, linestyle='-', label=f'NP-O ({angle}°, {ground_distance:.0f} miles)')
    ax.plot([points['O'][0], points['P'][0]], [points['O'][1], points['P'][1]], 
            color=color, linestyle='--', label=f'P-O ({angle}°, {line_of_sight:.0f} miles)')
    ax.plot([points['P'][0], points['NP'][0]], [points['P'][1], points['NP'][1]], 
            color=color, linestyle=':', label=f'P-NP ({angle}°, {altitude_polaris:.0f} miles)')
    
    # Plot points
    for point, (x, y) in points.items():
        ax.scatter(x, y, color='black', s=50, zorder=5)
        ax.text(x, y, point, fontsize=10, ha='right', va='bottom')
    
    # Label distances (positioned near midpoints)
    mid_np_o = ((points['NP'][0] + points['O'][0]) / 2, (points['NP'][1] + points['O'][1]) / 2)
    ax.text(mid_np_o[0], mid_np_o[1] + 100, f'{ground_distance:.0f} miles', 
            color=color, ha='center', fontsize=8)
    mid_p_o = ((points['P'][0] + points['O'][0]) / 2, (points['P'][1] + points['O'][1]) / 2)
    ax.text(mid_p_o[0] + 150, mid_p_o[1], f'{line_of_sight:.0f} miles', 
            color=color, ha='left', fontsize=8)
    mid_p_np = ((points['P'][0] + points['NP'][0]) / 2, (points['P'][1] + points['NP'][1]) / 2)
    ax.text(mid_p_np[0] + 150, mid_p_np[1], f'{altitude_polaris:.0f} miles', 
            color=color, ha='left', fontsize=8)
    
    # Add angle annotation at point O
    arc_radius = 300  # Radius of the arc in miles
    # Arc from (180° - angle) to 180° to align with the direction towards North (negative x)
    angle_arc = Arc(points['O'], arc_radius * 2, arc_radius * 2, 
                    theta1=180 - angle, theta2=180, color=color, linestyle='--')
    ax.add_patch(angle_arc)
    # Label the angle at the midpoint of the arc
    midpoint_angle = 180 - (angle / 2)
    ax.text(points['O'][0] + arc_radius * np.cos(np.radians(midpoint_angle)), 
            points['O'][1] + arc_radius * np.sin(np.radians(midpoint_angle)), 
            f'{angle}°', color=color, fontsize=8, ha='center', va='center')
    
    return ground_distance, altitude_polaris, line_of_sight

# Set up the plot with fixed scale
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlabel('Ground Distance (miles)')
ax.set_ylabel('Altitude (miles)')
ax.set_title('Triangle: Polaris, North Pole, Observation Location (Flat Earth)')
ax.set_xlim(-100, 4500) 
ax.set_ylim(-100, 6000)  # Vertical: around 12000 miles
ax.grid(True)

# Plot triangle for 60° (and optionally others)
distances = plot_triangle(ax, angle=60, color='blue')
plot_triangle(ax, angle=45, color='orange')
plot_triangle(ax, angle=30, color='red')
plot_triangle(ax, angle=80, color='green')


# Add legend
ax.legend()

# Show plot
plt.show()

# Print distances for reference
print(f"Ground Distance (NP-O, 60°): {distances[0]:.0f} miles")
print(f"Altitude of Polaris (P-NP, 60°): {distances[1]:.0f} miles")
print(f"Line-of-Sight Distance (P-O, 60°): {distances[2]:.0f} miles")

# Print distances for reference (in km)
print(f"Ground Distance (NP-O, 60°): {distances[0] * 1.60934:.0f} km")
print(f"Altitude of Polaris (P-NP, 60°): {distances[1] * 1.60934:.0f} km")
print(f"Line-of-Sight Distance (P-O, 60°): {distances[2] * 1.60934:.0f} km")

# Save plot
fig.savefig('polaris_altitude_latitude.png')


