import bge
import sqlite3
import os
import sys

# C:\CodeProjects\bge\Release\coj_game\ -> db\ -> coj_data.db
# os.chdir("..") go back one
root = os.path.abspath(os.curdir)
print(os.path.join(root, "db", "coj_data.db")) 
