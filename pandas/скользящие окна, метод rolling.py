import pandas as pd
import numpy as np


df = pd.DataFrame({'col_1': [1, 2, 3, 4, 5],
                   'col_2': [10, 20, 30, 40, 50]})

#Метод rolling()

# print(df.rolling(3)) #первый аргумент это ширина окна(сколько строк)
# Rolling [window=3,center=False,method=single]

# for window in df.rolling(3):
#     print(window, end='\n'*2)
#    col_1  col_2
# 0      1     10

#    col_1  col_2
# 0      1     10
# 1      2     20

#    col_1  col_2
# 0      1     10
# 1      2     20
# 2      3     30

#    col_1  col_2
# 1      2     20
# 2      3     30
# 3      4     40

#    col_1  col_2
# 2      3     30
# 3      4     40
# 4      5     50

# print(df.rolling(3).sum())
#    col_1  col_2
# 0    NaN    NaN
# 1    NaN    NaN
# 2    6.0   60.0
# 3    9.0   90.0
# 4   12.0  120.0

# print(df.rolling(3).mean())
#    col_1  col_2
# 0    NaN    NaN
# 1    NaN    NaN
# 2    2.0   20.0
# 3    3.0   30.0
# 4    4.0   40.0

# print(df.rolling(3, min_periods=1).mean()) #минимальная ширина окна=1, т.е берутся все элементы, а не группы по 3
#    col_1  col_2
# 0    1.0   10.0
# 1    1.5   15.0
# 2    2.0   20.0
# 3    3.0   30.0
# 4    4.0   40.0

# print(df.rolling(3, min_periods=1, step=2).mean()) #шаг=2
#    col_1  col_2
# 0    1.0   10.0
# 2    2.0   20.0
# 4    4.0   40.0

# print(df.rolling(2, min_periods=1, step=1).agg({'col_1': np.sum, 'col_2': np.mean}))
#    col_1  col_2
# 0    1.0   10.0
# 1    3.0   15.0
# 2    5.0   25.0
# 3    7.0   35.0
# 4    9.0   45.0


#Пример использования

df_sales = pd.DataFrame({'sales': np.random.randint(0, 100, 100)},
                        index=pd.date_range('2026', periods=100))

# print(df_sales)
#             sales
# 2026-01-01     62
# 2026-01-02     87
# 2026-01-03     55
# 2026-01-04      4
# 2026-01-05     97
# ...           ...
# 2026-04-06     25
# 2026-04-07     49
# 2026-04-08     84
# 2026-04-09     58
# 2026-04-10     14

# df_sales = df_sales.rolling(7, min_periods=1).agg({'sales': [np.sum, np.mean, np.min, np.max]})
# print(df_sales)


#Практика
import pandas as pd

df = pd.DataFrame({
    "sales": [10, 15, 20, 30, 25, 40, 35]
})

# df['mean_3'] = df.rolling(3).mean()
# print(df)

# print(df.rolling(4).agg({'sales': ['mean', 'max', 'min']}))

# df = pd.DataFrame({
#     "temp": [18, 20, 22, 19, 21]
# })

# df['avg'] = round(df.rolling(3, min_periods=1).mean(), 1)
# print(df)

df = pd.DataFrame({
    "math": [70, 80, 60, 90, 100],
    "physics": [75, 85, 65, 88, 95]
})

# print(df.rolling(2).agg({'math': 'mean', 'physics': 'mean'}))

df = pd.DataFrame({
    "sales": [100, 120, 90, 150, 170, 130, 160]
})

df['mean_3'] = df.rolling(3).mean()
df['trend'] = df['sales'] - df['mean_3']
df.drop(columns=['mean_3'], inplace=True)
print(df)