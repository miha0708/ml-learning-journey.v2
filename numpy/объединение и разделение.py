import numpy as np


#ОБЪЕДИНЕНИЕ

# a = np.array( [(1, 2), (3, 4)] )
# b = np.array( [(5, 6), (7, 8)] )

# c = np.hstack([a, b])
# d = np.vstack( [a, b] )

# print(c)
# #матрица 2x4 (1 2 5 6),
# #            (3 4 7 8)
# #склейка как бы по высоте сначала первый столбец, потом второй
# print(d)
# #матрицы 4х2 (1 2) (3 4) (5 6) (7 8)
# #можно и так np.hstack( [b, a, a, b, b, a] )
# #при объединении размерности должны совпадать


# a = np.fromiter(np.arange(18), dtype='int16').reshape(3, 3, 2)
# b = np.arange(18, 36).reshape(3, 3, 2)
# #можно и так и так создавать

# print(np.hstack([a, b]).shape) #(3, 6, 2)
# print(np.vstack([a, b]).shape) #(6, 3, 2)
#hstack объежиняет по axis1, а vstack по axis0


# a = np.arange(0, 5, 1.0)
# b = np.arange(5, 10, 1.0)
# print(a, b)
# print(np.hstack([a, b]))
# print(np.vstack([a, b]))

# print(np.column_stack([a, b]))
# # (0 5) (1 6) (2 7) (3 8) (4 9), вместо (1 2 3 4 5 6 7 8 9) или (0 1 2 3 4) (5 6 7 8 9)



# a = np.arange(12).reshape(3, 2, 2)
# b = np.arange(12, 24).reshape(3, 2, 2)

# c0 = np.concatenate([a, b], axis=0) #(6, 2, 2)
# c1 = np.concatenate([a, b], axis=1) #(3, 4, 2)
# c2 = np.concatenate([a, b], axis=2) #(3, 2, 4)
# print(c0, c1, c2)


# #r - делает объединение по axis0
# print(np.r_[1:9, 90, 100]) #[1 2 3 4 5 6 7 8 90 100]
# print(np.r_[np.arange(3), np.arange(3, 10)]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(np.hstack([[0, 1, 2, 3], [4, 5, 6, 7, 8, 9]])) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#c - делает объединение по axis1
# print(np.c_[[1, 2, 3], [4, 5, 6]]) #(1 4) (2 5) (3 6)


#РАЗДЕЛЕНИЕ

# a = np.arange(10)
# # print(np.hsplit(a, 2)) #(0 1 2 3 4) (5 6 7 8 9)
# # a = np.reshape(a, (10, -1))
# # print(np.vsplit(a, 2)) #в столбец от 0 до 4 и от 5 до 9
# a = np.reshape(a, (2, 5))
# print(np.hsplit(a, 5)) #(0 5), (1 6)...


#чтобы по произвольной оси
# a = np.arange(12).reshape(3, 2, 2)
# print(np.array_split(a, 2, axis=2))