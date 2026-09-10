import pandas as pd
import numpy as np
from time import time

dct = {f'col_{i}': [i, i*2, i*3] if i != 3 else [i, i, i] for i in range(5)}
df = pd.DataFrame(dct)
# print(df)

# print(df.apply(np.max))

# def my_func(series):
#     return series + 100 if series.name != 'col_2' else series * 0

# print(df.apply(my_func, axis=0))
#df.apply(функция), метод apply делает фукнкция(df), только можно применять любые функции
#apply итерирует по оси каждый элемент, поэтому надо прописать инстуркцию для элемента и apply все применит для всех


# def func_of_str(row, idx):
#         return row + (idx+1)*100

# new_df = df.apply(lambda x: func_of_str(x, x.name), axis=1)
# print(new_df)
# print(new_df.apply(np.mean, axis=1))

#аргумент raw=True, говорит будет передаваться массив массив numpy, по умолчанию стоит raw=False(передается серия)
#массив numpy намного быстрее


# dict_data = {f'col_{i}': range(100) for i in range(10000)}
# df = pd.DataFrame(dict_data)

# #Передается серия
# start = time()
# df.apply(np.mean)
# end = time()
# print(round(end-start, 3)) #0.185

# #Передается масив numpy
# start = time()
# df.apply(np.mean, raw=True)
# end = time()
# print(round(end - start, 3)) #0.038

# print(185/3.8) #61.6!!!!!! в 61 раз быстрее raw=True
#но не всегда raw=True поддерживает методы pandas


#Apply для Series
#нет аргументов axis, raw

# dict_array = {'age': [53, 25],
#               'name': ['Misha Makarov', 'Dasha'],
#               'has_car': [True, True]}

# df = pd.DataFrame(dict_array)
# # print(df['name'])
# def get_last_name(name):
#     split_name = name.split()
#     return split_name[-1] if len(split_name) == 2 else np.nan

# print(df['name'].apply(get_last_name)) #получили нужную серию
# # 0    Makarov
# # 1        NaN
# # Name: name, dtype: str

# df['last_name'] = df['name'].apply(get_last_name)
# print(df)


#Практика

import pandas as pd

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Charlie", "David", "Emma", "Frank"],
    "age": [17, 22, 19, 16, 25, 20],
    "math": [78, 92, 65, 81, 99, 56],
    "city": ["yaroslavl", "moscow", "kazan", "sochi", "moscow", "yaroslavl"]
})

# print(df)
df['name'] = df['name'].apply(lambda x: x.upper())
# print(df)
df['adult'] = df['age'].apply(lambda x: x >= 18)
# print(df)
df['city'] = df['city'].apply(lambda x: x.capitalize())
# print(df)

def grade(ball):
    if ball >= 90:
        return 'A'
    elif 75 <= ball < 90:
        return 'B'
    else:
        return 'C'

df['grade'] = df['math'].apply(grade)
# print(df)

def profile(row):
    return f'{row['name'].capitalize()} ({row['age']}) - {row['city']}'

df['profile'] = df.apply(profile, axis=1)
print(df)