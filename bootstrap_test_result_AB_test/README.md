# Анализ результатов A/B теста методами t-тест, U-тест, бутстрап средних

## Задача 

Проверяем стали ли мы больше зарабатывать с пользователя или нет.  
- подбираем инструмент (t-тест, U-тест Mann-Whitney или бутстрап)  
- считаем p-value тремя способами: t-тест, U-тест, бутстрап средних.  
- сравниваем результат между тестом и контролем по всем этим кейсам.  
- делаем выводы о наличии/отсутствии значимых различий, на основе анализа примененных критериев.

## Данные

  value - значение  
  experimentVariant - группа данных

## Используемые библиотеки

*pandas, numpy, scipy, pingouin, statsmodels, random, matplotlib, seaborn* 
