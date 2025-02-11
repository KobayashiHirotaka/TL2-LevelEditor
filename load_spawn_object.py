import bpy
import os
import bpy.ops

class SpawnNames():

    PROTOTYPE = 0
    INSTANCE = 1
    FILENAME = 2

    names = {}

    names["Enemy"] = ("PrototypeEnemySpawn", "EnemySpawn", "enemy/newPlayer.obj")
    names["Player"] = ("PrototypePlayerSpawn", "PlayerSpawn", "player/newPlayer.obj")

class MYADDON_OT_load_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_load_spawn_object"
    
    bl_label = "出現ポイントImport"
    
    bl_description = "出現ポイントのシンボルをImportします"

    bl_options = {"REGISTER", "UNDO"}

    def load_obj(self, type):

        print("出現ポイントのシンボルをImportします")

        spawn_object = bpy.data.objects.get(SpawnNames.names[type][SpawnNames.PROTOTYPE])
        if spawn_object is not None:
            return {'CANCELLED'}

        addon_directory = os.path.dirname(__file__)

        relative_path = SpawnNames.names[type][SpawnNames.FILENAME]

        full_path = os.path.join(addon_directory, relative_path)

        bpy.ops.wm.obj_import('EXEC_DEFAULT',filepath=full_path,display_type='THUMBNAIL',
                              forward_axis='Z',up_axis='Y')
        
        bpy.ops.object.transform_apply(location=False,rotation=True,scale=False,properties=False,isolate_users=False)
        
        object = bpy.context.active_object

        object.name = SpawnNames.names[type][SpawnNames.PROTOTYPE]

        object["type"] = SpawnNames.names[type][SpawnNames.INSTANCE]

        bpy.context.collection.objects.unlink(object)

        return {"FINISHED"}
    
    def execute(self,context):

        self.load_obj("Enemy")

        self.load_obj("Player")

        return {'FINISHED'}