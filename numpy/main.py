import numpy as np


# a = np.array([[1, 2, 3], [4, 90005, 6]], 'int32')
# b = a.reshape(2, 3)
# print(b)


# print(np.complex64(10))
# c = np.complex64(b)
# print(c)
# print(b)
# d = np.int32(c)
# print(d)

# a = np.array( (1, 2, 3), dtype='uint32')
# b = np.array((1, 8) , 'str_')
# print(a, b)

matrix_3_on_2 = np.array( [ [ [1, 2], [3, 4], [5, 6] ], [ [7, 8], [9, 10], [11, 12] ] ] )
print(matrix_3_on_2[0][2][0])
