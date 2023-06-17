# соединение с БД

import sqlite3
from sqlite3 import Error

import create_tables


def create_connection(path):
	"""подключение к БД"""
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("Connection SQLite DB successful.")
	except Error as e:
		print(f"The error '{e}' occurred.")
	return connection


# создаем соединение с БД
connection = sqlite3.Connection("db.sqlite3")


def write_query(connection, query):
	"""запись БД"""
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		#print("Query for write successfully.")
	except Error as e:
		print(f"The error '{e}' occurred.")


def read_query(connection, query):
	"""чтение БД"""
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except Error as e:
		print(f"The error '{e}' occurred.")


# создаём таблицы если их не существует
create_tables.create_tables()