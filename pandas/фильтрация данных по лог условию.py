import pandas as pd


data_dict = {'age':[30, 12, 44, 19, 25],
             'name':['Vova', 'Petya', 'Masha', 'Kolya', 'Misha'],
             'has_car':[True, False, False, True, True]}

df_data = pd.DataFrame(data_dict, index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])
# print(df_data)

#получаем данные о первой и третьей строки, длина массива = кол-ву строк
# print(df_data[[True, False, True, False, False]])
# print(df_data[df_data['has_car']]) #выводятся строчки, где has_car = True

#Фильтрация по логическому условию

# print(df_data[df_data['age'] > 30])
# #то есть, внутри первых скобок само логическое выражение!

#В сложных логических операциях нельзя использовать and, or, not
#Вместо их ~(not), &(and), |(or)


# print(df_data[(df_data['age'] < 50) & ~(df_data['has_car'])])
#Меньше 50 лет и нет машины
#Высший приоритет у битовых операций, а только после них идут операции сравнения


# #ISIN()
# print(df_data.isin([30, 'Misha'])) #возвращает df с True, если нашел такие значения
# print(df_data['age'].isin([30, 44])) #возвращает серию с True или False
# print(df_data[(df_data['name'].isin(['Misha']) & df_data['has_car'])]) #Отфильтровали по имени Misha и наличию машины


#QUERY()
#Логические операции используются стандартно(можно юзать and, or, not)
#Используются только заванию столбцов
#В обратные кавычки заключаем кирилицу

# print(df_data.query('age < 40 and not has_car')) #фильтруем по возрасту и наличию машины

#Также можем использовать переменные в запросе
# N = 10
# print(df_data.query('has_car and age < 4*@N')) #Есть машина и меньше 40 лет
# #Перед переменной необходимо ставить @!
