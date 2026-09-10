import pandas as pd
import numpy as np


# list_index = list('obeme')
# # print(list_index)

# index_data = pd.Index(
#     list_index,
#     name='rows'
# )
# # print(index_data) Index(['o', 'b', 'e', 'm', 'e'], dtype='str', name='rows')

# column_data = pd.Index(['col_1', 'col_2', 'col_3'], name='cols')

# df_data = pd.DataFrame({
#     'col_1':[1, 2, 3, 4, 5],
#     'col_2':[6, 7, 8, 9, 10],
#     'col_3':[11, 12, 13, 14, 15]},
#     index=index_data,
#     columns=column_data)

# print(df_data)



#свойства и методы индексов

# df = pd.DataFrame( {f'c_{i}':np.arange(1001)*i for i in range(101)} ) #столбец:значение
# # print(df)
# index = df.index
# columns = df.columns
# print(index) #RangeIndex(start=0, stop=1001, step=1)
# print()
# print(columns)

#индексы в списки

# print(index.to_list()) #0-1000 список
# print(columns.to_list()) #c_0-c_100 список

# print(index.to_numpy()) #в массив numpy
# print(columns.to_numpy()) #в массив numpy




# list_index = list('obeme')
# # print(list_index)

# index_data = pd.Index(
#     list_index,
#     name='rows'
# )
# # print(index_data) Index(['o', 'b', 'e', 'm', 'e'], dtype='str', name='rows')

# column_data = pd.Index(['col_1', 'col_2', 'col_3'], name='cols')

# df_data = pd.DataFrame({
#     'col_1':[1, 2, 3, 4, 5],
#     'col_2':[6, 7, 8, 9, 10],
#     'col_3':[11, 12, 13, 14, 15]},
#     index=index_data,
#     columns=column_data)

# print(df_data)

# index_data = df_data.index
# column_data = df_data.columns

# print(index_data.unique()) #Index(['o', 'b', 'e', 'm'], dtype='str', name='rows') уникальные значения
# print(column_data.unique()) #Index(['col_1', 'col_2', 'col_3'], dtype='str', name='cols')


# print(index_data.nunique()) #количество уникальных значений
# print(index_data.is_unique) #False, так как было повторение
# print(column_data.is_unique) #True, так как все значения уникальные

# print(index_data.duplicated()) #[False, False, False, False, True], если False то это первое вхождение, иначе True

# print(index_data.name) #заголовок всех строк
# print(column_data.name) #заголовок всех столбцов


#переименование индексов
# index_data.name = 'row_new'
# column_data.name = 'col_new'
# print(df_data)


#переименование rename()

# new_df_data = df_data.rename(columns={
#     'col_1': 'col_11',
#     'col_2': 'col_22',
#     'col_3': 'col_33'
# }) #метод по умолчанию не меняет, надо присваивать либо сразу выводить его
# #либо можно указать с помощью осей

# # new_df_data = df_data.rename({
# #     'col_1': 'col_11',
# #     'col_2': 'col_22',
# #     'col_3': 'col_33'}, axis=1) #axis1 - столбцы, axis0 - строки


# #также можно использовать питон функции для названией
# new_df_data = new_df_data.rename(
#     str.upper,
#     axis=0,
#     inplace=True #чтобы были сразу применены изменения, без присваивания
# )
# print(new_df_data)


# index = pd.Index([0, np.nan, 2, np.nan])
# df_nan = pd.DataFrame(np.arange(8).reshape(4, 2),
#                       columns=['col_1', 'col_2'],
#                       index=index)
# print(df_nan)

# #проверка на пропуски в индексах
# print(df_nan.index.hasnans) #True - есть
# print(df_nan.index.isna()) #[False, True, False, True], где True, там NaN
# print(df_nan.index.dropna()) #не меняет df, но показывает только нормальные значения



#Урок 2(доступ к данным)!!!

# df = pd.DataFrame({'col_1':[6, 3, 2, 9],
#                    'col_2':[7, -22, 0, 4],
#                    'col_3':[111, -76, 8, 1]},
#                    dtype=float)


# # df = df.set_index('col_1') #установка столбца col_1 в качестве индекса
# df.set_index(['col_1', 'col_3'], append=False, inplace=True) #мульти индекс, col_1 и col_3 - индексы и стоят в самом начале
# #старый индекс был заменен, чтобы оставить старый нужно изменить параметр append на True
# #если inplace=True, то тогда изменения вступают сразу, без присваивания, по умолчанию inplace=False

# #чтобы сбросить индекс у столбца надо применить reset_index
# df.reset_index('col_3', inplace=True)
# #можно все сбросить
# df.reset_index(inplace=True)
# print(df)


# df = pd.DataFrame({'col_1':[1, 2, 3],
#                    'col 2':[4, 5, 6],
#                    'col_3':[7, 8, 9]})

