import numpy as np


# a = np.array([1, 2, 3, 4, 4, 3, 2, 1])

# setA = np.unique(a) #убираем дубликаты
# print(setA) #[1, 2, 3, 4], вместо [1, 2, 3, 4, 4, 3, 2, 1]
# #в numpy множества - одномерный массив с уникальными значениями
# print(np.unique(a, return_counts=True)) #показывает сколько раз каждый элемент повторялся
# print(np.unique(a, return_index=True)) #индексы первого вхождения элемента
# print(np.unique(a, return_inverse=True)) #индексы по которым можно возвратить массив
#(array([1, 2, 3, 4]), array([2, 2, 2, 2])) - counts
#(array([1, 2, 3, 4]), array([0, 1, 2, 3])) - index
#(array([1, 2, 3, 4]), array([0, 1, 2, 3, 3, 2, 1, 0])) - inverse

# setA, idx = np.unique(a, return_inverse=True)
# print(setA[idx]) #восстановили исходный массив a


# x = np.array([[1, 1, 2, 3], [7, 3, 1, 0], [1, 1, 2, 3]])
# print(np.unique(x)) #[0, 1, 2, 3, 7]
# print(np.unique(x, axis=0)) #исчет и удаляет одинаковые строчки


# x = np.array([1, 2, 3, 4, 5])
# y = np.array([-1, 0, 2, 5, 8, 19, 4])
# # # print(np.isin(x, y)) #[False  True False  True  True]
# # #если есть элемент из множества x в множестве y, то true иначе false
# print(np.intersect1d(x, y)) #пересечение [2 4 5]
# print(np.setdiff1d(x, y)) #элементы, которые есть в x, но нет в y [1 3], короче x - y в множествах
# print(np.union1d(x, y)) #объединение x и y
# print(np.setxor1d(x, y)) #элементы, которых нет в обоих одновременно [-1  0  1  3  8 19]

