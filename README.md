## В репозитории представлены проекты курса [Аналитик данных](https://karpov.courses/analytics) Karpov.Courses

### В процессе обучения получил навыки:
Составлять сложные SQL запросы (оконные функции, подзапросы, join-ы)  
Считать продуктовые метрики (DAU, stick factor, средний чек, CR1, ARPPU, CPAcq, LTV, CAC, ROMI)  
Считать retention rate  
Проводить когортный анализ  
Проводить RFM сегментацию и анализ  
Строить воронку  
Проверять результаты A/A, A/B и A/B/C тестов    
Выявлять наиболее эффективные каналы маркетинга  
Предсказывать churn rate по проксиметрикам  
Кластеризовать пользователей  


### Использовать статистические методы:  
Определять эффекты изменений (t-test, ранговые тесты, диспесионный анализ, бутстрап)  
Искать закономерности в данных (корреляция), прогнозирование (LogisticRegression, RandomForest, FbProphet)  

### 
Работать с гипотезами
Строить графики и разрабатывать дашборды
Знаю основы математической статистики и теории вероятности

### Инструменты:  
Языки: Python, SQL(PostgreSQL, ClickHouse), Bash  
Библиотеки: Pandas, NumPy, SciPy, Pingouin, StatsModels, FbProphet, SkLearn, Matplotlib, Seaborn  
Дашборды: Tableau, DataLens  
GitLab, Airflow  

