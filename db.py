import sqlite3
conn = sqlite3.connect("mydatabase.db")
#conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT ,usn TEXT,name TEXT,email TEXT,password TEXT)")
cur = conn.execute("SELECT * FROM users")
print(cur.fetchall())
conn.execute("CREATE TABLE marksheet(id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT, semester TEXT, filename TEXT)")
#cur = conn.execute("SELECT * FROM marksheet")
conn.execute("CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT, filename TEXT)")
#cur = conn.execute("SELECT * FROM books")
conn.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT, filename TEXT)")
#cur = conn.execute("SELECT * FROM notes")