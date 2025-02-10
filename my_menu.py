import bpy

class TOPBAR_MT_my_menu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_my_menu"
    
    bl_label = "MyMenu"
    
    bl_description = "拡張メニュー by ..."
    
    def draw(self, context):
      self.layout.operator("wm.url_open_preset", text = "Manual", icon = "HELP")
        
    def submenu(self,context):
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)