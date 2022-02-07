import unreal
import math

class PowerOfTwo(object):

    editor_util = unreal.EditorUtiltyLibrary()
    selectedAssets = editor_util.selectedAssets()
    number_of_assets = len(selectedAssets)
    not_pow = 0
    is_pow = 0

    x_size = 0
    y_size = 0

    def __init__(self):

        if len(self.selectedAssets) == 0:
            self.selectedAssets = editor_util.selectedAssets()
        
        GetAssetNames()    

    def GetAssetNames():

        for asset in self.selectedAssets:
            unreal.log(asset.get_fname())

            asset_name  = asset.get_fname()
            asset_path = asset.get_path_name()

            try:
                x_size = asset.blueprint_get_size_x()
                y_size = asset.blueprint_get_size_y()

                IsPowerOfTwo(asset, x_size, y_size)

                unreal.log("{} checked, {} textures not properly formatted".format(number_of_assets, not_pow))

            except Exception as error:
                unreal.log("{} is not a texture".format(asset_name))


    def IsPowerOfTwo(asset, x_size, y_size):
        isXValid = math.log(x_size, 2).is_integer()
        isYValid = math.log(y_size, 2).is_integer()

        if not isXValid or not isYValid:
            unreal.log("{} Is not power of two ({},{})".format(asset.get_fname(), x_size, y_size))
            not_pow += 1
        else:
            is_pow += 1
        
        



