import pandas as pd


#pd.read_csv() - считывание файлов 
#DataFrame.to_csv() - запись данных в формат csv



# pd.read_csv(
#     filepath: путь к файлу,
#     sep: (по умол. ",") разделитель в строке файла,
#     Index_col: столбец /столбцы для использования в качестве меток строк,
#     usecols: список имен столбцов которые будут в результирующем DF,
#     squeeze: (по умол. False) если данные содержат только один столбец, вернёт серию,
#     dtype: словарь устанавливающий тип данных в столбцах,
#     nrows: количество строй для чтения,
#     parse_dates: список столбцов которые нужно представить в виде даты и времени,
#     infer_datetime_format: (по умол. False) если True, pandas попытается определить формат строк даты и времени в столбцах и, если это возможно, переключиться на более быстрый метод их анализа,
#     keep_date_col: (по умол. False) если значение True и parse_dates указывает на объединение нескольких столбцов, сохранит исходные столбцы,
#     encoding: кодировка, используемая при чтении.
# )


# DataFrame.to_csv(
#     filepath: путь к файлу в котором сохранятся данные в формате csv,
#     sep: (по умол. ",") разделитель в строке файла,
#     columns: столбцы для записи в файл,
#     header: (по умол. True) запишет первой строкой метки столбцов, если передать список строк, то они будут использоваться в качестве меток столбцов,
#     index: (по умол. True) запишет индексы строк в файл,
#     index_label: название столбца с индексами,
#     encoding: (по умол. utf8) кодировка записываемого файла
# )



df = pd.read_csv(
    'C:/Users/miham/Desktop/Pandas/test.csv',
    sep=',',
    index_col='age', #вместо индекса теперь колонка name
    usecols=['name', 'city', 'age'], #выборка столбцов
    # squeeze: (по умол. False) если данные содержат только один столбец, вернёт серию
    # dtype={'age':'float', 'name':'object'} #меняем тип указанного стобца
    # nrows=2 #импорт первых двух строк
    # parse_dates=['day_month_year'],
    # dayfirst=True,
    encoding='utf8'
    )

print(df)

# # df.rename(columns={'day_month_year':'date'}, inplace=True) #inplace не создает копию, а меняет при inplace=true
# print(df)



#Запись csv

#Сначала читаем и делаем всякие выборки, потом уже записываем!

# df = pd.read_csv(
#     'C:/Users/miham/Desktop/Pandas/test.csv',
#     encoding='utf8'
# )

# df.to_csv('C:/Users/miham/Desktop/Pandas/test_to_csv.csv', 
#           index=False,
#           sep=',',
#           columns=['name', 'age', 'city'],
#           header=['name_copy', 'age_copy', 'city_copy'],
#         #   index_label='index' #только при index=true
#           encoding='utf8'
# )

# df_check_to_csv = pd.read_csv('test_to_csv.csv')
# print(df_check_to_csv) #чекаем измененный файл


