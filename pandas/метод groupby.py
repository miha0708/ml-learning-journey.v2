import pandas as pd
import numpy as np


df = pd.DataFrame({
    'name': ['Petya', 'Vasya', 'Petya', 'Mark'],
    'city': ['Kaliningrad', 'Volgograd', 'Yaroslavl', np.nan],
    'age': [18, 33, 18, np.nan]}
)
# print(df)

#Метод groupby()

#метод используется для группировки данных
# print(df.groupby('name')) #<pandas.api.typing.DataFrameGroupBy object at 0x00000223325DEF90>
groups = df.groupby(['name']) #просто вывести нельзя, надо перебрать

# for name, group in groups:
#     print(f'Name of group - {name}', end='\n')
#     print(group, end='\n'*2)

# Name of group - Mark
#    name city  age
# 3  Mark  NaN  NaN

# Name of group - Petya
#     name         city   age
# 0  Petya  Kaliningrad  33.0
# 2  Petya    Yaroslavl  18.0

# Name of group - Vasya
#     name       city   age
# 1  Vasya  Volgograd  18.0


#Можно также и по нескольким параметрам
#NaN уже не учитывается
# groups = df.groupby(['name', 'age']) #просто вывести нельзя, надо перебрать

# for name, group in groups:
#     print(f'Name of group - {name}', end='\n')
#     print(group, end='\n'*2)

# Name of group - ('Petya', 18.0)
#     name         city   age
# 0  Petya  Kaliningrad  18.0
# 2  Petya    Yaroslavl  18.0

# Name of group - ('Vasya', 33.0)
#     name       city   age
# 1  Vasya  Volgograd  33.0

# print(df.groupby('name', dropna=False).sum()) #чтобы учитывался NaN
#                        city   age
# name                             
# Petya  KaliningradYaroslavl  36.0
# Vasya             Volgograd  33.0
# NaN                           0.0

#Чтобы столбец, по которому группируют не был индексом, нужно поставить as_index=False
# print(df.groupby('age', dropna=False, as_index=False).sum())
#     age        name                  city
# 0  18.0  PetyaPetya  KaliningradYaroslavl
# 1  33.0       Vasya             Volgograd
# 2   NaN        Mark                      

#чтобы функция агрегации не агрегировала все данные, мы сначала выберем, то, что будем агрегировать
# print(df.groupby('name', as_index=False)['age'].sum())
#     name   age
# 0   Mark   0.0
# 1  Petya  36.0
# 2  Vasya  33.0


#Практика

import pandas as pd

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Helen", "Ivan", "Jack"],
    "city": ["Moscow", "Moscow", "SPB", "SPB", "Kazan", "Kazan", "Moscow", "SPB", "Kazan", "Moscow"],
    "department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "HR", "Sales", "IT"],
    "age": [20, 25, 21, 28, 24, 30, 26, 22, 27, 23],
    "salary": [70000, 50000, 80000, 60000, 55000, 90000, 65000, 52000, 61000, 85000],
    "bonus": [5000, 2000, 7000, 3000, 2500, 8000, 3500, 2200, 2800, 7500]
})

# print(df['salary'].agg(np.mean))
# print(df.groupby('department')['name'].count())

# print(df.groupby('city')['salary'].agg(['mean', 'max', 'min']))
# print(df.groupby('department')['age'].mean())
# print(df.groupby('department')['salary'].mean())
# print(df.groupby('department')['bonus'].sum())

# groups = df.groupby(['city', 'department'])
# for name, group in groups:
#     print(name, group['name'].count())
#     print(name, group['salary'].mean())


# df['total_income'] = df['salary'] + df['bonus']
# print(df['total_income'].agg('mean'))
# print(df['total_income'].agg('max'))
# print(df['total_income'].agg('max') - df['total_income'].agg('min'))



# print(df.groupby('city')['salary'].agg(lambda x: x.sum() / x.count()))
# print(df.groupby("department").agg({
#     "age": "mean",
#     "salary": "mean",
#     "bonus": "sum"
# }))


#Шпора
# print(df.groupby("city")["salary"].mean())
# print(df.groupby("city").agg({"salary": "mean", "bonus": "sum"}))
# print(df.groupby(["city", "department"]).agg({"salary": "mean", 'bonus': np.mean}).reset_index())
# print(df.loc[df.groupby("city")["salary"].idxmax()])

