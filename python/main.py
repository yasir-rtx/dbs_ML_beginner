import os
from function import user_calling as calling
from function import users

os.system("clear")

calling(0)
calling(1)

for user in users : print(user,"\n")
