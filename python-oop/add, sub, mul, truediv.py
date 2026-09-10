from typing import Union

class Clock:
    __DAY = 86400
    def __init__(self, second: int) -> None:
        if not isinstance(second, int):
            raise TypeError('Секунды - целое число!')
        self.second = second % self.__DAY
    
    
    def __add__(self, other: Union[int, 'Clock']) -> 'Clock':
        if not isinstance(other, (int, Clock)):
            raise TypeError('Передайте целое число секунд или объект класса Clock!')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.second

        return Clock(self.second + sc)
    
    def __radd__(self, other: Union[int, 'Clock']) -> 'Clock':
        return self.__add__(other)
    
    def __sub__(self, other: Union[int, 'Clock']) -> 'Clock':
        if not isinstance(other, (int, Clock)):
            raise TypeError('Передайте целое число секунд или объект класса Clock!')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.second

        return Clock(self.second - sc)
    
    def __rsub__(self, other: Union[int, 'Clock']) -> 'Clock':
        if not isinstance(other, (int, Clock)):
            raise TypeError('Передайте целое число секунд или объект класса Clock!')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.second

        if other < self.second:
            raise ValueError('Время не может быть отрицательным!')
        return Clock(sc - self.second)

    def __str__(self) -> str:
        s = self.second % 60
        m = (self.second // 60) % 60
        h = (self.second // 3600) % 24
        return f'Текущее время - {h:02d}:{m:02d}:{s:02d}'

c1 = Clock(1003)
c2 = Clock(20000)
c3 = 10000 - c1
print(c3)