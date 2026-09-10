import pandas as pd
import numpy as np


df1 = pd.DataFrame({
    'col_1': [10, np.nan, 30],
    'col_2': [40, 50, 60]},
    index=['row_1', 'row_2', 'row_3']
)

df2 = pd.DataFrame({
    'col_1': [1, 2, np.nan],
    'col_2': [40, 50, 60],
    'col_3': [90, 900, 9000]},
    index=['row_1', 'row_2', 'row_3']
)

series1 = pd.Series([np.nan, 0, 33], index=['row_1', 'row_2', 'row_30'])

# print(df1, end='\n'*2)
# print(df2, end='\n'*2)
# print(series1)

# print(np.nan == np.nan) #False, также при сравнении nan с любым числом
# print(series1 == 5) #[False, False, False], возвращается серия с булевыми значениями
# print(series1 > [1, 2, 3]) #кол-во элементов должны совпадать, возвращается булевая серия [False, False, True]
# print(series1 == series1) #[False, True, True]
# print(series1 > df1['col_2']) #[False, False, False], для сравнения должны быть одинаковые индексы
# print(df2['col_2'] <= df1['col_1']) #[True, False, True], False из-за np.nan


#Сравнения DataFrame

# print(df1 == 6) #просто каждый элемент сравнивается с числом
# print(df1 >= [10, 20]) #кол-во элементов в списке должно равнятся кол-ву столбцов
# print(df1 >= df2) #должны совпадать индексы строк и столбцов, иначе будет ошибка


#Специальные методы для сравнения


# eq() - ==
# ne() - !=
# le() - =>
# lt() - >
# ge() - >=
# gt() - >

#Все методы работают одинаково!

# print(series1.le(df1['col_2'])) #происходит выравнивание индексов, а затем сравнение, индексы которых нет в обоих элементах приравниваются к False
# print(df1 > df2) #ошибка, так как разные индексы(2 стобца и 3 стобца)
# print(df1.gt(df2)) #col_3 вся false, так как она только в одном есть, все выровнялось и сравнилось
# print(df1.gt([1, 2, 3], axis=0)) #кол-во элементов списка должно сопадать с кол-вом строк
# print(df1.gt([1, 2], axis=1)) #кол-во элементов списка должно сопадать с кол-вом столбцов, по умолчанию axis=1


#Метод equals()

#при использовании этого метода значения NaN будут считаться равными
#индексы строк и столбцов должны быть одинаковыми и в одинаковом порядке
# print(df1.equals(df2)) #False
# print(df1['col_2'].equals(df2['col_2'])) #True, но series != dataframe
# print(series1.equals(series1)) #True, серии равны, даже если есть np.nan
# print(df1.equals(df1)) ##True, датафреймы равны, даже если есть np.nan
