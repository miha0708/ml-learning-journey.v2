import pandas as pd
import numpy as np


# series_from_list = pd.Series(
#     [100, 104, 115, 135],
#     index=['row_1', 'row_2', 'row_3', 'row_4'],
#     dtype=int,
#     name='test'
# )

# print(series_from_list)


# def create_series_from_dict(data_dict, index_list):
#     return pd.Series(
#         data_dict,
#         index=index_list,
#         name='test_dict'
#     )


# dict_array = {
#     'row_1': 1,
#     'row_2': 2,
#     'row_3': 3
# }

# selected_index = ['row_2']
# series_from_dict = create_series_from_dict(dict_array, selected_index)
# print(series_from_dict)

#если передаем список, то мы определяем названия и кол-во элементов должны совпадать
#если передаем словарь, то мы делаем выборку, можно сколько необходимо выбирать


# np_a = np.array([1, 2, 4, 4, 0])
# series_from_np = pd.Series(
#     np_a,
#     copy=False
# )

# series_from_np.iloc[3] = 111 #4 строчка, так как с нуля отсчет меняется, вместе с этим меняяется и массив numpy(copy=false)
# print(series_from_np)
# print(np_a)




# series_from_list = pd.Series(
#     [1, 2, 3, 4, 5],
#     index=['0', '1', '2', '3', '4'],
#     name='series_from_list'
# )

# series_from_series = pd.Series(
#     series_from_list,
#     index=['2', '3'],
#     name='series_from_series'
# )
# print(series_from_series)
# #создаем серию из серии путем выборки определенных значений из импортируемой серии



# dict_array = {
#     'col_1': [4, 5, 21, 1, 4, 0], #одинаковоые размеры
#     'col_2': [4, 1106, 21, 1, 4, 0],
#     'col_3': [4, 999, 21, 1, 4, 0],
# }

# df = pd.DataFrame(
#     dict_array,
#     index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6'], #назавание строк
#     columns=['col_1', 'col_3'], #выборка столбцов
#     dtype=float
# )

# print(df)


# np_array = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])

# df = pd.DataFrame(np_array, 
#                   copy=False, 
#                   columns=['col_1', 'col_2', 'col_3', 'col_4'],
#                   index=['row_1', 'row_2', 'row_3'])

# df.iloc[1:2, -1] = 1111 #вторая строка и послежний столбец
# print(df)
# print(np_array) #также поменялось, так как copy=false



