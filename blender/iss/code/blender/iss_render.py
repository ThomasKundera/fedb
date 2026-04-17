import os
import bpy
import math
from mathutils import Vector
from tkblender import add_axis_helpers, look_at,m,km, tk_earth_radius

k_fedb_dir = os.environ.get('FEDBDIR', '/tmp')

k_iss_glb = os.path.join(k_fedb_dir,"blender/iss/org/International_Space_Station_ISS_A.glb")
k_earth_texture = os.path.join(k_fedb_dir,"povray/common/data/earth_surface_map.jpg")

def clear_scene():
    """Remove all objects from the current scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def setup_world_background():
    """Set the world background to pure black (space-like dark)."""
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("World")
        bpy.context.scene.world = world

    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links

    # Clear existing nodes
    for node in list(nodes):
        nodes.remove(node)

    # Create a simple black background
    bg = nodes.new('ShaderNodeBackground')
    bg.inputs['Color'].default_value = (0.0, 0.0, 0.0, 1.0)   # pure black
    bg.inputs['Strength'].default_value = 1.0

    output = nodes.new('ShaderNodeOutputWorld')

    # Connect
    links.new(bg.outputs['Background'], output.inputs['Surface'])

def setup_space_ambient(strength=0.8, color=(0.02, 0.03, 0.08)):
    """
    Sets up soft ambient world lighting suitable for space scenes (ISS + Earth).
    Reduces harsh shadows from the Sun.
    """
    print("🌌 Setting up soft space ambient lighting...")

    # Get or create world
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("Space_World")
        bpy.context.scene.world = world

    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links

    # Clear any existing nodes
    for node in list(nodes):
        nodes.remove(node)

    # Background node (soft ambient)
    bg = nodes.new("ShaderNodeBackground")
    bg.location = (0, 0)
    bg.inputs["Color"].default_value = (*color, 1.0)   # RGB + Alpha
    bg.inputs["Strength"].default_value = strength

    # World Output
    output = nodes.new("ShaderNodeOutputWorld")
    output.location = (300, 0)

    # Connect
    links.new(bg.outputs["Background"], output.inputs["Surface"])

    print(f"   ✅ World ambient set (strength: {strength}, color: {color})")
    return world


def setup_camera(name,camloc, target):
    """Create and position the camera."""
    cam_data = bpy.data.cameras.new(name=name)

    # FOV
    cam_data.lens = 28
    #cam_data.lens = 50       # default
    # cam_data.lens = 85

    cam_obj = bpy.data.objects.new("Camera", cam_data)

    cam_obj.location = camloc
    look_at(cam_obj,camloc,target)

    cam_obj.data.clip_start = 10*m
    cam_obj.data.clip_end   = 20000*km

    bpy.context.scene.collection.objects.link(cam_obj)
    bpy.context.scene.camera = cam_obj

    return cam_obj


def setup_sun_light():
    """Add a weak sun light so the sphere shape remains visible."""
    light_data = bpy.data.lights.new(name="Sun", type='SUN')
    light_obj = bpy.data.objects.new("Sun", light_data)

    light_obj.location = (-8000*km, -3000*km, 10000*km)
    #light_obj.rotation_euler = (1, 0, 0)

    bpy.context.scene.collection.objects.link(light_obj)
    light_data.energy = 10.0


def create_earth(km=1.0, earth_texture_path=None):
    print("🌍 Creating Earth sphere...")

    # Recommended scale: keep everything inside safe precision range
    # Example: km=1 → 1 Blender Unit ≈ 10 km → Earth radius ≈ 637 units
    radius = tk_earth_radius

    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=radius,
        location=(0, 0, 0),
        segments=96,
        ring_count=48
    )
    earth = bpy.context.object
    earth.name = "Earth"

    # 1. Basic smooth shading
    bpy.ops.object.shade_smooth()

    # 2. Add proper "Smooth by Angle" modifier (the modern Auto Smooth)
    print("   Adding Smooth by Angle modifier (Auto Smooth)...")
    try:
        # This is the official way in Blender 4.2+
        bpy.ops.object.modifier_add_node_group(
            asset_library_type='ESSENTIALS',
            asset_library_identifier="",
            relative_asset_identifier="geometry_nodes\\smooth_by_angle.blend\\NodeTree\\Smooth by Angle"
        )

        # Get the modifier we just added
        mod = earth.modifiers.get("Smooth by Angle")
        if mod:
            # Set the smoothing angle (30° is excellent for a planet/sphere)
            mod["Input_1"] = math.radians(30)   # Change to 20-40 if needed
            print(f"   Smooth by Angle applied with 30° threshold")
        else:
            print("   ⚠️ Could not find modifier after adding")

    except Exception as e:
        print(f"   ⚠️ Failed to add via asset library: {e}")
        print("   Falling back to basic shade smooth only")

    # === Material setup ===
    mat = bpy.data.materials.new(name="Earth_Material")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    for node in list(nodes):
        nodes.remove(node)

    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.location = (0, 0)

    output = nodes.new("ShaderNodeOutputMaterial")
    output.location = (300, 0)

    tex = nodes.new("ShaderNodeTexImage")
    tex.location = (-300, 0)
    tex.interpolation = 'Cubic'

    if k_earth_texture and os.path.exists(k_earth_texture):
        print(f"   Loading Earth texture: {k_earth_texture}")
        tex.image = bpy.data.images.load(k_earth_texture)
        links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    else:
        print("   ⚠️ No texture provided → using fallback color")
        bsdf.inputs["Base Color"].default_value = (0.05, 0.15, 0.65, 1.0)

    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    # Assign material
    earth.data.materials.clear()
    earth.data.materials.append(mat)

    # Rotates for a nicer place
    earth.rotation_euler = (0,math.radians(35), 0)
    #earth.rotation_euler = (math.radians(-10), 0,0)
    print(f"   ✅ Earth created successfully (radius {radius:.1f} units)")
    return earth

def create_iss(iss_location):
    # Import the ISS GLB
    bpy.ops.import_scene.gltf(filepath=k_iss_glb)

    # Get the imported ISS objects (usually the top-level collection or main object)
    iss_objects = [obj for obj in bpy.context.selected_objects]
    if iss_objects:
        iss = iss_objects[0]
        iss.location = iss_location
        iss.scale = (100*m, 100*m, 100*m)


def setup_render_stamp():
    """Configure clean timestamp stamp (hide filename and scene name)."""
    scene = bpy.context.scene

    scene.render.use_stamp = True
    scene.render.use_stamp_date = True
    scene.render.use_stamp_time = True

    # Hide unwanted info
    scene.render.use_stamp_filename = False
    scene.render.use_stamp_scene = False
    scene.render.use_stamp_render_time = True
    scene.render.use_stamp_frame = False
    scene.render.use_stamp_camera = False
    scene.render.use_stamp_lens = False
    scene.render.use_stamp_marker = False

    # Visual settings
    scene.render.stamp_font_size = 12
    scene.render.stamp_foreground = (1.0, 1.0, 1.0, 1.0)
    scene.render.stamp_background = (0.0, 0.0, 0.0, 0.6)

    print("✅ Clean stamp enabled")


def main():
    """Main function - orchestrates the entire scene creation and render."""
    clear_scene()
    #setup_world_background()
    setup_space_ambient()
    setup_sun_light()

    #add_axis_helpers(length=1000*km,thickness=1*km, translate=(0,0,0))

    #iss_location=(10*km,0*km,5*km)
    #cam_loc = Vector(iss_location)+Vector((2*km,-50*km,2*km))
    #add_axis_helpers(length=1*km,thickness=10*m, translate=iss_location)
    #create_iss(iss_location)

    #setup_camera("camera",(1,-30,1),(0,0,0))
    #add_axis_helpers(translate=(5,0,0))
    create_earth()
    iss_location = (10*km, 10*km, tk_earth_radius+350*km)
    cam_loc = Vector(iss_location) + Vector((20*km,20*km,30*km))

    add_axis_helpers(length=20*km,thickness=100*m, translate=iss_location)

    create_iss(iss_location)
    #setup_camera("camera",(200*km,-19000*km,200*km),(0,0,0))
    setup_camera("camera",cam_loc,iss_location)

    # Set output filename
    scene = bpy.context.scene
    output_dir = os.path.join(os.environ.get('WORKDIR', '/tmp'), 'renders')
    os.makedirs(output_dir, exist_ok=True)
    scene.render.filepath = os.path.join(output_dir, "iss.png")

    # Render settings
    setup_render_stamp()

    # Render the scene
    bpy.ops.render.render(write_still=True)
    print("✅ Render finished! Image saved as iss.png")


# ======================
# Run the script
# ======================
if __name__ == "__main__":
    main()
