import bge
cont = bge.logic.getCurrentController()
own = cont.owner
sens = cont.sensors['Message']    
if sens.positive:
    own['Text']=sens.bodies[0]
