import numpy as np

# a = np.arange(10)
# a = np.reshape(a, (2, 5))
# b = a.reshape(10)
# a[0][0] = 1000


# a = np.reshape(a, (a.size)) #из матрицы в обычный массив
# a = a.ravel() #или метод ravel делает то же самое
# print(a)


# a = np.array( [(1, 2, 3), (4, 5, 6), (7, 8, 9)] )
# print(a)
# b = a.T #транспанирование, когда наоборот столбцы и строки
# print()
# # print(b)


# x = np.arange(10)
# x = np.reshape(x, (-1, x.size))
# print(x.T) #только так можно применять транспанирование, нужно чтобы было больше 1 оси



# x_test = np.arange(32).reshape(8, 2, 2)
# print(x_test.shape) #8, 2, 2
# x_test4 = np.expand_dims(x_test, axis=0) #добавление еще одной оси, это просто новое предстваление, они друг от друга зависят
# # print(x_test4)
# print(x_test4.shape) #(1, 8, 2, 2)

# a = np.append(x_test4, x_test4, axis=0)
# # print(a) #просто в начала массива добавили еще один массив
# print(a.shape) #(2, 8, 2, 2)
# b = np.delete(a, 0, axis=0) #удаление элемента по индексу и оси
# print(b.shape) #(1, 8, 2, 2)
# b = np.expand_dims(x_test4, -1) #добавление еще одной оси в конец
# print(b.shape) #(1, 8, 2, 2, 1)
# c = np.squeeze(b) #удалает все оси, где 1 элемент
# print(c.shape) #(8, 2, 2)

