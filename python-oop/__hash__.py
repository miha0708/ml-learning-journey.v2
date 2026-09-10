class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 20)
print(p1 == p2)
print(hash(p1), hash(p2), sep='\n')