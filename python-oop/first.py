from time import *

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        if x == None or y == None:
            print('Вы неверно ввели данные!')

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def get_coords(self):
        print((self.x, self.y))

pt = Point(1, 2)