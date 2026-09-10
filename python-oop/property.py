class Person:

    @staticmethod
    def validation(age):
        return not(age < 18 or age > 100)

    def __init__(self, name, age):
        if self.validation(age):
            self.__age = age
            self.__name = name
        else:
            print('Возраст должен быть в диапазоне от 18 до 100 лет')

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if self.validation(age):
            self.__age = age

p = Person('Lara', 18)
p.age = 30
print(p.__dict__)
