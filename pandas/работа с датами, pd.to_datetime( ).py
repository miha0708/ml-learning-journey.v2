import pandas as pd
import numpy as np


#можно либо сразу считать как data
df_date = pd.read_csv('data.csv', parse_dates=['data'], dayfirst=True)
# print(df_date.dtypes)

#либо изменить тип столбца на дату
df_date = df_date.astype({'data': 'datetime64[ns]'})
# print(df_date.dtypes)


# print(pd.to_datetime('2022-11-03')) #2022-11-03 00:00:00
# print(pd.to_datetime(df_date['data']))
# 0   2026-02-01
# 1   2026-02-03
# 2   2026-02-04
# 3   2026-02-05
# 4   2026-02-06
# 5   2026-02-07
# 6   2026-02-08
# 7   2026-02-15
# 8   2026-02-10
# 9   2026-02-11
# Name: data, dtype: datetime64[ns]


# print(pd.to_datetime('19-02-12')) #2012-02-19 00:00:00
# #хотя имели ввиду 2019 год, надо писать формат записи
# print(pd.to_datetime('19-02-12', format='%y-%m-%d')) #2019-02-12 00:00:00


#Свойства и методы дат

#Столбец с датой

# print(df_date)
#      id       data
# 0  1000 2026-02-01
# 1  1001 2026-02-03
# 2  1002 2026-02-04
# 3  1003 2026-02-05
# 4  1004 2026-02-06
# 5  1005 2026-02-07
# 6  1006 2026-02-08
# 7  1007 2026-02-15
# 8  1008 2026-02-10
# 9  1009 2026-02-11

# df_date['day_name'] = df_date['data'].dt.day_name() #Sunday и тд., если надо число, то просто day()
# df_date['month'] = df_date['data'].dt.month_name() #February и тд., аналогично как и с днями
# df_date['weekday'] = df_date['data'].dt.weekday #6 и тд., то есть какой месяц недели, 0-пн, 6-вс
# print(df_date) #если ..._name, то ставим скобки, иначе не надо

# print(df_date.loc[2, 'data'].day_name()) #Wednesday, можем обращаться не только к серии, но и к элементу отдельно


#Диапазон дат

# print(pd.date_range('2023-03-10', periods=10)) #по базе период это день
# DatetimeIndex(['2023-03-10', '2023-03-11', '2023-03-12', '2023-03-13',
#                '2023-03-14', '2023-03-15', '2023-03-16', '2023-03-17',
#                '2023-03-18', '2023-03-19'],
#               dtype='datetime64[us]', freq='D')

#чтобы изменить частоту периода используется период freq
# print(pd.date_range('2023-01-19', periods=5, freq='2MS')) #еще есть QS, YS, у нас шаг каждые 2 месяца
# DatetimeIndex(['2023-02-01', '2023-04-01', '2023-06-01', '2023-08-01',
#                '2023-10-01'],
#               dtype='datetime64[us]', freq='2MS')

#также можно указать диапазон дат
# print(pd.date_range('2023', '2025', freq='QS'))
# DatetimeIndex(['2023-01-01', '2023-04-01', '2023-07-01', '2023-10-01',
#                '2024-01-01', '2024-04-01', '2024-07-01', '2024-10-01',
#                '2025-01-01'],
#               dtype='datetime64[us]', freq='QS-JAN')

#также можно поделить на даты, между которыми равный интервал
# print(pd.date_range('2023', '2025', periods=4))
# DatetimeIndex(['2023-01-01 00:00:00', '2023-09-01 16:00:00',
#                '2024-05-02 08:00:00', '2025-01-01 00:00:00'],
#               dtype='datetime64[us]', freq=None)


#Фильтрация данных

# print(df_date)
#      id       data
# 0  1000 2026-02-01
# 1  1001 2026-02-03
# 2  1002 2026-02-04
# 3  1003 2026-02-05
# 4  1004 2026-02-06
# 5  1005 2026-02-07
# 6  1006 2026-02-08
# 7  1007 2026-02-15
# 8  1008 2026-02-10
# 9  1009 2026-02-11

# print(df_date[df_date['data'] == '2026-02-05']) #нашли такую строку
#      id       data
# 3  1003 2026-02-05


#Практика

# import pandas as pd

# df = pd.DataFrame({
#     "name": ["Alex", "Bob", "Emma", "David"],
#     "birthday": ["2006-08-15", "2005-12-01", "2004-03-27", "2006-01-09"]
# })

# df = df.astype({'birthday': 'datetime64[ms]'})
# df['year'] = df['birthday'].dt.year
# df['month'] = df['birthday'].dt.month
# df['day'] = df['birthday'].dt.day
# print(df)


# import pandas as pd

# df = pd.DataFrame({
#     "task": ["Python", "SQL", "Pandas", "ML"],
#     "start_date": ["2026-08-01", "2026-08-10", "2026-08-15", "2026-08-20"]
# })

# df['new_date'] = '2026-08-27'
# df = df.astype({'start_date': 'datetime64[ms]', 'new_date': 'datetime64[ms]'})
# df['days_passed'] = df['new_date'] - df['start_date']
# df.drop(columns='new_date', inplace=True)
# print(df)


# import pandas as pd

# df = pd.DataFrame({
#     "product": ["A", "B", "C", "D", "E"],
#     "date": [
#         "2026-07-30",
#         "2026-08-03",
#         "2026-08-11",
#         "2026-08-18",
#         "2026-09-01"
#     ],
#     "sales": [120, 250, 180, 300, 210]
# })

# df = df.astype({'date': 'datetime64[ms]'})
# # df = df[(df['date'] >= '2026-08-01') & (df["date"] <= '2026-08-20')] и так и так можно
# df = df.loc[(df['date'] >= '2026-08-01') & (df["date"] <= '2026-08-20')] #я бы оставил loc, а не маску
# df = df.sort_values(by=['date'], ascending=True)
# print(df)


import pandas as pd

df = pd.DataFrame({
    "event": ["Exam", "Gym", "Movie", "Study", "Meeting", "Rest"],
    "datetime": [
        "2026-08-25 09:30",
        "2026-08-25 18:15",
        "2026-08-26 21:00",
        "2026-08-27 10:45",
        "2026-08-28 12:01",
        "2026-08-29 08:00"
    ]
})

df = df.astype({'datetime': 'datetime64[ms]'})
df['weekday'] = df['datetime'].dt.weekday
df['hour'] = df["datetime"].dt.hour
df['is_weekend'] = df['datetime'].dt.day_of_week

def check_weekday(day):
    if 5 <= day <= 6:
        return True
    else:
        return False

df["is_weekend"] = df['is_weekend'].apply(check_weekday)
df = df.loc[(df['hour'] < 12) | ((df['hour'] == 12) & (df["datetime"].dt.minute == 0))]
print(df)