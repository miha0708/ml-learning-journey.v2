from string import ascii_letters


class Person:

    s_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    s_rus_upper = s_rus.upper()

    max_age = 100
    min_age = 18

    min_weight = 30.0
    max_weight = 200.0

    nums = '0123456789'

    def __init__(self, fio, age, ps, weight):
        self.verify_fio(fio)
        self.verify_age(age)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__age = age
        self.__ps = ps
        self.__weight = weight


    @classmethod
    def verify_fio(cls, fio):
        if type(fio) is not str:
            raise TypeError('Данные ФИО должны быть строкой')
        
        f = fio.split()
        if len(f) != 3:
            raise ValueError('Данные ФИО должны содержать имя, фамилию и отчество')
        
        letters = ascii_letters + cls.s_rus + cls.s_rus_upper
        for s in f:
            if len(s) < 1:
                raise ValueError('В ФИО должне быть минимум 1 символ')
            else:
                if len(s.strip(letters)) != 0:
                    raise ValueError('Содержится недопустимый символ')
                
    @classmethod
    def verify_age(cls, age):
        if type(age) is not int:
            raise TypeError('Возраст должен быть целой положительной величиной')
        
        if age < cls.min_age or age > cls.max_age:
            raise ValueError(f'Возраст должен быть в диапазоне от {cls.min_age} до {cls.max_age}')
    

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) is not str:
            raise TypeError('Пасспорт должен быть строкой')
        
        p = ps.split()
        if len(p) != 2:
            raise ValueError('В паспорте должны быть серия и номер')
        if len(p[0]) != 4 or len(p[1]) != 6:
            raise ValueError('Пасспорт должен быть представлен в формате **** ******')
        
        letter = cls.nums + ' '
        if len(ps.strip(letter)) != 0:
            raise ValueError('В паспорте должны быть только цифры и пробел')
        

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) not in [int, float]:
            raise TypeError('Вес должен быть числом')
        
        if weight < cls.min_age or weight > cls.max_age:
            raise ValueError(f'Введен некорректный вес')
        

    @property
    def fio(self):
        return self.__fio
    
    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio.split()
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age
    
    @property
    def ps(self):
        return self.__ps
    
    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight



p = Person('Макаров Михаил Алексеевич', 19, '7822 550365', 100.0)
print(p.fio)
p.fio = 'Макарова Дарья Алексеевна'
print(p.fio)
p.weight = 70
print(p.__dict__)