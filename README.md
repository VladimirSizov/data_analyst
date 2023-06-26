### В репозитории представлены:
### - тестовые проекты
### - проекты [курс Аналитик данных](https://karpov.courses/analytics) Karpov.Courses
### - SQL запросы [курс Симулятор SQL](https://karpov.courses/simulator-sql) Karpov.Courses
<hr>

### Практиковал:
Проверять результаты A/A, A/B и A/B/C тестов.   
Считать продуктовые метрики (DAU, stick factor, средний чек, покупок на пользователя, CR1, ARPPU, CPAcq, LTV, CAC, ROMI).  
Работать с гипотезами: формулировать, приоритизировать, проверять.  
Выявлять наиболее эффективные каналы маркетинга.  
Составлять сложные SQL запросы (оконные функции, подзапросы, join-ы).  
Предсказывать churn rate по проксиметрикам (LogisticRegression, RandomForest).  
Собирать данные из открытых источников, обращаться по API в (Telegram, VK, Google Sheets).  
Строить графики и разрабатывать дашборды в BI системах.  
Прогнозировать спрос (FbProphet).  
Считать retention rate.  
Проводить RFM анализ.  
Строить воронку.  
Кластеризовать пользователей.   
Работать с GitLab и Airflow.   

Знаю основы математической статистики и теории вероятности, работать со статистическими методами.  

### Инструменты:  
Языки: Python, SQL(PostgreSQL, ClickHouse), Bash  
Библиотеки: Pandas, NumPy, SciPy, Pingouin, StatsModels, FbProphet, SkLearn, Matplotlib, Seaborn, PandaHouse  
Дашборды: Tableau, DataLens  

