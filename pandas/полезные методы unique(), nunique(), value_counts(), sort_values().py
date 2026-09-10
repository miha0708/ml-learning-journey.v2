import pandas as pd
import numpy as np

data_dict = {'age': [30, 30, 10, 17, 25],
             'name': ['Vova', 'Vova', 'Masha', 'Kolya', 'Misha'],
             'has_car': [True, True, False, True, True]}

df = pd.DataFrame(data_dict)
# print(df)

#Метод unique()
#применяется только к сериям и индексам
#возвращает массив с уникальными значениями
# print(df['age'].unique()) #возвращает массив с уникальными значениями [30. 20. nan 25]


#Метод nunique()
#применяется ко всему
#возвращает кол-во уникальныз значений
# print(df['age'].nunique()) #nan не учитывается [30. 20. nan 25.], но выведет метод именно 3
# print(df.nunique())
# age        3
# name       5
# has_car    2
# dtype: int64


#Метод value_counts()
#возвращает серию с мультииндексом
#показывает сколько раз данная строка была использова в df
# print(df.value_counts()) #если есть np.nan в строке, то здесь это отображаться не будет!
# age  name   has_car
# 30   Vova   True       2
# 10   Masha  False      1
# 17   Kolya  True       1
# 25   Misha  True       1
# Name: count, dtype: int64

# print(df.value_counts(['age'])) #можно применять и к серии и к df
# age
# 30    2
# 10    1
# 17    1
# 25    1
# Name: count, dtype: int64

# print(df.value_counts(['age', 'has_car'], dropna=False)) #повтор только по этим двум колонкам, если надо подсчитать с пропусками, то dropna=False!
# age  has_car
# 30   True       2
# 10   False      1
# 17   True       1
# 25   True       1
# Name: count, dtype: int64


# print(df.value_counts('age', normalize=True, dropna=False, ascending=False))
# age
# 30    0.4
# 10    0.2
# 17    0.2
# 25    0.2
# Name: proportion, dtype: float64

#ascending отвечает за порядок сортировки, если True, то по возрастанию, если False, то по убыванию


#Метод sort_values()
#сортировка данных по указанному столбцу
print(df.sort_values(by=['age', 'name'], ascending=True)) #сортировка по двум стобцам и по возрастанию
#    age   name  has_car
# 2   10  Masha    False
# 3   17  Kolya     True
# 4   25  Misha     True
# 0   30   Vova     True
# 1   30   Vova     True
#по умолчанию NaN внизу, пожтому na_position='first' ставит на первое место!