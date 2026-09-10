# class Geom:
#     name = 'Geom'

# class Line(Geom):
#     def draw(self):
#         print('Рисование линии')

# l = Line()
# l.draw()
# print(l.name)
# print(issubclass(Line, Geom))




class Geom(object):
    _name = 'Geom'
    def __init__(self, x1, y1, x2, y2, fill=None):
        print(f'Инициализатор Geom был вызван для {self.__class__}')
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def draw():
        print('Рисование Geom')


class Line(Geom):
    def draw():
        print('Рисование Line')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print('Инициализатор Rect')
        self.fill = fill

    def draw():
        print('Рисование Rect')

g = Geom(1, 2, 3, 4)
print(g._name)
r = Rect(1, 2, 3, 4)
print(r.__dict__)