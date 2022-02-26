from itertools import count
import unreal

class DeleteEmptyDirectories(object):
    editor_asset_lib = unreal.EditorAssetLibrary()
    sourceDirectory = "/Game/Default"
    includeSubDirectories = True
    countOfDeleted = 0

    assets = editor_asset_lib.list_assets(sourceDirectory, recursive=includeSubDirectories, includefolder=True)
    folders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]

    def __init__(self):
        for folder in folders:
            has_assets = editor_asset_lib.does_directory_have_assets(folder)

            if not has_assets:
                editor_asset_lib.delete_directory(folder)
                countOfDeleted += 1
                unreal.log("Folder {} without assets was delete".format(folder))
        
        unreal.log("Deleted {} folders without assets".format(countOfDeleted))

