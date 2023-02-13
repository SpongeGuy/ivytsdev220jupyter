import sqlite3
import sqlalchemy
from sqlalchemy import text
from sqlalchemy import create_engine
conn = sqlite3.connect('books.db')
curs = conn.cursor()

"""
curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))
curs.close()
conn.close()
"""

curs.execute('''CREATE TABLE books (title VARCHAR(20) PRIMARY KEY, author VARCHAR(20), year INT)''')
curs.execute('INSERT INTO books VALUES("harry potter", "jk rowling", 2001)')
engine = create_engine("sqlite:///books.db", echo = True, future = True)

with engine.connect() as connection:
	rows = connection.execute(text("SELECT title FROM books"))
	titles = []
	for row in rows:
		titles.append(row)
		titles.sort()
		print(row)

	for title in titles:
		print(title)

curs.close()
conn.close()