from sys import prefix
import unreal

prefixMapping = {
    "Blueprint" : "BP_",
    "StaticMesh" : "SM_",
    "Skeleton" : "SKL_",
    "PhysicsAsset" : "PA_",
    "Material" : "M_",
    "MaterialInstance" : "MI_",
    "MaterialFunction" : "MF_",
    "NiagaraEmitter" : "NE_",
    "NiagaraSystem" : "NS_",
    "Animation" : "ANIM_",
    "BlueprintWidget" : "BPW_",
    "Struct" : "S_",
    "SoundCue" : "SC_",
    "Texture2D" : "T_",
    "RenderTarget" : "RT",
    "Enum" : "E_",
}

class Prefixer(object):

    editorUtility = unreal.EditorUtilityLibrary()

    selected_assets = editor_util.get_selected_assets()
    number_of_assets = len(selected_assets)
    prefixed_assets = 0
    UnableToBePrefixed = 0

    def program(self):
        for asset in self.selected_assets:
            assetname = asset.get_fname()
            asset_class = asset.get_class()
            class_name = system_lib.get_class_display_name(asset_class)

            class_Prefix = prefixMapping.get(class_name, None)

            if class_Prefix is None:
                UnableToBePrefixed += 1
                unreal.log_warning("No mapping for {} of type {}".format(assetname,class_name))
                continue

            if not asset_name.startswith(class_Prefix):
                newAssetName = class_Prefix + asset_name
                editor_util.rename_asset(asset, newAssetName)
                prefixed_assets += 1


            unreal.log("{} with class {}".format(assetname, asset_class))

    def __init__(self):

        if self.selected_assets is None:
            self.selected_assets = editor_util.get_selected_assets()
        
        program(self)
        

    



