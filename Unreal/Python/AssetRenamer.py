import unreal

class AssetRenamer(object):

    systemLibrary = unreal.systemLibrary()
    editor_util = unreal.EditorUtiltyLibrary()
    string_lib = unreal.StringLibrary()
    UseCase = False

    replaced = 0

    def __init__(self):
        rename_assets()
    
    def ResolveDependencies():
        if systemLibrary is None:
            systemLibrary = unreal.SystemLibrary()
            
        if editor_util is None:
            editorUtility = unreal.EditorUtilityLibrary()
        
        if StringLibrary is None:
            StringLibrary = unreal.StringLibrary()


    def RenameAsset(UseCase):
        if string_lib.contains(asset_name, search_pattern, use_case=UseCase):
            replacedName = string_lib.replace(asset_name, search_pattern, replace_pattern)
            editor_util.rename_asset(asset, replacedName)
            replaced += 1

            unreal.log("Replaced {} with {}".format(asset, replacedName))
        else:
            unreal.log("{} did not match the search pattern, was skipped".format(asset_name))

    def rename_assets():
        selected_assets = editor_util.selected_assets()
        number_of_assets = len(selected_assets)
        
        UseCase = unreal.SearchCase.CASE_SENSITIVE if UseCase else unreal.SearchCase.IGNORE_CASE

        for asset in selected_assets:
            asset_name = systemLibrary.get_object_name(asset)

            if UseCase == False:
                RenameAsset(UseCase, asset_name)
                
            elif UseCase == True:
                RenameAsset(UseCase, asset_name)
                    
            
        


        