# добавление таблиц в БД

import db_connect

def create_tables():
	"""создаём таблицы если их нет"""

	"""создаём таблицу week_popularity"""
	query = """
		CREATE TABLE IF NOT EXISTS week_popularity (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			trending TEXT NOT NULL,
			popularity INTEGER NOT NULL,
			date INTEGER NOT NULL);
		"""
	db_connect.write_query(db_connect.connection, query)

	"""создаём таблицу date_trending"""
	query = """
	CREATE TABLE IF NOT EXISTS date_trending (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		trending TEXT NOT NULL,
		date INTEGER NOT NULL);
	"""
	db_connect.write_query(db_connect.connection, query)


	"""создаём таблицу trending_related"""
	query = """
	CREATE TABLE IF NOT EXISTS trending_related (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		trending TEXT NOT NULL,
		related TEXT NOT NULL,
		frequency INTEGER NOT NULL,
		date INTEGER NOT NULL);
	"""
	db_connect.write_query(db_connect.connection, query)

	print("Connection SQLite DB successful.")
	print("Tables created if they didn't exist.")

