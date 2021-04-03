import bpy

for i in bpy.context.object.vertex_groups:
    bpy.context.object.vertex_groups.remove(i)
