import bge
import sqlite3
import os
import sys

# setting up database heli_data.db
# print(os.listdir())
# os.chdir('db')

zvRootDir = sys.argv[0]
if os.name == 'nt':
    zvRootDir = zvRootDir.rsplit("\\", 1)[0]
else:
    zvRootDir = zvRootDir.rsplit('/', 1)[0]

print(zvRootDir)

print(os.path.join(zvRootDir, "/heli_data", "/db", "heli_data.db")) 

# zvDbCon = sqlite3.connect('heli_data.db')
# zvCrs = zvDbCon.cursor()

#for row in zvCrs.execute('SELECT * FROM sys_settings'):
#    print(row)