### Проекты:
| №| Название и ссылка | О чем проект                                                     | Навыки и инструменты           |  
|-----------|-------------------|------------------------------------------------------------------|-----------------------------------|
|1              |[Анализ маркетинговых расходов интернет-магазина](marketing_traffic_analysis/)|Проанализировали чувствительные показатели аудитории. Оценили качество покупателей. Расходы отдела маркетинга. Подготовили обоснование для оптимизации работы с каналами привлечения.|`pandas` `numpy` `itertools` `matplotlib` `seaborn`|
|2              |[Прогнозирование оттока и кластеризация пользователей телекоммуникационной компании](churn_prediction_and_clustering/)|Выявили зависимые показатели и возможные причины оттока пользователей. Использовали библиотеки логистической регрессии и случайный лес, и определили какая модель обладает лучшими показателями предсказания. Для улучшения показателей прогноза попробовали применить нормализацию данных, а также использовать подбор оптимального минимального порога корреляции переменных. Кластеризовали пользователей.|`pandas` `numpy` `sklearn` `scipy` `matplotlib` `seaborn`|
|10              |[Анализ результатов A/B теста методами t-тест, U-тест, бутстрап средних](bootstrap_test_result_AB_test/)|Проверили стали ли мы больше зарабатывать с пользователя или нет. Подобрали инструмент (t-тест, U-тест Mann-Whitney или бутстрап) Посчиталм p-value тремя способами: t-тест, U-тест, бутстрап средних. Сравнили результат между тестом и контролем по всем этим кейсам. Сделали выводы о наличии/отсутствии значимых различий, на основе анализа примененных критериев.|`pandas` `numpy` `scipy` `pingouin` `statsmodels` `random` `matplotlib` `seaborn`|
|9              |[Анализ результатов A/B/C теста, а также A/B теста сегментированных пользователей](analysis_of_the_results_of_the_ab_test_of_segmented_users/)|Проверили результаты A/B/C теста с изображениями блюд в приложении (прямоугольные или квадратные). Выявили какие изображения будем использовать. Проверили результаты A/B теста, сделали выводы о наличии изменений в данных на основании статистических тестов.|`pandas` `statsmodels` `pingouin` `seaborn`|
|3              |[Составление SQL запросов в ClickHouse](pandahouse_sql/)|Составили SQL запросы в ClickHouse|`pandas` `pandahouse`|
|14             |[Дашборд HH сравнение вакансий Аналитиков](https://public.tableau.com/app/profile/vladimir.sizov/viz/SalaryComparisonSkills/OverviewVacancies)|Обзор рынка вакансий Аналитиков на HH. В разрезах сравнения уровня зарплат разных специализаций или набора требуемых скиллов|`tableau`|
|4              |[А/А-тестирование. Поиск ошибки системы сплитирования данных у мобильного приложения.](aa_test/)|Проверили утверждение о поломке сплит системы и нашли причины. Считали результаты A/A-теста, проверяли FPR на конверсии в покупку. Сделали выводы, на основе анализа результатов A/A-теста.|`pandas` `numpy` `scipy` `random` `tqdm` `matplotlib` `seaborn`|
|5              |[RFM анализ](rfm_analysis/)|Провели RFM анализ. В каждом подсегменте поделили пользователей на 4 класса.|`pandas` `numpy` `seaborn`|
|6              |[Изучение влияния погодных условий на прогнозирование количества аренд велосипедов в Лондоне](time_series_with_prediction/)|Выяснили на сколько сильно и какие факторы (сезонности, погодных условий) влияют на изменения количества аренды велосипедов. Использовали метод линейной регрессии для определения размера влияния, а также библиотеку fbprophet для предсказания количества аренды велосипедов.<br>методы: линейная регрессия, fbprophet|`pandas` `numpy` `patsy` `pingouin` `scipy` `statsmodels` `fbprophet` `calendar` `matplotlib` `seaborn`|
|7              |[Поиск причины оттока водителей такси](finding_the_cause_of_the_outflow_of_taxi_drivers/)|Изучили отток водителей и посмотрели, какие есть различия между водителями, которые покидают сервис, и которые остаются. Протестировали гипотезы, выделили группы водителей, которые наиболее подвержены оттоку. На основе результатов сделали выводы о том, что можно улучшить в сервисе, чтобы в дальнейшем внести изменения. Проверили, есть ли различия в размерах оттока клиентов в разных городах, есть ли разница в активности в первые 30 дней с момента регистрации между водителями из разных городов, может ли отток быть связан с активностью в первые 30 дней после регистрации. Проверили переменные и провели статистические тесты.<br>тесты: kruskal, gameshowell, mannwhitneyu|`pandas` `numpy` `pingouin` `scipy` `scikit_posthocs` `seaborn`|
|8              |[Предсказание стоимости машины методом линейной регрессии](predicting_the_cost_of_a_car_using_linear_regression/)|Предсказали стоимость машин и поняли, от каких факторов зависит ценообразование на автомобили. Узнали, какие переменные важны для прогнозирования и насколько хорошо полученная модель описывает данные.|`pandas` `numpy` `statsmodels` `seaborn`|
|11             |[Когортный анализ Retention и RFM сегментация](cohort_retention_analysis_and_rfm_segmentation/)|Выявили когорту с самым высоким retention на 3й месяц. Построили RFM-сегментацию пользователей, чтобы качественно оценить свою аудиторию.|`pandas` `numpy` `datetime` `seaborn` `matplotlib`|
|12             |[Построение доверительного интервала для определения аномалий](confidence_interval_for_determining_anomalies/)|Получили данные, преобразовали число поездок по дням. Определили и добавили границы 99% доверительного интервала в данные. Построили график по числу поездок. Изучили аномально высокие и низкие значения. Нашли причину данной аномалии.|`pandas` `numpy` `scipy` `datetime` `seaborn` `matplotlib`|
|13             |[Анализ эффективности рекламных каналов](analysis_of_the_effectiveness_of_advertising_channels/)|Анализировали поведение пользователей, а также оценили эффективность каналов их привлечения. Сделали когортный анализ, и посчитали конверсию в течение 7 дней. Построили воронку и нашли самые большие точки оттока пользователей. Определили рекламный канал: с самым большим притоком пользователей, с самой низкой конверсией, с самым большим первым чеком, с самым высоким ROMI|`pandas` `numpy` `seaborn` `matplotlib`|

|15             |[Дашборд Показатель прибыли мебельного магазина](https://datalens.yandex.ru/fpt156juk09u5-profit-overview?state=3f58d38a86)|Визуализация прибыли по срезам категорий товаров и регионов доставки|`datalens`|







