from maya import cmds

m_currentTime = Cmds.currentTime;

def ConstructAttributeName():
    #Construct Full name of attribute, using the mel name as a param
    AttributeFullname = '%s.%s' % (obj, _attr)
    keyframes = cmds.keyframe(AttributeFullname, query = True)

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
       
        #Get the previous and next values of the attributes and calculate the difference(delta) between them
        previousValue = cmds.getAttr(AttributeFullname, time = previousFrame)
        nextValue = cmds.getAttr(AttributeFullname, time = nextFrame)
        DeltaBetweenVal = nextValue - previousValue
        WeightedDelta = (DeltaBetweenVal * percentage) / 100.0
        NewValue = previousValue + WeightedDelta
          
         
        cmds.setKeyframe(AttributeFullname, time = m_currentTime, value = NewValue)
          

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
	
def main(): 
    Tween(12, selection = True)
   
main()