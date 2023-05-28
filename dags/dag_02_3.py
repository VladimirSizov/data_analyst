import re
import pandas as pd
from datetime import timedelta
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

TOP_1M_DOMAINS = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
TOP_1M_DOMAINS_FILE = 'top-1m.csv'

def get_data():
    # Здесь пока оставили запись в файл, как передавать переменую между тасками будет в третьем уроке
    top_doms = pd.read_csv(TOP_1M_DOMAINS)
    top_data = top_doms.to_csv(index=False)

    with open(TOP_1M_DOMAINS_FILE, 'w') as f:
        f.write(top_data)


# топ-10 доменных зон по численности доменов
def get_top_10():
    # читаем файл
    data = pd.read_csv(TOP_1M_DOMAINS_FILE, names=['rank', 'domain'])
    # отбираем самые популярные TLD
    pattern = re.compile('\.(.+)')
    data['TLD'] = data.domain.apply(lambda x: pattern.findall(x)[0])
    share_most_popular_TLD = data.TLD.value_counts().head(10)
    # записываем в csv
    with open('share_most_popular_TLD.csv', 'w') as f:
        f.write(share_most_popular_TLD.to_csv(header=False))


# домен с самым длинным именем
def get_longest_name():
    # читаем файл
    data = pd.read_csv(TOP_1M_DOMAINS_FILE, names=['rank', 'domain'])
    data['len'] = data.domain.apply(lambda x: len(x))
    longest_names = data[data.len == data.len.max()].domain.tolist()
    longest_name = sorted(longest_names)[0]
    with open('longest_name.txt', 'w') as f:
        f.write(longest_name)


# определяет на каком месте находится домен airflow.com
def get_airflow_rank():
    data = pd.read_csv(TOP_1M_DOMAINS_FILE, names=['rank', 'domain'])
    airflow_rank = data[data.domain == 'airflow.com']['rank'].values[0]
    with open('airflow_rank.txt', 'w') as f:
        f.write(str(airflow_rank))


def print_data(ds):
    date = ds
    with open('share_most_popular_TLD.csv', 'r') as f:
        share_most_popular_TLD = f.read()
    print(f'Share most popular TLD for date {date}')
    print(share_most_popular_TLD)

    with open('longest_name.txt', 'r') as f:
        longest_name = f.read()
    print(f'Longest domain name for date {date}')
    print(longest_name)

    with open('airflow_rank.txt', 'r') as f:
        airflow_rank = f.read()
    print(f'Domain rank airflow.com for date {date}')
    print(airflow_rank)


default_args = {
    'owner': 'v.sizov',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=6),
    'start_date': datetime(2023, 5, 6),
}
schedule_interval = '0 12 * * *'


dag = DAG('v-sizov_DA_35_lesson_2_3', default_args=default_args, schedule_interval=schedule_interval)

t1 = PythonOperator(task_id='get_data',
                    python_callable=get_data,
                    dag=dag)

t2_1 = PythonOperator(task_id='get_top_10',
                      python_callable=get_top_10,
                      dag=dag)

t2_2 = PythonOperator(task_id='get_longest_name',
                      python_callable=get_longest_name,
                      dag=dag)

t2_3 = PythonOperator(task_id='get_airflow_rank',
                      python_callable=get_airflow_rank,
                      dag=dag)

t3 = PythonOperator(task_id='print_data',
                    python_callable=print_data,
                    dag=dag)

t1 >> [t2_1, t2_2, t2_3] >> t3

#t1.set_downstream(t2)
#t1.set_downstream(t2_com)
#t2.set_downstream(t3)
#t2_com.set_downstream(t3)
