import sqlite3

conn = sqlite3.connect('univ.db')

cursor = conn.cursor()


result = cursor.execute('select * from student')

data = result.fetchmany(2)
print(data)

conn.commit()
cursor.close()
conn.close()