# print(df['col_1']) #вернет серию, тк любой столбец dataframe - серия Name: col_1, dtype: int64
# print(df[['col_1']]) #вернется dataframe
# print(df[['col_1', 'col_3']]) #можно и так
# df['col_1'] = 1 #весь столбец равен единице
# df['NEW_COL'] = 3 #новый стобец со всеми элементами равными 3
# df['NEW_COL_1'] = df['col_1'] #еще один новый столбец равный col_1
# del df['NEW_COL_1'] #удаление столбца

# print(df[[True, False, True]]) #вернем только первую и 3 строчку, только там, где True
# df[[True, False, True]] = 1000 #можно изменять все значения в этих строчках
# df.loc[[0], ['col_1']] = 10000 #изменяем только первую строчку первого столбца 

# print(df.col_1) #можно вызывать столбец отдельно
# print(df['col_1']) #можно и так
# print(df[['col_1']]) #и так



#Урок 3(мультииндексы)!!!



# Создание мультииндекса с помощью массивов(1 способ) from_arrays
# arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]
# index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])

# df_rows = pd.DataFrame(
#     [[0, 1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11],
#     [12, 13, 14, 15]],
#     index=index,
#     columns=['c_0', 'c_1', 'c_2', 'c_3']
# )
# print(df_rows)

# df_columns = pd.DataFrame(
#     [[0, 1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11],
#     [12, 13, 14, 15]],
#     columns=index,
#     index=['r_1', 'r_2', 'r_3', 'r_4']
# )
# print('\n')
# print(df_columns)


#from_product(2 способ)

# level_0 = ['A', 'B']
# level_1 = [1, 2, 3]

# multiproduct = pd.MultiIndex.from_product([level_0, level_1], names=['level_0', 'level_1'])
# df_data_product = pd.DataFrame({
#     'col_1':[1, 1, 1, 1, 1, 1],
#     'col_2':[2, 2, 2, 2, 2, 2],
#     'col_3':[3, 3, 3, 3, 3, 3],
#     'col_4':[4, 4, 4, 4, 4, 4],
#     'col_5':[5, 5, 5, 5, 5, 5],
#     'col_6':[6, 6, 6, 6, 6, 6]},
#     index=multiproduct
# )
# print(df_data_product)


#from_tuples(3 способ)


tuples = [(1, 'row_1'), (1, 'row_2'), (2, 'row_1'), (2, 'row_2')]
multiindex = pd.MultiIndex.from_tuples(tuples, names=['level_0', 'level_1'])

df_data_tuples = pd.DataFrame({
    'col_1':[1, 2, 1, 2],
    'col_2':[1, 2, 1, 2]},
    index=multiindex
)
# print(df_data_tuples)

#Свойства!

#получение мультииндекса
# print(df_data_tuples.index)
# print(df_data_tuples.columns)

#число уровней мультииндекса
# print(df_data_tuples.index.nlevels) #2

# #кортеж с длиной каждого уровня
# print(df_data_tuples.index.levshape) #(2, 2)

# #имена уровней
# print(df_data_tuples.index.names) #['level_0', 'level_1']
#также можно менять название уровней индекса
# df_data_tuples.index.names = ['new_level_0', 'new_level_1']

# #есть также специальный метод для изменения имена индексов set_names
# df_data_tuples.index.set_names(['level_0', 'level_1'], inplace=True)
# print(df_data_tuples)

# #можно поменять название конкретного уровня
# df_data_tuples.index.set_names('new_level_0', level=0, inplace=True)
# print(df_data_tuples)

#элементы содержащиеся в мультииндексе

# print(df_data_tuples.index.levels) #[[1, 2], ['row_1', 'row_2']]
# print(df_data_tuples.index) #чуть более подробно


#сброс уровней мультииндекс reset_index

# new_df = df_data_tuples.reset_index() #старая df не меняется(только если inplace=True, тогда меняется)!
# print(new_df)

# #также можно сбрасывать определенный уровень
# df_data_tuples.reset_index(['level_1'], inplace=True)
# print(df_data_tuples)


#удаление уровней с помощью метода droplevel

# new_index = df_data_tuples.index.droplevel() #по умолчанию удаляет индекс с 0 уровнем
# print(new_index) #Index(['row_1', 'row_2', 'row_1', 'row_2'], dtype='str', name='level_1') пропали 1 и 2

# new_index = df_data_tuples.index.droplevel(level=1) #удаляем индекс с указанным уровнем
# print(new_index) #Index([1, 1, 2, 2], dtype='int64', name='level_0')

# new_index = df_data_tuples.index.droplevel(['level_1']) #удаляем список уровней 1+, только все нельзя удалять, иначе - ошибка
# print(new_index) #Index([1, 1, 2, 2], dtype='int64', name='level_0')
