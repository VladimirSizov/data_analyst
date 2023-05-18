# Прогнозирование оттока и кластеризация пользователей телекоммуникационной компании

## Задача 
Определили показатели и возможные причины оттока пользователей.
Подготовили данные, определили какая модель обладает лучшими показателями предсказания
Попробовали применить нормализацию данных для улучшения показателей, а также использовать подбор оптимального для прогноза минимального порога корреляции переменных.
Библиотеки логистической регрессии и случайный лес.
Кластеризовали пользователей и сравнили их характеристики.


## Данные

customerID = id пользователя
gender - пол (Male, Female)
SeniorCitizen — является ли клиент пожилым гражданином или нет (1, 0)
Partner — есть ли у клиента партнер или нет (Yes, No)
Dependents - есть ли у клиента иждивенцы или нет (Yes, No)
tenure - Количество месяцев, в течение которых клиент оставался в компании
PhoneService — есть ли у клиента телефонная служба или нет (Yes, No)
MultipleLines — есть ли у клиента несколько линий или нет (Yes, No, No phone service)
InternetService - интернет-провайдер клиента (DSL, Fiber optic, No)
OnlineSecurity — есть ли у клиента онлайн-защита или нет (Yes, No, No internet service)
OnlineBackup — есть ли у клиента онлайн-резервное копирование или нет (Yes, No, No internet service)
DeviceProtection — есть ли у клиента защита устройства или нет (Yes, No, No internet service)
TechSupport — есть ли у клиента техническая поддержка или нет (Yes, No, No internet service)
StreamingTV — есть ли у клиента потоковое телевидение или нет (Yes, No, No internet service)
StreamingMovies — есть ли у клиента потоковые фильмы или нет (Yes, No, No internet service)
Contract - Срок контракта клиента (Month-to-month, One year, Two year)
PaperlessBilling — есть ли у клиента безбумажный биллинг или нет (Yes, No)
PaymentMethod — способ оплаты клиента
(электронный чек, чек по почте, банковский перевод (автоматический), кредитная карта (автоматический))
(Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
MonthlyCharges — сумма, взимаемая с клиента ежемесячно
TotalCharges — общая сумма, списанная с клиента
Churn — ушёл ли клиент или нет (Yes or No)

## Используемые библиотеки

*pandas, numpy, sklearn, scipy, matplotlib, seaborn* 
