import bge
import bpy
import sqlite3
import os
import sys

# set object variables
cont = bge.logic.getCurrentController()
own = cont.owner
cur_scn = bpy.context.scene.name

# =================================================================
# setting up database coj_data.db
root = os.path.abspath(os.curdir)
zvDbFile = os.path.join(root, "db", "coj_data.db")

own['GO_DbFile']=zvDbFile

zvDbCon = sqlite3.connect(zvDbFile)
zvCrs = zvDbCon.cursor()
# ===================================================================

zvCrs.execute("""
SELECT pls.PSSCNFLOAD
FROM PLSCENES pls
JOIN PLAYER plr on plr.PLRID=pls.PSPLRID
WHERE plr.PLRCURPLR='Y' and pls.PSSCNID='"""+ cur_scn +"'")
result = zvCrs.fetchone()
zvFload = result[0]
    
if zvFload == 'Y':
    print('this is the 1st load for', cur_scn)
else:
    print(cur_scn, 'has loaded before')


zvDbCon.commit()
zvDbCon.close()
