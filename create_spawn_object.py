import bpy
from .load_spawn_object import SpawnNames
from .load_spawn_object import MYADDON_OT_load_spawn_object

class MYADDON_OT_create_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_spawn_object"
    
    bl_label = "出現ポイントシンボルの作成"
    
    bl_description = "出現ポイントのシンボルを作成します"
    
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.StringProperty(name="Type",default="Player")
    
    def execute(self,context):

        spawn_object = bpy.data.objects.get(SpawnNames.names[self.type][SpawnNames.PROTOTYPE])

        if spawn_object is None:
            bpy.ops.myaddon.myaddon_ot_load_spawn_object('EXEC_DEFAULT')

            spawn_object = bpy.data.objects.get(SpawnNames.names[self.type][SpawnNames.PROTOTYPE])

        print("出現ポイントのシンボルを作成します")

        bpy.ops.object.select_all(action='DESELECT')

        object = spawn_object.copy()

        bpy.context.collection.objects.link(object)

        object.name = SpawnNames.names[self.type][SpawnNames.INSTANCE]

        return {'FINISHED'}