#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Create a polar plot
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='polar')

# Primary grid settings
r_max_primary = 180  # Maximum radius for primary grid
theta = np.linspace(0, 2 * np.pi, 100)  # Full circle (0 to 2π)

# Set primary grid
ax.set_rlim(0, r_max_primary)  # Primary radius limit
ax.set_rticks(np.arange(0, r_max_primary + 1, 30))  # Radial grid lines every 30 units
ax.set_thetagrids(np.arange(0, 360, 30))  # Angular grid lines every 30 degrees
ax.grid(True, color='black', linestyle='-', alpha=0.5)  # Primary grid in black

# Secondary grid settings
r_max_secondary = 12420  # Maximum radius for secondary grid
scale_factor = r_max_primary / r_max_secondary  # Scale 12420 to map to 180

# Create secondary grid (scaled to overlay on primary)
r_ticks_secondary = np.arange(0, r_max_secondary + 1, 2070)  # Secondary radial grid every ~2070 units (scaled equivalent of 30)
r_ticks_scaled = r_ticks_secondary * scale_factor  # Scale to primary grid's coordinates

# Overlay secondary radial grid lines in red
for r in r_ticks_scaled:
    ax.plot(theta, np.full_like(theta, r), color='red', linestyle='--', alpha=0.7)

# Add secondary radial labels (optional, scaled to primary grid)
for r, r_scaled in zip(r_ticks_secondary, r_ticks_scaled):
    ax.text(0, r_scaled, f'{int(r)}', color='red', fontsize=8, ha='center', va='bottom')

# Add labels and title
ax.set_title("Polar Coordinate Grid with Dual Scales", pad=20)

# Show the plot
plt.show()
