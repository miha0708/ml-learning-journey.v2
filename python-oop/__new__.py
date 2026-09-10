# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('Вызов __new__ для: ' + str(cls))
#         return super().__new__(cls)
    
#     def __init__(self, x=0, y=0):
#         print('Вызов __init__ для: ' + str(self))
#         self.x = x
#         self.y = y

# pt = Point(1, 2)


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        self.__instance = None
    
    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port
    
    def connect(self):
        print(f'Соединение с БД: Пользователь - {self.user}, пароль - ***, порт - {self.port}')
    
    def close(self):
        print('Закрытие соединения с БД')
    
db = DataBase('misha', '1234', '0000')
db2 = DataBase('dasha', '012345', '0001')
print(id(db), id(db2))
db2.connect()
db.connect()