import os
import bpy
import math
from mathutils import Vector
from tkblender import add_axis_helpers, look_at,m

k_iss_glb = r"blender/iss/org/International_Space_Station_ISS_A.glb"
k_earth_texture=r"povray/common/data/earth_surface_map.jpg"

def main():
    """Main function - orchestrates the entire scene creation and render."""
    scene = bpy.context.scene

    # Set output filename
    output_dir = os.path.join(os.environ.get('WORKDIR', '/tmp'), 'renders')
    os.makedirs(output_dir, exist_ok=True)
    scene.render.filepath = os.path.join(output_dir, "iss.png")

    # Render the scene
    bpy.ops.render.render(write_still=True)
    print("✅ Render finished! Image saved as iss.png")


# ======================
# Run the script
# ======================
if __name__ == "__main__":
    main()
