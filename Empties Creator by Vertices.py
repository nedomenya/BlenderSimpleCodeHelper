import bpy

obj = bpy.context.active_object

vertex_Index = 0
while vertex_Index < len(obj.data.vertices):    
    v = obj.data.vertices[vertex_Index]
    co_final = obj.matrix_world @ v.co
    obj_empty = bpy.data.objects.new("Empty"+str(vertex_Index), None)
    bpy.context.collection.objects.link(obj_empty)
    obj_empty.location=co_final
    obj_empty.empty_display_size=1
    vertex_Index+=1
