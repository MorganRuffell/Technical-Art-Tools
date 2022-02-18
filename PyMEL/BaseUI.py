from maya import cmds
from AnimationTweenWindow import AnimationTweenWindow

_WindowName = ""


class BaseMayaWindow(object, name):

    windowName = "BaseWindow"

    def __init__(self, name):

        if name == "":
            name = "BaseMayaWindow"

        elif name is None:
            name = "BaseMayaWindow"

        if cmds.window(self.windowName, query = True, exists = True):
            cmds.deleteUI(self.windowName)

        showWindow(self)

    def showWindow(self):
       cmds.window("Tweener Window")
       cmds.showWindow()

    def reset(self, *args):
        if args: 
            for x in args:
                args.remove(x)
        
        
    def close(self, *args):
        if args: 
            for x in args:
                args.remove(x)
        
        deleteUI(windowName)

    def BuildUI(self):
        pass



        #column = cmds.columnLayout(self.windowName)
        #row = cmds.rowLayout(numberOfColumns = 2)
        #cmds.setParent(column)
        #cmds.button(label = "Reset", command = self.reset)
        #cmds.button(label = "Close", command = self.close)

