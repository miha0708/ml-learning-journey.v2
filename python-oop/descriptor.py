class Point3D:
    def __init__(self, x, y, z):
        self.verify_coord(x)
        self.verify_coord(y)
        self.verify_coord(z)

        self.x = x
        self.y = y
        self.z = z
    
    @staticmethod
    def verify_coord(x):
        if type(x) != int:
            raise TypeError('Координаты должны быть представлены в виде целых чисел')
            
pt = Point3D(1, 2, 100000)
print(pt.__dict__)