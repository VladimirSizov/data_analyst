# Анализ маркетинговых расходов интернет-магазина

## Задача 

- проанализировать чувствительные показатели аудитории  
- оценить качество покупателей  
- расходы отдела маркетинга  
- подготовить обоснование для оптимизации работы с каналами привлечения.  

### Посчитать:
Аудитория:  
- размер аудитории, MAU, WAU, DAU  
- качество взаимодействия, количество сессий, просмотров на сессию, фактор залипания  
- RR показатель удержания пользователей  

Продажи:  
- GM валовая прибыль  
- количество покупателей, количество покупок, покупок на пользователя  
- средний чек  
- CR1 конверсия в покупку, время первой покупки после установки  
- ARPPU средний доход на покупателя  

Источники трафика и маркетинг:  
- расходы на рекламу всего и по источникам  
- стоимость привлечения покупателя по источникам  
- LTV прибыль которую приносит клиент  
- ROMI коэффициент возврата маркетинговых инвестиций  

## Данные

### devices - склейка устройств и User ID  
DeviceID — идентификатор устройства  
UserID — идентификатор пользователя  

### installs данные регистрации в системе, и источниках трафика  
DeviceID — идентификатор устройства  
InstallationDate — дата регистрации  
InstallCost — цена привлечения клиента  
Platform — платформа  
Source — источник трафика  

### events - данные об активности просмотра товаров  
DeviceID — идентификатор устройства  
AppPlatform — платформа  
EventDate — дата события  
events — количество просмотров всех товаров за этот день у этого DeviceID.  

### checks - данные о покупках и их стоимости   
UserID — идентификатор пользователя  
Rub — суммарный чек пользователя  
BuyDate — дата  

## Используемые библиотеки

*pandas, numpy, itertools, matplotlib, seaborn* 