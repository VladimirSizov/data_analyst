## Описание:
В репозитории представлены проекты курса [Аналитик данных](https://karpov.courses/analytics) (Karpov.Courses)

## Основные инструменты и навыки, полученные при обучении:

- Языки: Python, SQL
- Анализ данных: библиотеки Pandas, NumPy, SciPy, Pingouin, StatsModels
- Визуализация: Matplotlib, Plotly, Seaborn
- Построение дашбордов: Tableau
- Метрики юнит-экономики, когортный анализ
- Анализ результатов A/B тестов
- Работа с гипотезами
- Машинное обучение: библиотеки: FbProphet

## Проекты:
| №| Название и ссылка | О чем проект                                                     | Навыки и инструменты           |  
|-----------|-------------------|------------------------------------------------------------------|-----------------------------------|
|1              |[Анализ маркетинговых расходов интернет-магазина](marketing_traffic_analysis/)|Проанализировать чувствительные показатели аудитории. Оценить качество покупателей. Расходы отдела маркетинга. Подготовить обоснование для оптимизации работы с каналами привлечения.|`pandas` `numpy` `itertools` `matplotlib` `seaborn`|
|2              |[Составление SQL запросов в ClickHouse](pandahouse_sql/)|Составление SQL запросов в ClickHouse|`pandas` `pandahouse`|
|3              |[А/А-тестирование. Поиск ошибки системы сплитирования данных у мобильного приложения.](aa_test/)|Проверяем утверждение о поломке сплит системы и находим причины. Считаем результаты A/A-теста, проверяем FPR на конверсии в покупку. Делаем выводы, на основе анализа результатов A/A-теста.|`pandas` `numpy` `scipy` `random` `tqdm` `matplotlib` `seaborn`|
|4              |[RFM анализ](rfm_analysis/)|Проведите RFM анализ. В каждом подсегменте поделите пользователей на 4 класса.|`pandas` `numpy` `seaborn`|
|5              |[Изучение влияния погодных условий на прогнозирование количества аренд велосипедов в Лондоне](time_series_with_prediction/)|Выяснить на сколько сильно и какие факторы (сезонности, погодных условий) влияют на изменения количества аренды велосипедистов. Мы используем метод линейной регрессии для определения размера влияния, а также библиотеку fbprophet для предсказания количества аренды велосипедов.<br>методы: линейная регрессия, предсказание fbprophet|`pandas` `numpy` `patsy` `pingouin` `scipy` `statsmodels` `fbprophet` `calendar` `matplotlib` `seaborn`|
|6              |[Поиск причины оттока водителей такси](finding_the_cause_of_the_outflow_of_taxi_drivers/)|Изучить отток водителей и посмотреть, какие есть различия между водителями, которые покидают сервис, и которые остаются. Протестировать гипотезы, выделить группы водителей, которые наиболее подвержены "оттоку". На основе результатов сделать выводы о том, что можно улучшить в сервисе, чтобы в дальнейшем внести изменения. Проверить, есть ли различия в размерах оттока клиентов в разных городах. Есть ли разница в активности в первые 30 дней с момента регистрации между водителями из разных городов? Может ли отток быть связан с активностью в первые 30 дней после регистрации? Проверить переменные и провести статистические тесты.<br>тесты: kruskal, gameshowell, mannwhitneyu|`pandas` `numpy` `pingouin` `scipy` `scikit_posthocs` `seaborn`|
|7              |[Предсказание стоимости машины методом линейной регрессии](predicting_the_cost_of_a_car_using_linear_regression/)|Попробуем предсказать стоимость машин и понять, от каких факторов зависит ценообразование на автомобили. Узнаем, какие переменные важны для прогнозирования и насколько хорошо полученная модель описывает данные.|`pandas` `numpy` `statsmodels` `seaborn`|
|8              |[Анализ результатов A/B/C теста, а также A/B теста сегментированных пользователей](analysis_of_the_results_of_the_ab_test_of_segmented_users/)|Проверяем результаты A/B/C теста с изображениями блюд в приложении (прямоугольные или квадратные). Выявляем какие изображения будем использовать. Проверяем результаты A/B теста, делаем выводы о наличии изменений в данных на основании статистических тестов.|`pandas` `statsmodels` `pingouin` `seaborn`|
|9              |[Анализ результатов A/B теста методами t-тест, U-тест, бутстрап средних](bootstrap_test_result_AB_test/)|Проверяем стали ли мы больше зарабатывать с пользователя или нет. Подбираем инструмент (t-тест, U-тест Mann-Whitney или бутстрап) Считаем p-value тремя способами: t-тест, U-тест, бутстрап средних. Сравниваем результат между тестом и контролем по всем этим кейсам. Делаем выводы о наличии/отсутствии значимых различий, на основе анализа примененных критериев.|`pandas` `numpy` `scipy` `pingouin` `statsmodels` `random` `matplotlib` `seaborn`|
|10             |[Когортный анализ Retention и RFM сегментация](cohort_retention_analysis_and_rfm_segmentation/)|Выявляем когорту с самым высоким retention на 3й месяц. Строим RFM-сегментацию пользователей, чтобы качественно оценить свою аудиторию.|`pandas` `numpy` `datetime` `seaborn` `matplotlib`|
|11             |[Построение доверительного интервала для определения аномалий](confidence_interval_for_determining_anomalies/)|Получаем данные, преобразуем число поездок по дням. Определяем и добавляем границы 99% доверительного интервала в данные. Строим график по числу поездок. Изучаем аномально высокие и низкие значения. Находим причину данной аномалии.|`pandas` `numpy` `scipy` `datetime` `seaborn` `matplotlib`|
|12             |[Анализ эффективности рекламных каналов](analysis_of_the_effectiveness_of_advertising_channels/)|Анализируем поведение пользователей, а также оцениваем эффективность каналов их привлечения. Делаем когортный анализ, и считаем конверсию в течение 7 дней. Строим воронку и находим самые большие точки оттока пользователей. Определяем рекламный канал: с самым большим притоком пользователей, с самой низкой конверсией, с самым большим первым чеком, с самым высоким ROMI|`pandas` `numpy` `seaborn` `matplotlib`|
|13             |[vv](https://public.tableau.com/app/profile/vladimir.sizov/viz/SalaryComparisonSkills/OverviewVacancies)|vv|`tableau`|







