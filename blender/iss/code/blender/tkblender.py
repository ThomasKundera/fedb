import math
from mathutils import Vector
import bpy

# Units
m=1
km=1000.*m
ua=149597870700*m

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
    

def add_axis_helpers(length=50.0, thickness=0.05, arrow_size=0.3, add_labels=True):
    """Add renderable X/Y/Z axis lines with arrowheads and optional text labels.
    
    Parameters:
        length (float): Total length of each axis line
        thickness (float): Diameter of the axis lines
        arrow_size (float): Size of the arrowhead cones
        add_labels (bool): Whether to add "X", "Y", "Z" text labels
    """
    collection = bpy.context.scene.collection
    
    # Helper to create a thin cylinder for the axis line
    def create_axis(name, color, direction):
        # Cylinder (main line)
        bpy.ops.mesh.primitive_cylinder_add(
            radius=thickness,
            depth=length,
            location=(0, 0, 0),
            rotation=direction
        )
        axis = bpy.context.active_object
        axis.name = name
        
        # Simple emissive material so it glows a bit and is easy to see
        mat = bpy.data.materials.new(name=f"Axis_{name}")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        for node in list(nodes):
            nodes.remove(node)
        
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs['Color'].default_value = color
        emission.inputs['Strength'].default_value = 10.0
        
        output = nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.links.new(emission.outputs['Emission'], output.inputs['Surface'])
        
        axis.data.materials.append(mat)
        collection.objects.link(axis)  # ensure it's in scene
        return axis

    # X axis (red) - along positive X
    rot_x = (0, math.radians(90), 0)
    x_axis = create_axis("Axis_X", (1.0, 0.0, 0.0, 1.0), rot_x)
    
    # Y axis (green) - along positive Y
    rot_y = (math.radians(-90), 0, 0)
    y_axis = create_axis("Axis_Y", (0.0, 1.0, 0.0, 1.0), rot_y)
    
    # Z axis (blue) - along positive Z
    rot_z = (0, 0, 0)
    z_axis = create_axis("Axis_Z", (0.0, 0.0, 1.0, 1.0), rot_z)

    # Add arrowheads (cones) at the end of each axis
    def add_arrowhead(name, location, rotation, color):
        bpy.ops.mesh.primitive_cone_add(
            radius1=arrow_size,
            depth=arrow_size * 2,
            location=location,
            rotation=rotation
        )
        cone = bpy.context.active_object
        cone.name = f"Arrow_{name}"
        
        mat = bpy.data.materials.new(name=f"Arrow_{name}")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        for n in list(nodes): nodes.remove(n)
        em = nodes.new('ShaderNodeEmission')
        em.inputs['Color'].default_value = color
        em.inputs['Strength'].default_value = 15.0
        out = nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.links.new(em.outputs['Emission'], out.inputs['Surface'])
        
        cone.data.materials.append(mat)
        collection.objects.link(cone)

    # Arrowheads
    add_arrowhead("X", (length/2, 0, 0), (0, math.radians(90), 0), (1.0, 0.0, 0.0, 1.0))
    add_arrowhead("Y", (0, length/2, 0), (math.radians(-90), 0, 0), (0.0, 1.0, 0.0, 1.0))
    add_arrowhead("Z", (0, 0, length/2), (0, 0, 0), (0.0, 0.0, 1.0, 1.0))

    # Optional text labels (always face camera approximately)
    if add_labels:
        def create_label(text, location, color):
            bpy.ops.object.text_add(location=location)
            txt = bpy.context.active_object
            txt.name = f"Label_{text}"
            txt.data.body = text
            txt.data.size = 0.6
            txt.data.align_x = 'CENTER'
            txt.data.align_y = 'CENTER'
            
            mat = bpy.data.materials.new(name=f"Label_{text}")
            mat.use_nodes = True
            nodes = mat.node_tree.nodes
            for n in list(nodes): nodes.remove(n)
            em = nodes.new('ShaderNodeEmission')
            em.inputs['Color'].default_value = color
            em.inputs['Strength'].default_value = 20.0
            out = nodes.new('ShaderNodeOutputMaterial')
            mat.node_tree.links.new(em.outputs['Emission'], out.inputs['Surface'])
            txt.data.materials.append(mat)
            
            # Simple rotation to face camera better (adjust if needed)
            txt.rotation_euler = (math.radians(90), 0, 0)
            collection.objects.link(txt)
        
        create_label("X", (length/2 + 0.8, 0, 0), (1.0, 0.2, 0.2, 1.0))
        create_label("Y", (0, length/2 + 0.8, 0), (0.2, 1.0, 0.2, 1.0))
        create_label("Z", (0, 0, length/2 + 0.8), (0.2, 0.2, 1.0, 1.0))

    print("✅ Axis helpers added (X=red, Y=green, Z=blue)")