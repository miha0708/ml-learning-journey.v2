from typing import Union

class Clock:
    __day = 86400
    def __init__(self, seconds: int) -> None:
        if not isinstance(seconds, int):
            raise TypeError('Передайте целое число')
        self.seconds = seconds % self.__day

    def __eq__(self, other: Union[int, 'Clock']) -> bool:
        if not isinstance(other, (int, Clock)):
            raise TypeError('Невозможно сравнить! Сравниваются целые числа или экземпляры класса')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        
        return self.seconds == sc
    
    def __lt__(self, other: Union[int, 'Clock']) -> bool:
        if not isinstance(other, (int, Clock)):
            raise TypeError('Невозможно сравнить! Сравниваются целые числа или экземпляры класса')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        
        return self.seconds < sc
    
    def __le__(self, other: Union[int, 'Clock']) -> bool:
        if not isinstance(other, (int, Clock)):
            raise TypeError('Невозможно сравнить! Сравниваются целые числа или экземпляры класса')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        
        return self.seconds <= sc
    
    def __gt__(self, other: Union[int, 'Clock']) -> bool:
        if not isinstance(other, (int, Clock)):
            raise TypeError('Невозможно сравнить! Сравниваются целые числа или экземпляры класса')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        
        return self.seconds > sc

    def __ge__(self, other: Union[int, 'Clock']) -> bool:
        if not isinstance(other, (int, Clock)):
            raise TypeError('Невозможно сравнить! Сравниваются целые числа или экземпляры класса')
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        
        return self.seconds >= sc
    


c1 = Clock(1000)
c2 = Clock(10000)
print(c1 >= 1000)
