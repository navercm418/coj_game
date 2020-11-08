import bge

scene = bge.logic.getCurrentScene()
objects = scene.objects
GOB = objects['TL1_GameController']
print(GOB.GO_DbFile)
