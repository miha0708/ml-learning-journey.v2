import pandas as pd
import numpy as np


#Метод map()

# df = pd.DataFrame({
#     "name": ["Alex", "Bob", "Emma"],
#     "grade": [5, 4, 3]
# })

#Создаю словарь, по которому будем менять оценки на наш формат
# grades = {5: "Nice", 4: "Good", 3: "U can better"}
# df['grade'] = df['grade'].map(grades)
# print(df)
#    name         grade
# 0  Alex          Nice
# 1   Bob          Good
# 2  Emma  U can better

#Если нет такого значения у словаря для конвертации в нужное, то NaN


#Метод replace()
#гибкий map()
df = pd.DataFrame({'name': ['Misha', 'Dasha', 'Lena', 'Lesha'],
                   'age': [18, 15, 46, 47],
                   'city': ['Yaroslavl', 'Yaroslavl', 'Nekrasovskoe', 'Moscow'],
                   'gender': ['M', 'F', 'F', 'M']})

df.replace({
    'age': {
        18: 'young',
        15: 'young',
        46: 'old',
        47: 'old'
    },
    'gender': {
        'M': 'Male',
        'F': 'Female'
    }
}, inplace=True)
# print(df)
#     name    age          city  gender
# 0  Misha  young     Yaroslavl    Male
# 1  Dasha  young     Yaroslavl  Female
# 2   Lena    old  Nekrasovskoe  Female
# 3  Lesha    old        Moscow    Male

#map для создания нового столбца из старого
#replce для очистки данных


#Метод duplicated() — найти дубликаты

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Alex", "Emma", "Bob"],
    "age": [20, 19, 20, 22, 19]
})

# print(df.duplicated())
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# dtype: bool
# print(df[df.duplicated()]) #показать только ддубликаты
#    name  age
# 2  Alex   20
# 4   Bob   19

#аргумент subset по какому столбцу
# print(df.duplicated(subset=['name']))

# print(df.duplicated(keep="first")) #база
# print(df.duplicated(keep="last")) #идет с конца
# print(df.duplicated(keep=False)) #все копии True, а уникальные значения False


#Метод drop_duplicates() — удалить дубликаты

# print(df.drop_duplicates()) #просто удалить дубликаты
# print(df.drop_duplicates(subset=['name'])) #только по столбцу name
# print(df.drop_duplicates(subset=["name"], keep="last")) #последние остаются
# print(df.drop_duplicates(subset=["name"], keep=False)) #удалить все повторы + оригиналы, только уникальные остаются


#Практика

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Alex", "Emma", "Kate", "Bob"],
    "city": ["msk", "spb", "msk", "kazan", "spb", "spb"],
    "gender": ["M", "M", "M", "F", "F", "M"]
})

# Через map сделать столбец city_full с полными названиями городов.
# Через replace заменить "M" → "Male", "F" → "Female".
# Вывести только повторяющиеся строки по имени.
# Удалить повторяющиеся имена, оставив последнюю запись.
# Вывести все строки, которые имеют дубликаты (keep=False).

dict_city_full = {
    'msk': 'Moscow',
    'spb': 'Petersburg',
    'kazan': 'Kazan'
}
df['city_full'] = df['city'].map(dict_city_full)
df = df.replace({
    'gender': {
        'M': 'Male',
        'F': 'Female'
    }
})
# print(df[df.duplicated(subset=['name'])])
# df = df.drop_duplicates(subset=['name'], keep='last')
# print(df)
# print(df[df.duplicated(keep=False)])



#Блок 2

#Метод query() — фильтрация строк

df = pd.DataFrame({
    "name": ["Alex", "Bob", "Alex", "Emma", "Bob"],
    "age": [20, 19, 20, 22, 19]
})

# print(df[df['age'] > 19]) #одинаково
# print(df.query('age > 19')) #только еще можно использовать переменные здесь
# m = 10
# print(df.query('age == @m*2'))
#    name  age
# 0  Alex   20
# 2  Alex   20

#Метод query() всегда возвращает df


#Метод concat() — склеивание DataFrame

jan = pd.DataFrame({
    "name": ["Alex", "Bob"],
    "sales": [100, 200]
})

feb = pd.DataFrame({
    "name": ["Emma", "Kate"],
    "sales": [150, 180]
})

