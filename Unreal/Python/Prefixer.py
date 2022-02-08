from sys import prefix
import unreal
import json

prefixMapping = {}
with open("..\Prefixes.json","r") as json_file:
    prefixMapping = json.loads(json_file.read())

class Prefixer(object):

    editorUtility = unreal.EditorUtilityLibrary()

    selected_assets = editor_util.get_selected_assets()
    number_of_assets = len(selected_assets)
    prefixed_assets = 0
    UnableToBePrefixed = 0

    def program(self):
        for asset in self.selected_assets:
            assetname = system_lib.get_object_name(asset)
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

            else:
                unreal.log("Asset {} of type {} is already prefixed with {}".format(asset_name, class_name, class_Prefix))

            unreal.log("Prefixed {} of {} assets".format(prefixed_assets, number_of_assets))

    def __init__(self):

        if self.selected_assets is None:
            self.selected_assets = editor_util.get_selected_assets()
        
        program(self)
        

    



