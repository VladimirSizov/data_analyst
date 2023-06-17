# обращение к БД

import pandas as pd

import db_connect

def read_date_trending():
    """чтение всех данных из date_trending"""
    # получаем данные
    query = """SELECT * from date_trending"""
    data = db_connect.read_query(db_connect.connection, query)
    # получаем список колонок
    query_columns = """PRAGMA table_info(date_trending);"""
    columns = [i[1] for i in db_connect.read_query(db_connect.connection, query_columns)]
    # собираем датафрейм
    df = pd.DataFrame(data=data, columns=columns)
    df['trending'] = df.trending.astype('string')
    return df


def write_date_trending(trending, date):
    """делаем запись в date_trending"""
    query = 'INSERT INTO date_trending (trending, date) VALUES ' \
        + str((trending, date)) + ';'
    db_connect.write_query(db_connect.connection, query)


def read_trending_related():
    """чтение всех данных из trending_related"""
    # получаем данные
    query = """SELECT * from trending_related"""
    data = db_connect.read_query(db_connect.connection, query)
    # получаем список колонок
    query_columns = """PRAGMA table_info(trending_related);"""
    columns = [i[1] for i in db_connect.read_query(db_connect.connection, query_columns)]
    # собираем датафрейм
    df = pd.DataFrame(data=data, columns=columns)
    df['trending'] = df.trending.astype('string')
    df['related'] = df.related.astype('string')
    return df


def write_trending_related(trending, related, frequency, date):
    """делаем запись в trending_related"""
    query = 'INSERT INTO trending_related (trending, related, frequency, date) VALUES ' \
        + str((trending, related, frequency, date)) + ';'
    db_connect.write_query(db_connect.connection, query)


def update_trending_related(db_id, new_frequency):
    """обновляем частотность запись в trending_related"""
    query = 'UPDATE trending_related SET frequency = ' + str(new_frequency) + ' WHERE id = ' + str(db_id)
    db_connect.write_query(db_connect.connection, query)


def delete_trending_related(db_id):
    """удаляем запись в trending_related по id"""
    query = 'DELETE FROM trending_related WHERE id = ' + str(db_id)
    db_connect.write_query(db_connect.connection, query)


def read_week_popularity():
    """чтение данных из week_popularity"""
    # получаем данные
    query = """SELECT * from week_popularity"""
    data = db_connect.read_query(db_connect.connection, query)
    # получаем список колонок
    query_columns = """PRAGMA table_info(week_popularity);"""
    columns = [i[1] for i in db_connect.read_query(db_connect.connection, query_columns)]
    # собираем датафрейм
    df = pd.DataFrame(data=data, columns=columns)
    return df


def write_week_popularity(trending, popularity, date):
    """делаем запись в week_popularity"""
    query = 'INSERT INTO week_popularity (trending, popularity, date) VALUES ' \
        + str((trending, popularity, date)) + ';'
    db_connect.write_query(db_connect.connection, query)

