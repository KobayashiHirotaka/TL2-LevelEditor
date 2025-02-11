import bpy
from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .my_menu import TOPBAR_MT_my_menu
from .add_filename import MYADDON_OT_add_filename
from .add_collider import MYADDON_OT_add_collider
from .add_disabled import MYADDON_OT_add_disabled
from .filename import OBJECT_PT_file_name
from .collider import OBJECT_PT_collider
from .disabled import OBJECT_PT_disabled
from .draw_collider import DrawCollider

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
    TOPBAR_MT_my_menu,MYADDON_OT_add_filename,MYADDON_OT_add_collider,MYADDON_OT_add_disabled,
    OBJECT_PT_file_name,OBJECT_PT_collider,OBJECT_PT_disabled,)

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