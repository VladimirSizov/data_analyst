# методы подключения к google trends через библиотеку pytrends
# https://pypi.org/project/pytrends/

from pytrends.request import TrendReq
import pandas as pd
import datetime
import zoneinfo
import re


# выбираем локализацию подключения, tz смещение часового пояса (в минутах)
pytnd = TrendReq(hl='ru-RU', tz=0)


def get_trending():
	"""возвращает cписок слов которые сейчас в тренде"""
	# pn - регион
	return pytnd.trending_searches(pn='russia')[0].tolist()


def get_related(kw_list):
	"""по слову запроса возвращает датафрейм, связанные запросы с частотностью"""
	# kw_list запрос к которому нужно найти связанные с частотностью
	pytnd.build_payload(kw_list=[kw_list],  # сужение запроса по категориям
						   cat=0,  # сужение запроса по категориям 71
						   timeframe='now 1-H',  # даты поиска '2017-02-06 2017-02-12', 'now 1-H', 'today 1-m'
						   geo='',  # сужение по гео 'GE'
						   gprop='')  # фильтр поиска 'images', 'news', 'youtube', 'froogle'...
	# не всегда related_queries обрабатывает без ошибок kw_list
	try:
		result = pytnd.related_queries()[kw_list]['rising']
		result = result.rename(columns={'query': 'related', 'value': 'frequency'})
		result['trending'] = kw_list
		result = result.astype({'frequency': 'int'})
	except:
		result = pd.DataFrame({'trending': [], 'related': [], 'frequency': []})
	return result


def collect_related(trending=False):
	"""собирает связанные запросы по списку тех что в тренде"""
	# запрашиваем список сло в тренде, если его нет
	if not trending:
		trending = get_trending()
	# собираем
	data = pd.DataFrame({'trending': [], 'related': [], 'frequency': []})
	for trend_word in trending:
		# получаем датафрейм с связными запросами и частотностью
		related = get_related(trend_word).sort_values('frequency', ascending=False).reset_index(drop=True)
		# отбираем только рускоязычные запросы
		related = related[related.apply(lambda x: True if re.search('[а-я]', x['related']) else False, axis=1)]
		# добавляем к имеющимся
		data = pd.concat([data, related], ignore_index=True)
	zone = zoneinfo.ZoneInfo("Europe/Moscow")
	data['date'] = datetime.datetime.now(zone).date().strftime('%s')
	data = data.astype({'trending': 'string', 'related': 'string', 'frequency': 'int', 'date': 'int'})
	return data


def get_sub_related(related):
	"""по связаным запроам (related) датафрейма collect_related собирает уже связанные с ними запросы"""
	# соберём список связанных слов которые будем использовать в качестве трендовых
	trending = related['related'].unique().tolist()
	result = collect_related(trending)
	return result


def collect_words():
	"""собираем коллекцию трендов и связных слов"""
	# делаем первый запрос и собираем самые трендовые слова, и связанные к ним
	data = collect_related()
	# собираем связанные слова по связанным из уже собранной коллекции
	get_sub_related(data)
	return data


def get_trending_by_date():
	"""собирает трендовые слова на дату"""
	data = pytnd.trending_searches(pn='russia').rename(columns={0: 'trending'})
	zone = zoneinfo.ZoneInfo("Europe/Moscow")
	data['date'] = datetime.datetime.now(zone).date()
	return data


def get_trending_popularity(word):
	"""по слову запроса возвращает датафрейм [date, popularity, trending]"""
	# kw_list запрос к которому нужно найти связанные с частотностью
	pytnd.build_payload(kw_list=[word],  # сужение запроса по категориям
						cat=0,  # сужение запроса по категориям 71
						timeframe='today 5-y',  # даты поиска '2017-02-06 2017-02-12', 'now 1-H', 'today 1-m'
						geo='',  # сужение по гео 'GE'
						gprop='')  # фильтр поиска 'images', 'news', 'youtube', 'froogle'...
	# не всегда related_queries обрабатывает без ошибок kw_list
	try:
		result = pytnd.interest_over_time().reset_index()
		date = [int(date.strftime('%s')) for date in result.date]
		result = pd.DataFrame({'date': date, 'popularity': result[word], 'trending': word})
	except:
		result = pd.DataFrame({'date': [], 'popularity': [], 'trending': []})
	result = result.astype({'date': 'int'})
	return result
