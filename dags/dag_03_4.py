import pandas as pd
from datetime import datetime, timedelta
from airflow.decorators import dag, task

path = '/var/lib/airflow/airflow.git/dags/a.batalov/vgsales.csv'
year = 1994 + hash(f'v-sizov') % 23

default_args = {
	'owner': 'v.sizov',
	'depends_on_past': False,
	'retries': 2,
	'retry_delay': timedelta(minutes=5),
	'start_date': datetime(2023, 5, 6),
	'schedule_interval': '0 0 * * *'
}


@dag(default_args=default_args, catchup=False)
def v_sizov_DA_35_lesson_3_2():
	# получение данных
	@task()
	def get_data():
		df = pd.read_csv(path)
		return df.convert_dtypes()[df.Year == year]

	# Какая игра была самой продаваемой в этом году во всем мире?
	@task()
	def best_global_sales(data):
		return data[data.Global_Sales == data.Global_Sales.max()].Name.values[0]

	# Игры какого жанра были самыми продаваемыми в Европе?
	@task()
	def best_eu_sales(data):
		return data.groupby('Genre').EU_Sales.sum().idxmax()

	# На какой платформе было больше всего игр, которые продались более чем миллионным тиражом в Северной Америке?
	@task()
	def platform(data):
		return data[data.NA_Sales > 1].groupby('Platform').Name.count().idxmax()

	# У какого издателя самые высокие средние продажи в Японии?
	@task()
	def high_mean_jp(data):
		return data.groupby('Publisher').JP_Sales.mean().idxmax()

	# Сколько игр продались лучше в Европе, чем в Японии?
	@task()
	def eu_better(data):
		return len(data[data.EU_Sales > data.JP_Sales])

	# показать результат в лог
	@task()
	def print_data(bgs, bes, p, hmj, eb):
		print(f'Игра {bgs} была самой продаваемой в этом году во всем мире.')
		print(f'Игры жанра {bes} были самыми продаваемыми в Европе.')
		print(
			f'На платформе {p} было больше всего игр, которые продались более чем миллионным тиражом в Северной Америке.')
		print(f'У издателя {hmj} самые высокие средние продажи в Японии')
		print(f'{eb} игр продались лучше в Европе, чем в Японии.')

	# порядок выполнения
	data = get_data()
	bgs = best_global_sales(data)
	bes = best_eu_sales(data)
	p = platform(data)
	hmj = high_mean_jp(data)
	eb = eu_better(data)
	print_data(bgs, bes, p, hmj, eb)


# запускаем даг
v_sizov_DA_35_lesson_3_2 = v_sizov_DA_35_lesson_3_2()