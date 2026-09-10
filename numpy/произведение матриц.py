import numpy as np



# a = np.arange(9).reshape(3, 3)
# b = np.arange(9, 18).reshape(3, 3)
# #умножение матриц по правилам математики
# print(np.dot(a, b))
# print(np.matmul(a, b)) #предпочтительнее


# a = np.arange(9)
# b = np.ones(9)
# print(np.dot(a, b))
# print(np.inner(a, b)) #предпочтительнее, это все внутреннее умножение
# print(np.outer(a, b)) #внешнее умножение векторов


# a = np.array([4, 5, -1, 2])
# b = np.array([-3, 16, -1, 0])
# print(a * b) #вектор просто друг на друга перемноженный
# print(a @ b) #69 - внутреннее перемножение


#умножение вектора на матрицу
a = np.array([1, 2, 3])
b = np.arange(4, 10).reshape(3, 2)
print(np.dot(a, b)) #вектор на матрицу
print(np.dot(b, a)) #матрица на вектор
#вектор на матрицу - перемножение для каждого столбца, а матрица на вектор - перемножение для каждой строки
#dot = @