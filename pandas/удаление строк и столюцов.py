import pandas as pd
import numpy as np


# df = pd.DataFrame({
#     'col_1': [10, 20, np.nan, 40],
#     'col_2': [50, 60, 70, np.nan],
#     'col_3': [90, 100, 110, 120]},
#     index=['row_1', 'row_2', 'row_3', 'row_4']
# )
# print(df)

#Метод drop()
# Метод Drop() имеет следующие аргумены:
# Labels: Имена строк или столбцов для удаления. Принимает одиночное значение или список.
# axis: Направление удаления. 0 (или 'index') для строк, 1 (или 'columns') для столбцов.
# index: Прямое указание меток строк для удаления.
# columns:  Прямое указание меток столбцов для удаления.
# inplace: True меняет исходный DataFrame, False (по умолчанию) возвращает копию.


# df.drop(['row_4', 'row_1'], inplace=True) #labels необязательно писать
# print(df)

# df.drop(columns=['col_1'], inplace=True)
# print(df)
# df.drop(index=['row_4'], inplace=True)
# print(df)

#colums - список столбцов, а index - список строк
# index_for_del = df[df['col_1'] < 20].index
# df.drop(index=index_for_del, inplace=True)
# print(df)

#Метод astype()

# category_list = ['a', 'b', 'c', 'd', 'e']
# df = pd.DataFrame({
#     'col_1': [i for i in range(1000)],
#     'col_2': [float(i) for i in range(1000)],
#     'col_3': [category_list[i%5] for i in range(1000)]},
#     index=[f'c_{i}' for i in range(1000)]
# )
# # print(df.dtypes)
# # print(df.memory_usage())
# new_df = df.astype({'col_1':np.int16, 'col_2':np.float16}) #вместо 16к байт, всего 4к байт в сумме с 2 столбцов
# new_df = new_df.astype({'col_3':'category'}) #1040 байт вместо 8к
# print(new_df.memory_usage())
# print(new_df)


#Практика

# df = pd.DataFrame({
#     "name": ["Alex", "Bob", "Charlie", "David", "Emma", "Frank"],
#     "age": ["20", "19", "21", "18", "22", "20"],
#     "height": ["175", "182", "169", "180", "171", "178"],
#     "city": ["Moscow", "SPB", "Kazan", "SPB", "Moscow", "Sochi"],
#     "salary": [70000, 65000, 80000, 60000, 90000, 75000],
#     "student": ["True", "False", "True", "True", "False", "False"]
# })

# df.drop(columns='city', inplace=True)
# df.drop(index=[1, 4], inplace=True)
# df.drop(columns=['height', 'student'], inplace=True)
# df.drop(index=[0], columns=['student'], inplace=True)
# df.drop(columns='name', inplace=True)



# df = df.astype({'age': np.int8, 'height': np.float16, 'salary': np.float16, 'student': np.bool})
# print(df.dtypes)

# print(df)
# df.drop(columns='city', inplace=True)
# df = df.astype({'age': np.float64, 'height': np.float64, 'salary': np.float64})
# index_of_David = df[df['name'] == 'David'].index
# df.drop(index=index_of_David, inplace=True)

# df2 = df.drop(columns='student')
# df2.drop(columns=['height', 'city'], inplace=True)
# df2 = df2.astype({'age': np.int32, 'salary': np.float32})
# print(df2.dtypes)

dirty = pd.DataFrame({
    "name": ["Alex", "Bob", "Emma", "Kate"],
    "age": ["20", "21", "19", "22"],
    "weight": ["80.5", "90.2", "55.0", "61.8"],
    "active": ["True", "False", "True", "False"],
    "temp": [1, 2, 3, 4]
})

dirty.drop(columns='temp', inplace=True)
dirty = dirty.astype({'age': np.int64, 'weight': np.float64, 'active': np.bool})
print(dirty, end='\n'*2)
print(dirty.dtypes)



