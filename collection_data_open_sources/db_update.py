# методы добавления данных в БД

import datetime
import zoneinfo

import db_query
import pseudo_api


def add_new_date_trending():
    """добавление новых слов в date_trending"""
    # дата сегодня
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    date_now = int(datetime.datetime.now(zone).date().strftime('%s'))
    # получаем данные из таблицы date_trending БД на сегодня
    db_data = db_query.read_date_trending()
    # отбираем значения date_trending записаные сегодня которые уже есть в базе
    db_data = db_data[db_data.date == date_now].trending.tolist()
    # получаем те что в трендинге сейчас, запросив у google trends
    trending_now = pseudo_api.get_trending()
    # добавляем в БД новые слова
    for trending in trending_now:
        if trending not in db_data:
            print(trending)
            db_query.write_date_trending(trending, date_now)
    print("Table 'date_trending' updated.")


def add_new_trending_related():
    """добавление новых слов в trending_related"""
    # дата сегодня
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    date_now = int(datetime.datetime.now(zone).date().strftime('%s'))
    # получаем из БД date_trending список trending на сегодня
    db_date_trending = db_query.read_date_trending()
    db_date_trending = db_date_trending[db_date_trending.date == date_now].trending.tolist()
    # запрашиваем у google trends связанные запросы на сегодняшние trending
    collect_related = pseudo_api.collect_related(db_date_trending)
    # получаем из БД trending_related на сегодня
    db_trending_related = db_query.read_trending_related()
    db_trending_related = db_trending_related[db_trending_related.date == date_now].reset_index()
    # добавим или обновим данные в таблице trending_related
    trs = 0
    add = 0
    upd = 0
    hav = 0
    low = 0
    for n in range(len(collect_related)):
        new = collect_related.loc[n]
        # пропускаем низкочастотные
        if new.frequency < 30000:
            trs += 1
            continue
        else:
            # если в БД на сегодня не было записей
            if len(db_trending_related) == 0:
                db_query.write_trending_related(new.trending, new.related, new.frequency, new.date)
                add += 1
            else:
                flag = True
                for o in range(len(db_trending_related)):
                    old = db_trending_related.loc[o]
                    if new.trending == old.trending:
                        if new.related == old.related:
                            if int(new.date) == int(old.date):
                                # пропускаем, если в БД есть запись с такими значениями
                                if new.frequency == old.frequency:
                                    hav += 1
                                    flag = False
                                    break
                                # обновляем, если запись есть, но нужно исправить frequency
                                if new.frequency > old.frequency:
                                    db_query.update_trending_related(old.id, new.frequency)
                                    upd += 1
                                    flag = False
                                    break
                                # пропускаем, если запись есть, но исправлять frequency не нужно
                                if new.frequency < old.frequency:
                                    low += 1
                                    flag = False
                                    break
                # добавляем, если в БД такой записи нет
                if flag:
                    db_query.write_trending_related(new.trending, new.related, new.frequency, new.date)
                    add += 1
    print("Table 'trending_related' updated.")
    print('    trash =', trs, 'add new =', add, ', upd old =', upd, ', have =', hav, ', low freq =', low)


def add_word_in_week_popularity(word):
    """добавление нового слова на разные даты (недели) в week_popularity"""
    # получаем данные из БД
    old_data = db_query.read_week_popularity().to_numpy()
    # получаем новые данные
    new_data = pseudo_api.get_trending_popularity(word)
    # вносим новые данные в БД
    for i in range(len(new_data)):
        new_date = new_data.loc[i].date
        new_trending = new_data.loc[i].trending
        new_popularity = new_data.loc[i].popularity
        # смотрим есть ли в записях БД
        flag = True
        for k in range(len(old_data)):
            old_date = old_data[k][3]
            old_trending = old_data[k][1]
            if (new_date == old_date) & (new_trending == old_trending):
                # если запись в БД уже есть - прерываем
                flag = False
                break
        #  если записи ещё нет
        if flag:
            # записываем в БД
            db_query.write_week_popularity(new_trending, new_popularity, new_date)
    print('New', word, 'writes')


def add_new_week_popularity():
    """добавление всех сегодняшних слов в тренде в 'week_popularity'"""
    # дата сегодня
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    date_now = int(datetime.datetime.now(zone).date().strftime('%s'))
    # получаем из БД date_trending список trending на сегодня
    db_date_trending = db_query.read_date_trending()
    db_date_trending = db_date_trending[db_date_trending.date == date_now].trending.tolist()
    for word in db_date_trending:
        # добавляем в таблицу week_popularity БД значения популярности для трендового слова на каждую неделю за последние 5 лет
        add_word_in_week_popularity(word)
    print("All today trending add popularity in 'week_popularity'")


def add_if_fail():
    """добавляем в week_popularity всё чего не добавили когда либо"""
    # получаем данные из таблицы date_trending БД на сегодня
    db_data = db_query.read_date_trending()
    trending_all = db_data.trending.unique()
    # получаем те что есть в БД популярные
    old_data = db_query.read_week_popularity()
    have = old_data.trending.unique()
    # добавляем новые
    for word in trending_all:
        if word not in have:
            try:
                add_word_in_week_popularity(word)
                print('add', word)
            except:
                print('fail download', word)
    print("'add_if_fail' function done.")