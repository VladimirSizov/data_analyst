# запусказем прроцеессы получения и записи данных в БД

import datetime

import db_update


with open('/Users/vladimirsizov/Documents/PET_PROJECTS/GOOGLE_TRENDS/log.txt', 'a') as f:
	# запускаем сбор с google trends
	try:
		# добавляем в БД слова которые 'в_тренде' на дату
		db_update.add_new_date_trending()
		# добавляем в БД 'связные_слова' с 'в_тренде' на дату
		db_update.add_new_trending_related()
		# добавляем в БД еженедельное значение 'популярности'
		# слов 'в_тренде' за последние 5 лет
		db_update.add_new_week_popularity()
		# в случае сбоя сбора записей 'популярности', подтянет пропущеные данные
		#db_update.add_if_fail()
		execute = ' success'
	except:
		execute = ' fail'
	# результат пишем в лог
	result = '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + execute
	f.write(result)
