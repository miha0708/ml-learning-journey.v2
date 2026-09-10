import numpy as np
import pandas as pd


# df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"], 
#                     "B": ["B0", "B1", "B2", "B3"], 
#                     "C": ["CO", "C1", "C2", "C3"], 
#                     "D": ["DO", "D1", "D2", "D3"]}, 
#                     index=[0, 1, 2, 3])

# df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"], 
#                     "B": ["B4", "B5", "B6", "B7"], 
#                     "C": ["C4", "C5", "C6", "C7"], 
#                     "D": ["D4", "D5", "D6", "D7"]},
#                     index=[1, 2, 3, 4])

# df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"], 
#                     "B": ["B8", "B9", "B10", "B11"], 
#                     "C": ["C8", "C9", "C10", "C11"], 
#                     "D": ["D8", "D9", "D10", "D11"]}, 
#                     index=[2, 3, 4, 5])

# print(df1, end='\n'*3)
# print(df2, end='\n'*3)
# print(df3, end='\n'*3)

#Функция pd.concat()

# print(pd.concat([df1, df2, df3])) #индексы сохраняются от исходных df, чтобы такого не было ignore_index=True
#      A    B    C    D
# 0   A0   B0   CO   DO
# 1   A1   B1   C1   D1
# 2   A2   B2   C2   D2
# 3   A3   B3   C3   D3
# 1   A4   B4   C4   D4
# 2   A5   B5   C5   D5
# 3   A6   B6   C6   D6
# 4   A7   B7   C7   D7
# 2   A8   B8   C8   D8
# 3   A9   B9   C9   D9
# 4  A10  B10  C10  D10
# 5  A11  B11  C11  D11

# print(pd.concat([df1, df2, df3], ignore_index=True)) #теперь индексы по порядку
#       A    B    C    D
# 0    A0   B0   CO   DO
# 1    A1   B1   C1   D1
# 2    A2   B2   C2   D2
# 3    A3   B3   C3   D3
# 4    A4   B4   C4   D4
# 5    A5   B5   C5   D5
# 6    A6   B6   C6   D6
# 7    A7   B7   C7   D7
# 8    A8   B8   C8   D8
# 9    A9   B9   C9   D9
# 10  A10  B10  C10  D10
# 11  A11  B11  C11  D11

#Также можно объеднить по строкам, а не столбцам
# print(pd.concat([df1, df2, df3], ignore_index=False, axis=1))
#      A    B    C    D    A    B    C    D    A    B    C    D
# 0   A0   B0   CO   DO  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 1   A1   B1   C1   D1   A4   B4   C4   D4  NaN  NaN  NaN  NaN
# 2   A2   B2   C2   D2   A5   B5   C5   D5   A8   B8   C8   D8
# 3   A3   B3   C3   D3   A6   B6   C6   D6   A9   B9   C9   D9
# 4  NaN  NaN  NaN  NaN   A7   B7   C7   D7  A10  B10  C10  D10
# 5  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11


#Метод merge()


df_1 = pd.DataFrame({'client_id': [100103, 21990, 455323, 100103, 21990, 455323, 455323, 21990, 455323],
                    'product': ['product_2', 'product_2', 'product_1', 'product_1', 'product_1', 'product_3', 'product_3', 'product_3', 'product_6']})

df_2= pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'],
                    'price': [1000, 2000, 3000, 4000, 5000]})

# print(df_1)
#    client_id    product
# 0     100103  product_2
# 1      21990  product_2
# 2     455323  product_1
# 3     100103  product_1
# 4      21990  product_1
# 5     455323  product_3
# 6     455323  product_3
# 7      21990  product_3
# 8     455323  product_6

# print(df_2)
#      product  price
# 0  product_1   1000
# 1  product_2   2000
# 2  product_3   3000
# 3  product_4   4000
# 4  product_5   5000


#Методы объединения(how=)

# print(df_1.merge(df_2, how='left')) #только то, что есть слева
#    client_id    product   price
# 0     100103  product_2  2000.0
# 1      21990  product_2  2000.0
# 2     455323  product_1  1000.0
# 3     100103  product_1  1000.0
# 4      21990  product_1  1000.0
# 5     455323  product_3  3000.0
# 6     455323  product_3  3000.0
# 7      21990  product_3  3000.0
# 8     455323  product_6     NaN

# print(df_1.merge(df_2, how='right')) #только то, что есть справа
#    client_id    product  price
# 0   455323.0  product_1   1000
# 1   100103.0  product_1   1000
# 2    21990.0  product_1   1000
# 3   100103.0  product_2   2000
# 4    21990.0  product_2   2000
# 5   455323.0  product_3   3000
# 6   455323.0  product_3   3000
# 7    21990.0  product_3   3000
# 8        NaN  product_4   4000
# 9        NaN  product_5   5000

# print(df_1.merge(df_2, how='inner')) #только то, что есть в обоих
#    client_id    product  price
# 0     100103  product_2   2000
# 1      21990  product_2   2000
# 2     455323  product_1   1000
# 3     100103  product_1   1000
# 4      21990  product_1   1000
# 5     455323  product_3   3000
# 6     455323  product_3   3000
# 7      21990  product_3   3000

# print(df_1.merge(df_2, how='outer')) #все элементы из обоих
#     client_id    product   price
# 0    455323.0  product_1  1000.0
# 1    100103.0  product_1  1000.0
# 2     21990.0  product_1  1000.0
# 3    100103.0  product_2  2000.0
# 4     21990.0  product_2  2000.0
# 5    455323.0  product_3  3000.0
# 6    455323.0  product_3  3000.0
# 7     21990.0  product_3  3000.0
# 8         NaN  product_4  4000.0
# 9         NaN  product_5  5000.0
# 10   455323.0  product_6     NaN


#Аргумент on
# print(df_1.merge(df_2, how='inner', on='product')) #по какому стобцу будем объединять

# df_1.rename(columns={'product':'prod'}, inplace=True)

# print(df_1.merge(df_2,
#                  how='inner',
#                  left_on=['prod'],
#                  right_on=['product'],
#                  ))

#еще есть аргумент suffixes


#Практика
import pandas as pd

students = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alex", "Bob", "Charlie", "Emma"]
})

scores = pd.DataFrame({
    "id": [2, 3, 5],
    "score": [85, 92, 100]
})

# print(students.merge(scores, how='inner', on='id'))
# print(students.merge(scores, how='left', on='id'))

employees = pd.DataFrame({
    "employee_id": [101, 102, 103],
    "salary": [70000, 60000, 90000]
})

bonuses = pd.DataFrame({
    "id": [101, 102, 103],
    "salary": [5000, 3000, 8000]
})


# total_df = employees.merge(bonuses, left_on=['employee_id'], right_on=['id'], suffixes=('', '_bonus'))
# total_df = total_df.drop(columns='id')
# print(total_df)


customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Alex", "Bob", "Emma", "Kate"]
})

orders = pd.DataFrame({
    "order_id": [11, 12, 13, 14, 15],
    "customer_id": [1, 2, 2, 3, 2],
    "product_id": [101, 102, 103, 101, 101]
})

products = pd.DataFrame({
    "product_id": [101, 102, 103],
    "product": ["Laptop", "Mouse", "Keyboard"],
    "price": [1000, 50, 120]
})

new_cust_orders = customers.merge(orders, how='inner')
total_df = new_cust_orders.merge(products, how='inner')
total_df = total_df.drop(columns=['customer_id', 'order_id', 'product_id'])
print(total_df)