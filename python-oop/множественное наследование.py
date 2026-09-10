class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('Инициализатор Goods')
        self.name = name
        self.weight = weight
        self.price = price
    
    def get_info(self):
        return [f'Наименование: {self.name}',
                f'вес: {self.weight}', f'цена: {self.price}']



class MixinLog:
    ID = 0
    def __init__(self):
        print('Инициализатор MixinLog')
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_log(self):
        return(f'ID {self.id}: Товар был продан в 17:12')

    def get_info(self):
        return f'{self.id}'


class Notebook(Goods, MixinLog):
    def get_info(self):
        return MixinLog.get_info(self)



n = Notebook('Acer', 1.5, 30000)
print(n.get_info())
print(n.get_info())