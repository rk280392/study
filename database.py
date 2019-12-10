import sqlite3

db = sqlite3.connect('servers.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute('''SELECT * from serverinfo''')
for row in cursor:
    row['name'], row['ipaddr'], row['username'], row['password']
    print('{0} : {1}, {2}, {3}'.format(row['name'], row['ipaddr'], row['username'], row['password']))
#    print(row)
db.close()