# print(pd.concat([jan, feb]))
#    name  sales
# 0  Alex    100
# 1   Bob    200
# 0  Emma    150
# 1  Kate    180

names = pd.DataFrame({
    "name": ["Alex", "Bob"]
})

ages = pd.DataFrame({
    "age": [20, 21]
})

# print(pd.concat([names, ages], axis=1, ignore_index=True))
#    name  age
# 0  Alex   20
# 1   Bob   21


#Метод pivot_table() — сводная таблица


# Главная идея

# pivot_table одновременно делает три вещи:
# Группирует данные.
# Считает агрегат.
# Разворачивает результат в удобную таблицу.

# df.pivot_table(
#     index=..., строки
#     columns=..., столбцы
#     values=..., данные для агрерации
#     aggfunc=... функция агрегации
# )

# fill_value=0 вместо NaN
# margins=True добавляет строку и столбец All


#Практика по блоку 2
import pandas as pd

# df = pd.DataFrame({
#     "name": ["Alex", "Bob", "Emma", "Kate", "John", "Lisa", "Mike", "Anna"],
#     "age": [20, 18, 22, 19, 25, 21, 24, 20],
#     "city": ["Moscow", "SPB", "Moscow", "Kazan", "SPB", "Moscow", "Kazan", "SPB"],
#     "salary": [70000, 45000, 90000, 50000, 120000, 85000, 95000, 60000]
# })


# print(df.query('age > 20'))
# print(df.query("city == 'Moscow' and salary > 80000"))
# print(df.query("(city == 'Kazan' or salary < 50000) and not(age < 20)"))

# city = "SPB"
# min_salary = 50000
# print(df.query('city == @city and salary >= @min_salary'))


jan = pd.DataFrame({
    "name": ["Alex", "Bob", "Emma"],
    "sales": [100, 200, 150]
})

feb = pd.DataFrame({
    "name": ["Kate", "John", "Lisa"],
    "sales": [180, 250, 170]
})

mar = pd.DataFrame({
    "name": ["Mike", "Anna"],
    "sales": [220, 190]
})

age = pd.DataFrame({
    "age": [20, 19, 22]
})


# print(pd.concat([jan, feb], ignore_index=True))
# print(pd.concat([jan, feb, mar]))
# print(pd.concat([jan, age], axis=1))
#просто добавятся еще два столбца с таким же названием


sales = pd.DataFrame({
    "city": [
        "Moscow","Moscow","Moscow",
        "SPB","SPB","SPB",
        "Kazan","Kazan","Kazan"
    ],
    "product": [
        "Phone","Laptop","Phone",
        "Phone","Laptop","Laptop",
        "Phone","Laptop","Phone"
    ],
    "month": [
        "Jan","Jan","Feb",
        "Jan","Jan","Feb",
        "Jan","Feb","Feb"
    ],
    "sales": [100,200,120,150,180,210,90,130,110]
})

# print(sales, end='\n'*3)

# new_df = sales.pivot_table(
#     values='sales',
#     index='city',
#     aggfunc='sum'
# )

# new_df = sales.pivot_table(
#     values='sales',
#     columns='product',
#     index='city',
#     aggfunc='sum'
# )

# new_df = sales.pivot_table(
#     index='city',
#     columns='month',
#     values='sales',
#     aggfunc=['mean'],
#     fill_value=0
# )

# print(new_df)


# new_df = sales.pivot_table(
#     index='month',
#     columns='city',
#     values='sales',
#     aggfunc=['max'],
#     margins=True
# )
# print(new_df)


orders_jan = pd.DataFrame({
    "user": ["Alex","Bob","Emma","Kate"],
    "city": ["Moscow","SPB","Moscow","Kazan"],
    "amount": [1200,800,950,700]
})

orders_feb = pd.DataFrame({
    "user": ["Alex","Kate","Bob","Mike"],
    "city": ["Moscow","SPB","SPB","Kazan"],
    "amount": [1500,900,1000,1100]
})

orders_jan_feb = pd.concat([orders_jan, orders_feb], ignore_index=True)
# print(orders_jan_feb)

orders_jan_feb = orders_jan_feb.query('amount > 850')
print(orders_jan_feb)

new_orders_jan_feb = orders_jan_feb.pivot_table(
    index='city',
    columns='user',
    values='amount',
    aggfunc=['sum'],
    fill_value=0
)

print(new_orders_jan_feb)