# class FRange:
#     def __init__(self, start=0.0, stop=1.0, step=1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step

#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
    
#     def __next__(self) -> float:
#         if self.value + self.step <= self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration('Конец перебора!')
        
# f1 = FRange(0, 10, 0.5)
# for x in iter(f1):
#     print(x)

# print(iter(range(5)))


class Student:
    def __init__(self, name:str, grades:list[int]) -> None:
        self.name = name
        self.grades = grades
    
    def __iter__(self):
        self._idx = 0

        print(f'Какие оценки вы хотите увидеть у студента {self.name}а?')
        print('0 - все текущие оценки')
        print('2 - только двойки')
        print('3 - только тройки')
        print('4 - только четверки')
        print('5 - только пятерки')
        
        user_wanna_see_grades = int(input())
        self.user_chosie_spis = []

        if user_wanna_see_grades not in [0, 2, 3, 4, 5]:
            raise ValueError('Введено неверное значение!')
        
        self.user_choise = user_wanna_see_grades

        return self
    
    def __next__(self) -> int:
        while self._idx < len(self.grades):
            cur_grade = self.grades[self._idx]
            self._idx += 1

            if cur_grade == self.user_choise or self.user_choise == 0:
                self.user_chosie_spis.append(cur_grade)
        
            return f'{self.user_choise} - {self.user_chosie_spis}'
            
        raise StopIteration
    
s1 = Student('Михаил', [3, 5, 5, 3, 4, 5, 4])
for grades in s1:
    print(grades)