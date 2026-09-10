# class Counter:
#     def __init__(self):
#         self.__counter = 0
    
#     def __call__(self,step=1, *args, **kwds):
#         print('Был вызван __call__')
#         self.__counter += step
#         return self.__counter

# c2 = Counter()
# c1 = Counter()
# res2 = c2()
# c1(10)
# res1 = c1()
# print(res1, res2)


class StripChars:
    def __init__(self, chars):
        self.__chars = chars
    
    def __call__(self, *args, **kwds):
        new_strs = []
        for string in args:
            if not isinstance(string, str):
                raise TypeError('Передайте строку')
            new_strs.append(string.strip(self.__chars))
        return new_strs

    def __str__(self):
        return f'Робот-очиститель для знаков: {self.__chars}'

s1 = StripChars('.?! ')
print(s1)
res = s1(' Hello World! ', 'Ura!')
print(res)
