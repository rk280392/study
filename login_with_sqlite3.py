from pexpect import pxssh
import getpass
import sqlite3
from sqlite3 import Error

servername = input('name : ')
db = sqlite3.connect('servers.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("SELECT * from serverinfo where name = '%s'" % servername)
for row in cursor:
   aliasname = str(row['name']) 
   ip = str(row['ipaddr'])
   user_name = str(row['username']) 
   pass_word = str(row['password'])
db.close()
your_command = input('Please enter the command: ')
print("loading please wait.................")
try:                                                            
         s = pxssh.pxssh()
         ipaddress = ip
         username = user_name
         password = pass_word
         command = your_command
         s.login (ip, username, password)
        # s.sendline ('uptime')  # run a command
        # s.prompt()             # match the prompt
        # print s.before         # print everything before the prompt.
         s.sendline (command)
         s.prompt()
         #init_string = s.before.replace("\r\n", "")
         init_string = s.before
         print(init_string.decode('utf-8'))
         s.logout()
except pxssh.ExceptionPxssh as  e:
         print("pxssh failed on login.")
         print(str(e))
