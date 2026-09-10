class Vector:
    min_coord = -100
    max_coord = 100

    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            print('Некорректно!')
    
    def get_coords(self):
        return (self.x, self.y)

    @staticmethod
    def norm2(x, y):
        return (x*x + y*y)


v = Vector(1, 20)
res = Vector.get_coords(v)
print(res)
print(v.validate(1000))
print(Vector.norm2(10, 20))