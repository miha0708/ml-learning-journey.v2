import numpy as np

lst = [1, 2, 3]
a = np.array([1, 2, 3])
# print(lst*2) #[1 2 3 1 2 3]
# print(a*2) #[2 4 6]
# print(-a*2) #[-2 -4 -6]
# b = np.array([4, 5, 6]) #при операциях массива на массив, длины должны быть равными
# print(b-a) #[3, 3, 3]

b = np.arange(1, 7).reshape(2, 3)
print(b**a)