![-](https://github.com/VladimirSizov/data_analyst/blob/main/sertificat_rus.jpg)

### Проекты:
| №| Название и ссылка | О чем проект                                                     | Библиотеки           |  
|-----------|-------------------|------------------------------------------------------------------|-----------------------------------|
|1              |[Проверка результатов A/B тестирования дейтингового приложения](checking_ab_test_results/)|Провели проверку сплит системы. Проверили результаты A/B теста (известно что в тестовой группе изменилась цена подписки). Выявили изменения в: Revenue, ARPU, ARPPU, CR1, среднего чека и выбора подписки, в зависимости от: страны, пола, дня посещения, возраста пользователя, индекса привлекательности а также измерили их значения. Провели когортный анализ Retention rate по подписке. Выявили долю увеличения числа подписок с новой ценой. Сделали выводы об успешности эксперимента.|`requests` `urllib` `pandas` `numpy` `random` `scipy` `pingouin` `tqdm, matplotlib` `seaborn`|
|2              |[Приоритизация фичей бэклога методами RICE и ICE](hypotheses_prioritization/)|Рассчитали продуктовые метрики на данных текущих продаж. Проверили размер плечей метрик и опредилили метрики с максимальным плечом. Рассчитали impact (как размер прироста CM) каждой фичи в случае ожидаемого успеха при её внедрении. С помощью методов RICE и ICE приоритизировали фичи бэклога.|`pandas` `inspect`|
|3              |[Анализ маркетинговых расходов интернет-магазина](marketing_traffic_analysis/)|Проанализировали чувствительные показатели аудитории. Оценили качество покупателей. Расходы отдела маркетинга. Подготовили обоснование для оптимизации работы с каналами привлечения.<br>MAU Сессий, просмотров покупок на пользователя. День первой покупки после регистрации. Размеры когорт. Retention rate, средний чек по когортам/месяцам. Рекламные расходы, ARPPU по источникам.<br>Пользователей, покупателей, CR1, margin по платным/бесплатным источникам.<br>GM, % CAC в стоимости товара, ARPPU, LTV, ROMI по источникам/когортам.|`pandas` `numpy` `itertools` `matplotlib` `seaborn`|
|4              |[Сбор данных из открытых источников](collection_data_open_sources/)|Это пример некоторых методов получения данных из Google Trends и записи в собственную БД sqlite3. Настройки сценария автообновления БД. |`pytrends` `sqlite3` `pandas` `datetime` `zoneinfo` `re`|
|5              |[Прогнозирование оттока и кластеризация пользователей телекоммуникационной компании](churn_prediction_and_clustering/)|Выявили зависимые показатели и возможные причины оттока пользователей. Использовали библиотеки логистической регрессии и случайный лес, и определили какая модель обладает лучшими показателями предсказания. Для улучшения показателей прогноза попробовали применить нормализацию данных, а также использовать подбор оптимального минимального порога корреляции переменных. Кластеризовали пользователей.|`pandas` `numpy` `sklearn` `scipy` `matplotlib` `seaborn`|
|6              |[Составление SQL запросов в ClickHouse](pandahouse_sql/)|Составили SQL запросы в ClickHouse|`pandas` `pandahouse`|
|7              |[Дашборд HH сравнение вакансий Аналитиков](https://public.tableau.com/app/profile/vladimir.sizov/viz/SalaryComparisonSkills/OverviewVacancies)| Обзор рынка вакансий Аналитиков на HH. В разрезах сравнения уровня зарплат разных специализаций или набора требуемых скиллов|`tableau`|
|8              |[Написание дагов для AirFlow](dags/)|топ-10 доменных зон по численности доменов <br> домен с самым длинным именем <br> определяет на каком месте находится домен airflow.com<br>Какая игра была самой продаваемой в этом году во всем мире?<br>Игры какого жанра были самыми продаваемыми в Европе?<br>На какой платформе было больше всего игр, которые продались более чем миллионным тиражом в Северной Америке?<br>У какого издателя самые высокие средние продажи в Японии?<br>Сколько игр продались лучше в Европе, чем в Японии?|`airflow` |
|9              |[Анализ результатов A/B теста методами t-тест, U-тест, бутстрап средних](bootstrap_test_result_AB_test/)|Проверили стали ли мы больше зарабатывать с пользователя или нет. Подобрали инструмент (t-тест, U-тест Mann-Whitney или бутстрап) Посчиталм p-value тремя способами: t-тест, U-тест, бутстрап средних. Сравнили результат между тестом и контролем по всем этим кейсам. Сделали выводы о наличии/отсутствии значимых различий, на основе анализа примененных критериев.|`pandas` `numpy` `scipy` `pingouin` `statsmodels` `random` `matplotlib` `seaborn`|
|10             |[Анализ результатов A/B/C теста, а также A/B теста сегментированных пользователей](analysis_of_the_results_of_the_ab_test_of_segmented_users/)|Проверили результаты A/B/C теста с изображениями блюд в приложении (прямоугольные или квадратные). Выявили какие изображения будем использовать. Проверили результаты A/B теста, сделали выводы о наличии изменений в данных на основании статистических тестов.|`pandas` `statsmodels` `pingouin` `seaborn`|
|11             |[А/А-тестирование. Поиск ошибки системы сплитирования данных у мобильного приложения.](aa_test/)|Проверили утверждение о поломке сплит системы и нашли причины. Считали результаты A/A-теста, проверяли FPR на конверсии в покупку. Сделали выводы, на основе анализа результатов A/A-теста.|`pandas` `numpy` `scipy` `random` `tqdm` `matplotlib` `seaborn`|
|12              |[RFM анализ](rfm_analysis/)|Провели RFM анализ. В каждом подсегменте поделили пользователей на 4 класса.|`pandas` `numpy` `seaborn`|
|13             |[Изучение влияния погодных условий на прогнозирование количества аренд велосипедов в Лондоне](time_series_with_prediction/)|Выяснили на сколько сильно и какие факторы (сезонности, погодных условий) влияют на изменения количества аренды велосипедов. Использовали метод линейной регрессии для определения размера влияния, а также библиотеку fbprophet для предсказания количества аренды велосипедов.<br>методы: линейная регрессия, fbprophet|`pandas` `numpy` `patsy` `pingouin` `scipy` `statsmodels` `fbprophet` `calendar` `matplotlib` `seaborn`|
|14             |[Поиск причины оттока водителей такси](finding_the_cause_of_the_outflow_of_taxi_drivers/)|Изучили отток водителей и посмотрели, какие есть различия между водителями, которые покидают сервис, и которые остаются. Протестировали гипотезы, выделили группы водителей, которые наиболее подвержены оттоку. На основе результатов сделали выводы о том, что можно улучшить в сервисе, чтобы в дальнейшем внести изменения. Проверили, есть ли различия в размерах оттока клиентов в разных городах, есть ли разница в активности в первые 30 дней с момента регистрации между водителями из разных городов, может ли отток быть связан с активностью в первые 30 дней после регистрации. Проверили переменные и провели статистические тесты.<br>тесты: kruskal, gameshowell, mannwhitneyu|`pandas` `numpy` `pingouin` `scipy` `scikit_posthocs` `seaborn`|
|15             |[Предсказание стоимости машины методом линейной регрессии](predicting_the_cost_of_a_car_using_linear_regression/)|Предсказали стоимость машин и поняли, от каких факторов зависит ценообразование на автомобили. Узнали, какие переменные важны для прогнозирования и насколько хорошо полученная модель описывает данные.|`pandas` `numpy` `statsmodels` `seaborn`|
|16             |[Когортный анализ Retention и RFM сегментация](cohort_retention_analysis_and_rfm_segmentation/)|Выявили когорту с самым высоким retention на 3й месяц. Построили RFM-сегментацию пользователей, чтобы качественно оценить свою аудиторию.|`pandas` `numpy` `datetime` `seaborn` `matplotlib`|
|17             |[Построение доверительного интервала для определения аномалий](confidence_interval_for_determining_anomalies/)|Получили данные, преобразовали число поездок по дням. Определили и добавили границы 99% доверительного интервала в данные. Построили график по числу поездок. Изучили аномально высокие и низкие значения. Нашли причину данной аномалии.|`pandas` `numpy` `scipy` `datetime` `seaborn` `matplotlib`|
|18             |[Анализ эффективности рекламных каналов](analysis_of_the_effectiveness_of_advertising_channels/)|Анализировали поведение пользователей, а также оценили эффективность каналов их привлечения. Сделали когортный анализ, и посчитали конверсию в течение 7 дней. Построили воронку и нашли самые большие точки оттока пользователей. Определили рекламный канал: с самым большим притоком пользователей, с самой низкой конверсией, с самым большим первым чеком, с самым высоким ROMI|`pandas` `numpy` `seaborn` `matplotlib`|
|19             |[Дашборд Показатель прибыли мебельного магазина](https://datalens.yandex.ru/fpt156juk09u5-profit-overview?state=3f58d38a86)|Визуализация прибыли по срезам категорий товаров и регионов доставки|`datalens`|
