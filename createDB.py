import sqlite3

sqlite_file = 'osiris.db' 

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE odds_pinnacle ()	'