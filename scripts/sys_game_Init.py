import bge
import sqlite3
import os
import sys

# setting up database heli_data.db
zvDelim = ""
zvDbPath = ""
zvFload = "N"

# setting up database coj_data.db
root = os.path.abspath(os.curdir)
zvDbFile = os.path.join(root, "db", "coj_data.db")

zvDbCon = sqlite3.connect(zvDbFile)
zvCrs = zvDbCon.cursor()

if zvFload == "Y":
    zvCrs.execute("UPDATE sys_settings SET sysO1VAL = '"+ zvRootDir +"' WHERE sysO1 = 'root_directory_full'")
    zvCrs.execute("UPDATE sys_settings SET sysO1VAL = '"+ os.name +"' WHERE sysO1 = 'os_type'")
    zvCrs.execute("UPDATE sys_settings SET sysO1VAL = '"+ zvDbPath +"' WHERE sysO1 = 'database_directory'")
    zvCrs.execute("UPDATE sys_settings SET sysO2VAL = 'heli_data.db' WHERE sysO2 = 'database_file'")
    zvDbCon.commit()

# for row in zvCrs.execute('SELECT * FROM sys_settings'):
#    print(row)

zvDbCon.close()
