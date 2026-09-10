import pandas as pd
import numpy as np


df = pd.DataFrame({
    'col_1': [1, 2, 3],
    'col_2': [4, 5, 6],
    'has_car': [True, True, False]
})

#Метод iat
# print(df.iat[0, 1]) #[индекс строки, индекс стобца] 4
# print(df['col_1'].iat[1]) #2

#Метод at
#такой же, как и iat, только вместо индексов метки
# print(df.at[1, 'col_2'])
# df.at[1, 'col_2'] = 1000 #может менять, в отличии от iat
# print(df['col_2'].at[1])

#Метод iloc
# print(df.iloc[1, 1]) 5, индекс строки и столбца
# print(df.iat[1, 1]) 5
# print(df.at[1, 'col_2']) 5

# idx_car_df = df['has_car'].to_list()
# print(df.iloc[idx_car_df, [False, True, True]]) #пересечение строк с машиной true и столбцов 2 и 3
# print(df.iloc[:2, [1]]) #первые 2 строки второго столбца, если указать еще 1 скобки, то метод вернет df

#Метод loc(рекомендуемый)
#такой же как и iloc, только все делается по меткам

# print(df)
# print(df.loc[2, 'col_2']) #6
# print(df.loc[[0, 1], ['col_1']]) #только первая колонка и первые 2 элемента
# print(df.loc[:2, 'col_1':'col_2']) #крайние элементы среза тоже учавствуют

# print(df[df['col_2'] == 5])
# print(df.loc[df['col_2'] == 5]) #доступ по логическому условию


#Практика

import pandas as pd

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Charlie", "David", "Emma"],
    "age": [20, 19, 21, 18, 22],
    "city": ["Moscow", "SPB", "Kazan", "Sochi", "Perm"],
    "score": [88, 91, 76, 95, 84]}, 
    index=["a", "b", "c", "d", "e"]
)

print(df)
# print(df.at['c', 'age'])
# print(df.iat[3, 2])
# df.at['e', 'score'] = 100
# df.iat[1, 1] = 25

# print(df.iloc[[2], :]) #хочу в виде df
# print(df.iloc[:2, [0, 1]])
# print(df.iloc[-2:, :])
#вернет со второй по счету до 4 по счету вкюч строки и пересечение с 3 по счету столбцом до конца

# print(df.loc['b':'d', ['name', 'score']])
# idx_score_90 = df[df['score'] > 90].index
# print(df.loc[idx_score_90, ['name', 'city']])
#войдут b,c,d

#да
#нет
#индекс и метки, попарно так и отличаются друг от друга, ну еще loc и iloc поддерживают срезы и немного медленнее
