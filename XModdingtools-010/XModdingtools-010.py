bl_info = {
    "name": "XModdingtools",
    "author": "haunetal1990",
    "version": (0, 1, 0),
    "blender":  (2, 80, 0),
    "location": "View3D > UI > XModdingtools",
    "description": "Add some modding tools",
    "doc_url": "#",
    "category": "Add Mesh",
}
import bpy

def set_object_name(obj, new_name):
    obj.name = new_name

def transfer_object_name(obj):
    obj.data.name = obj.name

class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "XModdingtools"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)


class PanelOne(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_1"
    bl_label = "rename mesh(s)"

    def draw(self, context):
        layout = self.layout
        
        #row.label(text="haunetal1990")
        obj = context.object
        row = layout.row()
        row.prop(bpy.data.window_managers["WinMan"], "object_name", text="name")
        row = layout.row()
        row.operator("object.transfer_name_operator")
        row = layout.row()
        
        row.operator("object.rename_selected_objects", text="rename mesh data only")
        
class TransferObjectNameOperator(bpy.types.Operator):
    bl_idname = "object.transfer_name_operator"
    bl_label = "rename mesh(s)"

    def execute(self, context):
        selected_objs = context.selected_objects
        obj_name = bpy.data.window_managers["WinMan"].object_name

        for i, obj in enumerate(selected_objs):
            set_object_name(obj, f"{obj_name}_{str(i+1).zfill(2)}")
            transfer_object_name(obj)

        return {'FINISHED'}

class RenameSelectedObjectsOperator(bpy.types.Operator):
    bl_idname = "object.rename_selected_objects"
    bl_label = "rename mesh data only"

    def execute(self, context):
        for obj in context.selected_objects:
            transfer_object_name(obj)
        return {'FINISHED'}

classes = (
    TransferObjectNameOperator,
    RenameSelectedObjectsOperator
)

def register():
    bpy.utils.register_class(PanelOne)
    bpy.utils.register_class(TransferObjectNameOperator)
    bpy.utils.register_class(RenameSelectedObjectsOperator)
    bpy.types.WindowManager.object_name = bpy.props.StringProperty(name="Object Name")

def unregister():
    bpy.utils.unregister_class(PanelOne)
    bpy.utils.unregister_class(TransferObjectNameOperator)
    bpy.utils.unregister_class(RenameSelectedObjectsOperator)
    del bpy.types.WindowManager.object_name

if __name__ == "__main__":
    register()
