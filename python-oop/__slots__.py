class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

pt3 = Point3D(1, 2, 3)
pt3.w = 1000
print(pt3.w)
print(pt3.__dict__)



