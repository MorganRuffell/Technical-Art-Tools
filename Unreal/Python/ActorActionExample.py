import unreal

class ActorActionEditor(object):
    editor_util = unreal.EditorUtiltyLibrary()
    LayerSubsystem = unreal.LayerSubsystem()
    editorFilterLib = unreal.editorFilterLibrary()

    materials = []
    selected_assets = []

    def __init__(self):

        if materials is not None:
            materials.empty()

        materials = editor_filter_lib.by_class(selected_assets, unreal.Material)
        selected_assets = editor_util.get_selected_assets()

        if editor_util is None:
            editor_util = unreal.EditorUtiltyLibrary()
        
        if editorFilterLib is None:
            editorFilterLib = unreal.editorFilterLibrary()
        
        main()
    
    def main(self):

        if len(materials) < 1:
            print("")
            # use the unreal log for this.


        if len(materials) == 1:

            material = materials[0]
            material_name = material.get_fname()




        for x in materials:




        

