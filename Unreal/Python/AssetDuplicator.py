from venv import main
import unreal
import os as OperatingSystem


class AssetDuplicator(object):

    editor_utilites = unreal.EditorUtiltyLibrary()
    editor_asset_lib = unreal.EditorAssetLibrary()
    selectedassets = []
    NumberOfClones = 0
    NumberOfSelectedAssets = len(selected_assets)

    def __init__(self):

        if editor_utilites is None:
            raise ValueError (importError, ImportError)
        
        main(self)


    def main(self):

        if self.selectedassets is None:
            raise SizeError()

        for asset in self.selectedassets:
            asset_name = asset.get_fname()
            asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
            source_path = OperatingSystem.path.dirname(asset_path)

            for i in range(self.NumberOfClones):
                new_name = "{}_{}".format(asset_name, i)
                destination = OperatingSystem.path.join(source_path, new_name)
                duplicate = editor_asset_lib.duplicate_asset(asset_path, destination)

                if duplicate is None:
                    unreal.log("Duplicate from {} at {} already exists!").format(source_path, destination)


        pass
