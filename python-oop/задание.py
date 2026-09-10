from typing import Union

class Coin:
    MIN_PRICE = 0.00

    def __init__(self, name:str, price: Union[int, float]) -> None:
        self.check_price(price)
        self.check_name(name)

        self.name = name
        self.__price = price
    
    @classmethod
    def check_price(cls, price):
        if price <= cls.MIN_PRICE:
            raise ValueError('Минимальная цена монеты - 0.00$')
        if not isinstance(price, (int, float)):
            raise TypeError('Цена монеты должна быть числом')
        
    def check_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Некорректное название монеты')
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.check_price(value)
        self.__price = value

    def __str__(self):
        return f'Монета {self.name}: {self.__price}$'



class Wallet:
    def __init__(self, owner:str, usd_balance=0):
        self.owner = owner
        self.usd_balance = usd_balance
        self.crypto_balance = {}
    

    def deposit(self, amount):
        self.usd_balance += amount

    def __str__(self):
        return f'Владелец: {self.owner}, баланс: {self.usd_balance}$'
    

class Exchange:
    crypto_balance = []

    def __init__(self):
        self.available_coins = []
    
    def add_money(self, value):
        self.wallet += value

    def add_coin(self, coin):
        self.available_coins.append(coin)
    

    def buy_crypto(self, coin_name, coin_price, amount):
        if coin_name not in self.available_coins:
            print('Монета не найдена')
        
        buy_cost = float(coin_price) * amount
        if buy_cost > self.wallet:
            print('Недостаточно средств')
        else:
            self.wallet -= buy_cost
            self.crypto_balance.append((coin_name, amount))
