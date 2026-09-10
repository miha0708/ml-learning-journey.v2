class Point:
    def __init__(self, x=0, y=0):
        if self.__checkvalue(x) and self.__checkvalue(y):
            self.__x = x
            self.__y = y

    @staticmethod
    def __checkvalue(arg):
        return type(arg) in (int, float)

    def set_coord(self, x, y):
        if self.__checkvalue(x) and self.__checkvalue(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами!')
    
    def get_coord(self):
        return (self.__x, self.__y)
    
pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt._Point__y)