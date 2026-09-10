import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6])
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.mean())

# a = np.reshape(a, (3, 2))
# print(a)
# print(a.sum(axis=0)) #по вертикали [9, 12]
# print(a.sum(axis=1)) #по горизонтали [3 7 11]
# print(a.max(axis=1)) #макисмум для каждого ряда
# print(a.mean(axis=0)) #ср значение для каждого столбца


a = np.array([-1, 13, 0, -4, 50, 6.2])
# print(np.abs(a))
# print(np.abs(-10.6))

# print(a.max())
# print(np.amax(a))
# print(np.amin(a))

# print(np.round(a)) #одинаковые
# print(np.around(a))


# print(np.argmax(a)) #индекс максимального и минимального значения
# print(np.argmin(a))



# print(np.random.randint(0, 100, size=(6, 3), 'int16'))  #матрица 6х3 с рандомными числами int16 от 0 до 100
# print(np.random.rand()) #от 0 до 1
# print(np.random.randint(10, size=(5, 3)))

# print(np.random.rand(5))
# print(np.random.randn(5))


a = np.arange(10).reshape(5, 2)
np.random.shuffle(a)
# print(a) #перетасовка элементов

a = np.arange(10)
print(np.median(a)) #4.5 - медиана
