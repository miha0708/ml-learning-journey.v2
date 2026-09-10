import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# b = np.array([1, 2, 30, 40, 100])

# print(a==b) #[True, True, False, False, False]
# print(a[a > 2]) #[3 4 5]
# print(np.greater(a, b)) #a > b
# print(np.less(a, b)) #a < b
# print(np.equal(a, b)) #a == b
# print(np.array_equal(a, b)) #True or False, not array

# if np.array_equal(a, b):
#     print('a == b')
# else:
#     print('a != b')

# print(np.any(a > 2)) #we need only one el which greater than 2
# print(np.all(a > 2)) #false, because in a, we have 1


# a = np.array([np.nan, np.inf, -np.inf])
# print(np.isinf(a)) #[false, true, true]
# print(np.isnan(a)) #[true, false, false]
# indx = np.isinf(a)
# a = a[~indx] #we delete all el +-inf
# print(a) #[nan]
# print(np.isfinite(a)) #[false], all el is false(inf, nan...)


# a = np.array([1+2j, 3-4j, 5+0j])
# print(np.iscomplex(a)) #[True, True, False]
# print(np.isreal(a)) #[False, False, True] nan and inf is real numbers!


x = np.array([True, False, True, False])
y = np.array([True, True, False, False])

print(np.logical_and(x, y)) #[true, false, false, false]
print(np.logical_or(x, y)) #[true, true, true, false]
print(np.logical_not(x)) #reversed x [false, true, false, true]
print(np.logical_xor(x, y)) #[false, true, true, false]