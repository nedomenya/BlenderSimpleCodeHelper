import bpy

for i in bpy.context.object.data.shape_keys.key_blocks:
    bpy.context.object.shape_key_remove(i)

