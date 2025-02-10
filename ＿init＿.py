import bpy
from level_editor.my_menu import TOPBAR_MT_my_menu

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

classes = (TOPBAR_MT_my_menu,)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)

    print("レベルエディタが有効化されました。")

def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    for cls in classes:
        bpy.utils.unregister_class(cls)

    print("レベルエディタが無効化されました。")
    
if __name__ == "__main__":
    register()
    
def draw_menu_manual(self,context):
    
    self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')


