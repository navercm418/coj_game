import bge

cont = bge.logic.getCurrentController()
own = cont.owner
#sens = cont.sensors["sas"]

zvSub = "Test"
zvBody = "This is a test message."
zvTo = bge.logic.getCurrentScene().objects["TL1_GameController"]
zvTo = str(zvTo)
zvFrom = own
zvFrom = str(zvFrom)

# sendMessage(subject, body, to, from)
bge.logic.sendMessage(zvSub, zvBody, zvTo, zvFrom)
print('msg sent:', zvSub,  zvBody, zvTo, zvFrom)
