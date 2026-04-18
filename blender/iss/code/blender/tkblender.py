import math
from mathutils import Vector
import bpy

# Units
m=1./10000 # 1 unit is 10 km
m=1
km=1000.*m
ua=149597870700*m

tk_earth_radius = 6371*km

def look_at(camera_obj, camloc, target):
    """Make camera look at a target point (POV-Ray style).
    Fixed: properly handles looking down / up."""
    
    loc = camloc
    direction = Vector(target) - Vector(loc)

    print(f"Camera: {loc}, Target: {target}, Direction: {direction}")
    
    if direction.length < 1e-6:
        print("Warning: Camera and target at same position")
        return
    
    direction = direction.normalized()
    
    # Choose up axis dynamically to avoid flip when looking straight down/up
    if abs(direction.z) > 0.98:        # nearly vertical
        up_axis = 'Y'                  # use world Y as up
    else:
        up_axis = 'Y'                  # normal case: world Y as up (most stable)
    
    # Camera looks along -Z (Blender default)
    rot_quat = direction.to_track_quat('-Z', up_axis)
    camera_obj.rotation_euler = rot_quat.to_euler()


def add_axis_helpers(length=10.0, thickness=0.05, add_labels=True, translate=(0, 0, 0)):
    """
    Add renderable X/Y/Z axis lines with arrowheads and optional text labels.
    All parts are grouped under one parent Empty.
    translate = (x, y, z) moves the entire axis system.
    """
    tx, ty, tz = translate
    arrow_size = thickness * 2

    print(f"🛠️ Creating axis helpers at position {translate}...")

    # Create parent Empty at the desired location
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(tx, ty, tz))
    parent = bpy.context.active_object
    parent.name = "Axis_Helpers"
    parent.empty_display_size = length * 0.1

    # Material helper (good visibility in Solid + Rendered)
    def create_material(name, base_color, emission_strength=10.0):
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        for n in list(nodes):
            nodes.remove(n)

        bsdf = nodes.new('ShaderNodeBsdfPrincipled')
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = 0.0

        emission = nodes.new('ShaderNodeEmission')
        emission.inputs['Color'].default_value = base_color
        emission.inputs['Strength'].default_value = emission_strength

        mix = nodes.new('ShaderNodeMixShader')
        mix.inputs['Fac'].default_value = 0.7

        output = nodes.new('ShaderNodeOutputMaterial')

        links.new(bsdf.outputs['BSDF'], mix.inputs[1])
        links.new(emission.outputs['Emission'], mix.inputs[2])
        links.new(mix.outputs['Shader'], output.inputs['Surface'])
        return mat

    # Helper to create one axis
    def create_axis_part(name, color, line_rotation, arrow_rotation):
        # Main axis line (cylinder) - offset from translate
        bpy.ops.mesh.primitive_cylinder_add(
            radius=thickness,
            depth=length,
            location=(0, 0, 0),
            rotation=line_rotation
        )
        line = bpy.context.active_object
        line.name = f"Axis_{name}"
        line.data.materials.append(create_material(f"Mat_Axis_{name}", color))
        line.parent = parent
        return
        # Arrowhead at the positive end
        arrow_pos = (length/2 if name == "X" else 0,
                     length/2 if name == "Y" else 0,
                     length/2 if name == "Z" else 0)

        bpy.ops.mesh.primitive_cone_add(
            radius1=arrow_size,
            depth=arrow_size * 2,
            location=arrow_pos,
            rotation=arrow_rotation
        )
        cone = bpy.context.active_object
        cone.name = f"Arrow_{name}"
        cone.data.materials.append(create_material(f"Mat_Arrow_{name}", color, 14.0))
        cone.parent = parent

    # Create the three axes
    create_axis_part("X", (1.0, 0.1, 0.1, 1.0), (0, math.radians(90), 0), (0, math.radians(90), 0))
    #create_axis_part("Y", (0.1, 1.0, 0.1, 1.0), (math.radians(-90), 0, 0), (math.radians(-90), 0, 0))
    #create_axis_part("Z", (0.1, 0.1, 1.0, 1.0), (0, 0, 0), (0, 0, 0))

    # Optional labels
    if add_labels:
        def create_label(text, offset, color):
            loc = (tx + offset[0], ty + offset[1], tz + offset[2])
            bpy.ops.object.text_add(location=loc)
            txt = bpy.context.active_object
            txt.name = f"Label_{text}"
            txt.data.body = text
            txt.data.size = length * 0.018
            txt.data.align_x = 'CENTER'
            txt.data.align_y = 'CENTER'
            txt.rotation_euler = (math.radians(90), 0, 0)

            mat = create_material(f"Mat_Label_{text}", color, 18.0)
            txt.data.materials.append(mat)
            txt.parent = parent

        create_label("X", (length/2 + 2.0, 0, 0), (1.0, 0.3, 0.3, 1.0))
        create_label("Y", (0, length/2 + 2.0, 0), (0.3, 1.0, 0.3, 1.0))
        create_label("Z", (0, 0, length/2 + 2.0), (0.3, 0.3, 1.0, 1.0))

    # Move the parent to the desired location
    parent.location = translate

    print(f"✅ Axis helpers created at {translate}. Parent: Axis_Helpers")
    return parent
