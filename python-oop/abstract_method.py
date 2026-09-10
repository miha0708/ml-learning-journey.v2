class Geom:
    def get_perim(self):
        raise NotImplementedError('Метод get_perim должен быть переопределен в дочернем классе!')


class Rect(Geom):
    def __init__(self, h, w):
        self.h = h
        self.w = w
    
    def get_perim(self):
        return 2*(self.h + self.w)

class Square(Geom):
    def __init__(self, a):
        self.a = a

    # def get_perim(self):
    #     return 4*self.a

geom = [Rect(1, 2), Square(10)]
for g in geom:
    print(g.get_perim())