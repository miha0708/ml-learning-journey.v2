import pandas as pd
import numpy as np

data_dict = {'age': [30, np.nan, 44, 19, 25],
             'name': ['Vova', 'Petya', 'Masha', 'Kolya', 'Misha'],
             'has_car': [True, False, np.nan, True, True],
             'brend': [np.nan, np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(data_dict)
# print(df)

#метод dropna() удаляет строки с пропусками

df.dropna(subset=['age', 'name', 'has_car'], inplace=True, axis=0)
# print(df)

#чтобы удалить стобцы с пропусками надо менять axis = 1
# print(df.dropna(axis=1))

#аргумент how='any'(по умолч) если хотя бы 1 пропуск, то удаляем
#можно менять на how='all', тогда только если все пропуски
# print(df.dropna(axis=1, how='all'))
# print(df.dropna(subset=[0], axis=1)) #удалился столбец, где в 0 строке были пропуски в этих стобцах

# data_dict = {
#     'age': [30, np.nan, 44, 19, 25],
#     'name': ['Vova', 'Petya', 'Masha', 'Kolya', 'Misha'],
#     'has_car': [True, False, np.nan, True, True],
#     'brend': [np.nan, np.nan, 'Toyota', np.nan, np.nan]
# }
# df = pd.DataFrame(data_dict)


# df.dropna(subset=['age', 'name'], inplace=True)
# print(df)
# df.dropna(subset=['brend'], inplace=True)
# print(df)

#Примеры dropna()
# df = pd.DataFrame({
#     "name": ["Alex", "Bob", None, "David", "Emma"],
#     "age": [20, None, 25, None, 30],
#     "city": ["Moscow", "London", None, "Berlin", "Paris"]
# })

# # df.dropna(inplace=True)
# # df.dropna(subset='age', inplace=True)
# df.dropna(subset=['name', 'city'], thresh=1, inplace=True)
# print(df)


# df = pd.DataFrame({
#     "name": ["Alex", "Bob", "Charlie", "David", "Emma", "Frank", "Grace"],
#     "age": [20, None, 25, None, 30, 35, None],
#     "salary": [1000, 2000, None, 3000, None, 4000, 5000],
#     "city": ["Moscow", "London", None, "Berlin", "Paris", None, "Rome"],
#     "email": ["a@mail.com", None, "c@mail.com", "d@mail.com", None, "f@mail.com", "g@mail.com"],
#     "phone": ["111", "222", None, None, "555", None, "777"]
# })


# df.dropna(subset=['name', 'age'], inplace=True)
# df.dropna(subset=['age', 'salary', 'city', 'phone'], thresh=3, axis=0, inplace=True)
# print(df)


#Метод fillna()

data_dict = {'age': [30, np.nan, 44, 19, 25],
             'name': ['Vova', 'Petya', 'Masha', 'Kolya', 'Misha'],
             'has_car': [True, False, np.nan, True, True],
             'brend': [np.nan, np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(data_dict)

# df.fillna(0, inplace=True) #Меняем NaN на любое значение
# print(df.fillna(value={
#     'age':100,
#     'has_car': 'no car',
#     'brend': 0
# })) #можно менять значения на какие хочешь для каждого столбца


#Метод isna()

data_dict = {'age': [30, np.nan, 44, 19, 25],
             'name': ['Vova', 'Petya', 'Masha', 'Kolya', 'Misha'],
             'has_car': [True, False, np.nan, True, True],
             'brend': [np.nan, np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(data_dict)

# print(df.isna()) #вернет df с True и False
# print(df['age'].isna()) #вернет серию 
# print(df[~df['age'].isna()]) #вернет df, где age != NaN


#Метод notna()

data_dict = {'age': [30, np.nan, 44, 19, 25],
             'name': ['Vova', 'Petya', 'Masha', 'Kolya', 'Misha'],
             'has_car': [True, False, np.nan, True, True],
             'brend': [np.nan, np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(data_dict)

# print(df.notna()) #просто обратный метод методы isna()
print(df[df['age'].notna()])