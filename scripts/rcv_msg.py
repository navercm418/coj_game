import bge

cont = bge.logic.getCurrentController()
own = cont.owner

sens = cont.sensors['Message']
    
if sens.positive:
    zvText = own['Text']=sens.bodies[0]
    zvText = str(zvText)
    zvOwn = str(own)
    print("msg:", zvOwn, zvText)