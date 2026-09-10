class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Студент - {self.name}, оценки - {self.marks}'
    
    def __getitem__(self, key: str) -> 'Student':
        if not isinstance(key, str):
            raise TypeError('Передайте строку!')
        if key == 'имя' or key == 'Имя':
            return self.name
        
        elif key == 'оценки' or key == 'Оценки':
            print('Какую по счету вы хотите увидеть оценку?')
            print(f'Доступно от 0 до {len(self.marks) - 1}')
            idx = int(input())
            if 0 <= idx <= len(self.marks) - 1:
                return self.marks[idx]
            else:
                raise ValueError('!')
        
        else:
            raise ValueError('Передайте строку: "Оценки" или "Имя"')
    
    def __setitem__(self, key, value):
        self.marks[key] = value
    
    def __delitem__(self, key):
        del self.marks[key]

s1 = Student('Михаил', [3, 5, 4, 4, 5])
print(s1['оценки'])