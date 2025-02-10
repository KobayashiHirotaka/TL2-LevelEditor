import bpy
from level_editor.stretch_vertex import MYADDON_OT_stretch_vertex
from level_editor.create_ico_sphere import MYADDON_OT_create_ico_sphere
from level_editor.export_scene import MYADDON_OT_export_scene
from level_editor.my_menu import TOPBAR_MT_my_menu
from level_editor.add_filename import MYADDON_OT_add_filename
from level_editor.add_collider import MYADDON_OT_add_collider
from level_editor.filename import OBJECT_PT_file_name
from level_editor.collider import OBJECT_PT_collider
from level_editor.draw_collider import DrawCollider

bl_info = {
    "name": "レベルエディタ",
    "author": "Hirotaka Kobayashi",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}    

classes = (MYADDON_OT_export_scene,MYADDON_OT_create_ico_sphere,MYADDON_OT_stretch_vertex,
    TOPBAR_MT_my_menu,MYADDON_OT_add_filename,MYADDON_OT_add_collider,OBJECT_PT_file_name,
    OBJECT_PT_collider,)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")

    print("レベルエディタが有効化されました。")

def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)

    if DrawCollider.handle:
        bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")
    for cls in classes:
        bpy.utils.unregister_class(cls)

    print("レベルエディタが無効化されました。")
    
if __name__ == "__main__":
    register()