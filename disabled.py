import bpy
from .add_disabled import MYADDON_OT_add_disabled

class OBJECT_PT_disabled(bpy.types.Panel):
    bl_idname = "OBJECT_PT_disabled"
    
    bl_label = "Disabled"

    bl_space_type = "PROPERTIES"

    bl_region_type = "WINDOW"

    bl_context = "object"

    bpy.types.Object.disabled = bpy.props.BoolProperty(
        name="Disabled",
        description="Object disabled flag",
        default=True
    )

    def draw(self, context):
        
        if "disabled" in context.object:
            
            self.layout.prop(context.object, "disabled", text=self.bl_label)
        else:
            self.layout.operator(MYADDON_OT_add_disabled.bl_idname)