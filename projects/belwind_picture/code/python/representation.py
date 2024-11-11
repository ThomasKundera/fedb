#!/usr/bin/env python3
from object_size import measuredsizearray

# Make a matplotlib figure of the belwind picture
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
ax.set_xlim(0, 4490)
ax.set_ylim(0, 3215)
for name, x1, y1, x2, y2 in measuredsizearray:
    rect = patches.Rectangle((x1, 3215-y1), (x2-x1), (y1-y2), linewidth=0, edgecolor='r', facecolor='red')
    ax.add_patch(rect)
    #ax.text((x1+x2)/2, 3215-(y1+y2)/2, name, ha='center', va='center', fontsize=8)

# Save plot preserving aspect ratio, using 1200 px width for x axis
#fig.set_dpi(1200)
ax.set_aspect('equal', adjustable='box')


# Save plot
fig.savefig('belwind.png', dpi=600, bbox_inches='tight')

#plt.show()

