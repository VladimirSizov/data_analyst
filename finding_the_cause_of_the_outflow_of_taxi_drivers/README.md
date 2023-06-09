# Поиск причины оттока водителей такси

## Задача 

- изучить отток водителей и посмотреть, какие есть различия между водителями, которые покидают сервис, и которые остаются.
- протестировать гипотезы, выделить группы водителей, которые наиболее подвержены "оттоку".
- на основе результатов сделать выводы о том, что можно улучшить в сервисе, чтобы в дальнейшем внести изменения.
- проверить, есть ли различия в размерах оттока клиентов в разных городах.
- есть ли разница в активности в первые 30 дней с момента регистрации между водителями из разных городов?
- может ли отток быть связан с активностью в первые 30 дней после регистрации?
- проверить переменные и провести статистические тесты.

тесты: kruskal, gameshowell, mannwhitneyu

## Данные

avg_dist – среднее расстояние (в милях) за поездку в первые 30 дней после регистрации  
avg_rating_by_driver – средняя оценка поездок водителем  
avg_rating_of_driver – средняя оценка поездок водителя  
avg_surge – средний множитель всплеска за все поездки этого водителя  
city – город  
last_trip_date – дата последней поездки (YYYYMMDD)  
phone – основное устройство, которое использует водитель  
signup_date – дата регистрации аккаунта (YYYYMMDD)  
surge_pct – процент поездок, совершенных с множителем > 1  
trips_in_first_30_days – количество поездок, которые совершил водитель в первые 30 дней после регистрации  
luxury_car_user – TRUE, если пользователь в первые 30 дней использовал премиум-автомобиль  
weekday_pct – процент поездок пользователя, совершенных в будние дни  
  

## Используемые библиотеки

*pandas, numpy, pingouin, scipy, scikit_posthocs, seaborn* 
