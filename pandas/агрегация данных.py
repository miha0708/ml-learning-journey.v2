import pandas as pd
import numpy as np


df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [np.nan, np.nan, np.nan]],
                   columns=[f'col_{i}' for i in range(1, 4)])

print(df)

# Функции агрегации:
# min()
# max()
# mean()
# sum()
# std()
# count()


# print(df.min()) #аналогично max, mean, sum(NaN не учитывается)
#col_1    1.0
# col_2    2.0
# col_3    3.0

# print(df['col_1'].mean()) #2.5
# print(df.std(ddof=1)) #стандартное отклонение(по умолчанию ddof=1, чтобы чисто математически ddof=0)
# print(df['col_2'].count()) #2, так как 3 это NaN, считает кол-во непустых элементов
# print(df.count()) #вернет серию с данными по каждому столбцу
# col_1    2
# col_2    2
# col_3    2
# dtype: int64


#Метод agg()

#позволяет применять несколько функций одновременно и указывать оси применения

# print(df.agg(['mean', 'sum']))
#       col_1  col_2  col_3
# mean    2.5    3.5    4.5
# sum     5.0    7.0    9.0

#также можно передавать свои функции
# def my_func(series):
#     return series.min() + 1000

# print(df.agg(my_func))
# print(df.agg(lambda x: x > 0))

#агрегация для каждого столбца отдельно
# print(df.agg({'col_1': 'mean', 'col_2': np.min, 'col_3': 'std'}))

# #именованная агрегация
# print(df.agg(min_col_1=('col_1', 'min'), max_col_2=('col_2', 'max'), mean_col_3 = ('col_3', np.mean)))
#             col_1  col_2  col_3
# min_col_1     1.0    NaN    NaN
# max_col_2     NaN    5.0    NaN
# mean_col_3    NaN    NaN    4.5


#Практика
import pandas as pd

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Charlie", "David", "Emma", "Frank"],
    "age": [20, 19, 21, 18, 22, 20],
    "score": [88, 74, 95, 67, 91, 82]
})

# print(df['age'].agg('min'))
# print(df['age'].agg('max'))
# print(df['age'].agg('mean'))
# print(df['score'].agg('sum'))
# print(df['score'].agg(['min', 'max', 'mean']))

# print(df['age'].agg(['min', 'max', 'mean']))
# print(df['score'].agg(['sum', 'mean', 'median']))

df = pd.DataFrame({
    "salary": [50000, 70000, 60000, 90000, 120000]
})

# print(df.agg(lambda x: x.max() - x.min()))
# print(df.agg(lambda x: x.max() / x.min()))
# print(df.agg(lambda x: round(x.mean())))

df = pd.DataFrame({
    "height": [175, 182, 169, 180, 171, 177],
    "weight": [72, 83, 68, 80, 61, 74]
})

# df = df.agg({'height':['min', 'max', 'mean'], 'weight':['mean', 'sum']})
# print(df)


df = pd.DataFrame({
    "math": [90, 76, 88, 95, 67],
    "physics": [85, 80, 92, 91, 70],
    "informatics": [100, 82, 95, 98, 75]
})

# print(df.agg(lambda x: x.min()))
# print(df.agg(lambda x: x.max()))
# print(df.agg(lambda x: x.mean()))
# print(df.agg(lambda x: x.median()))

def minl(row):
    return min(row['math'], row['physics'], row['informatics'])

# df['min'] = df.apply(minl, axis=1)
# print(df)

df = df.agg({
    "math": ["min", "max", "mean", "median"],
    "physics": ["min", "max", "mean", "median"],
    "informatics": ["min", "max", "mean", "median"]
})
print(df)