import sqlite3

sqlite_file = 'osiris.db' 

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# Creating a new SQLite table with 1 column
c.execute('''
	CREATE TABLE odds_pinnacle
		(
		log_time datetime,
		start_time datetime,
		sport_id integer,
		league_id integer,
		league_name varchar(50),
		event_id char(9),
		line_id char(9),
		home_team varchar(20),
		away_team varchar(20),
		market_type char(9),
		market_value numeric,
		market_odds numeric,
		market_size numeric
		)
	''')

conn.commit()
conn.close()
