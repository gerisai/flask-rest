import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

query = 'CREATE TABLE users (id int, username text, password text)'

cursor.execute(query)

user = (1,'isai', 'asdf')

query = 'INSERT INTO users VALUES (?,?,?)'
cursor.execute(query,user)

users = [
    (2,'rolf','asdf'),
    (3,'anne','xyz')
]

cursor.executemany(query,users)

query = 'SELECT * FROM users'
for row in cursor.execute(query):
    print(row)

connection.commit()

connection.close()