import bge
import sqlite3
import os
import sys

# setting up database heli_data.db
zvDelim = ""
zvDbPath = ""

zvRootDir = sys.argv[0]
if os.name == 'nt':
    zvRootDir = zvRootDir.rsplit("\\", 1)[0]
    zvDelim = "\\"
else:
    zvRootDir = zvRootDir.rsplit('/', 1)[0]
    zvDelim = "/"

zvDbPath = zvRootDir + zvDelim + "heli_data" + zvDelim + "db"
os.chdir(zvDbPath)

zvDbCon = sqlite3.connect('heli_data.db')
zvCrs = zvDbCon.cursor()
zvCrs.execute("UPDATE sys_settings SET sysO1VAL = '"+ zvRootDir +"' WHERE sysO1 = 'root_directory_full'")
zvCrs.execute("UPDATE sys_settings SET sysO1VAL = '"+ os.name +"' WHERE sysO1 = 'os_type'")
zvCrs.execute("UPDATE sys_settings SET sysO1VAL = '"+ zvDbPath +"' WHERE sysO1 = 'database_directory'")
zvCrs.execute("UPDATE sys_settings SET sysO2VAL = 'heli_data.db' WHERE sysO2 = 'database_file'")

zvDbCon.commit()

for row in zvCrs.execute('SELECT * FROM sys_settings'):
    print(row)

zvDbCon.close()
