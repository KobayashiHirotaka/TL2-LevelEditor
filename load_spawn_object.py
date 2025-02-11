import bpy
import os
import bpy.ops

class MYADDON_OT_load_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_load_spawn_object"
    
    bl_label = "出現ポイントImport"
    
    bl_description = "出現ポイントのシンボルをImportします"

    bl_options = {"REGISTER", "UNDO"}

    prototype_object_name = "ProttypePlayerSpawn"

    object_name = "PlayerSpawn"
    
    def execute(self, context):

        print("出現ポイントのシンボルをImportします")

        spawn_object = bpy.data.objects.get(MYADDON_OT_load_spawn_object.prototype_object_name)
        if spawn_object is not None:
            return {'CANCELLED'}

        addon_directory = os.path.dirname(__file__)

        relative_path = "player/newPlayer.obj"

        full_path = os.path.join(addon_directory, relative_path)

        bpy.ops.wm.obj_import('EXEC_DEFAULT',filepath=full_path,display_type='THUMBNAIL',
                              forward_axis='Z',up_axis='Y')
        
        bpy.ops.object.transform_apply(location=False,rotation=True,scale=False,properties=False,isolate_users=False)
        
        object = bpy.context.active_object

        object.name = MYADDON_OT_load_spawn_object.prototype_object_name

        object["type"] = MYADDON_OT_load_spawn_object.object_name

        bpy.context.collection.objects.unlink(object)

        return {"FINISHED"}