import pymssql

conn1 = pymssql.connect("Host1", "user1", "password1", "db1")
conn2 = pymssql.connect("Host2", "user2", "password2", "db2")

cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

cursor1.execute('SELECT * FROM TABLE1 LIMIT 10')
cursor2.execute('SELECT * FROM TABLE2 LIMIT 10')

result1 = cursor1.fetchall()
result2 = cursor2.fetchall()

# print each row
for row in result1:
   print(row)

# print each row
for row in result2:
   print(row)
