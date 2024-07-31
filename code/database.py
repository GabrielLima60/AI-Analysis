import sqlite3
import sys

user = sys.argv[1]
password = sys.argv[2]
insert_or_check = sys.argv[3]


connection = sqlite3.connect('lib//users.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    password TEXT
)
''')

if insert_or_check == "insert":
    # Use parameterized query to prevent SQL injection
    cursor.execute('''
        INSERT INTO users (user, password)
        VALUES (?, ?)
        ''', (user, password))
    
elif insert_or_check == "check":
    cursor.execute('''
        SELECT * FROM users WHERE user = ? AND password = ?
        ''', (user, password))
    result = cursor.fetchone()
    
    print(str(result))

connection.commit()

connection.close()