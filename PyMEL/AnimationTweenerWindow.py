from maya import cmds
import BasicProgramClass as Program
from BaseUI import BaseMayaWindow 

m_currentTime = Cmds.currentTime;
AttributeFullName = ""
   
main()

class TweenProgram(Program):

    tweenValue = 0

    def _init(self):

        Tween(this.tweenValue, selection = True)

    def ConstructAttributeName():
    #Construct Full name of attribute, using the mel name as a param
        if obj and _attr:
          AttributeFullname = '%s.%s' % (obj, _attr)
          keyframes = cmds.keyframe(AttributeFullname, query = True)
        else:
           return None

    def CalculateTweenPoint(previousFrame, nextFrame):
        #Get the previous and next values of the attributes and calculate the difference(delta) between them
        previousValue = cmds.getAttr(AttributeFullname, time = previousFrame)
        nextValue = cmds.getAttr(AttributeFullname, time = nextFrame)
        
        DeltaBetweenVal = nextValue - previousValue
        WeightedDelta = (DeltaBetweenVal * percentage) / 100.0
    
        NewValue = previousValue + WeightedDelta
        return NewValue


    def CreateCommandNames(attributes, obj, percentage):
        for _attr in attributes:      
            ConstructAttributeName(obj, _attr)
              
            #if attribute is not keyable, ignore it
            if not keyframes:
                continue
                  
            #append results to this list
            previousKeyframes = []      
                  
            for frame in keyframes:
                if x < m_currentTime:
                    previousKeyframes.append(x)
              
            #use list comprenehsion -- really powerful if you want to do things quickly!   
            laterKeyFrames = [frame for frame in keyframes if frame > m_currentTime]
              
            if not previousKeyframes and not keyframes:
                continue
                  
            if previousKeyframes:
                previousFrame = max(previousKeyframes)
                  
            else:
                previousFrame = None
                  
            nextFrame = min(laterKeyframes) if laterKeyFrames else None
             
            if not previousFrame or not nextFrame:
                continue
            
            
            cmds.setKeyframe(AttributeFullname, time = m_currentTime, value = CalculateTweenPoint(previousFrame, nextFrame))
          

    def FetchCurrentTime():
    	if m_currentTime == Cmds.currentTime:
    		return
    	else:
    		m_currentTime = Cmds.currentTime
    		return 

    def Tween(percentage, obj = None, attributes = None, selection = True):

        if not obj and not selection:
            raise ValueError("Values are null, we cannot tween to anything!")

        if not obj:
            obj = cmds.ls(selection = True)[0]

        if not attributes:
            attributes = cmds.ListAttr(obj, keyable = True)
    
        FetchCurrentTime()
        CreateCommandNames(attributes, obj, percentage)
	
    
class AnimationTweenWindow(BaseMayaWindow):

    windowName = "TweenerWindow"

    def __init__(self):

        if cmds.window(self.windowName, query = True, exists = True):
            cmds.deleteUI(self.windowName)

        showWindow(self)

    def BuildUI(self):
        column = cmds.columnLayout(self.windowName)
        row = cmds.rowLayout(numberOfColumns = 2)

        cmds.text(label = "Slider for Interpolated value")
        self.slider = cmds.floatSlider(min = 0, max = 100, value = 50, step = 1, changeCommand = main())

        cmds.setParent(column)
        cmds.button(label = "Reset", command = self.reset)
        cmds.button(label = "Close", command = self.close)

    def showWindow(self):
       cmds.window("Tweener Window")
       cmds.showWindow()

    def reset(self, *args):
        if args: 
            for x in args:
                args.remove(x)
        
        cmds.floatSlider(self.slider, value = 50)


    def close(self, *args):
        if args: 
            for x in args:
                args.remove(x)
        
        deleteUI(windowName)

   
        



