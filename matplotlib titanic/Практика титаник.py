import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv('titanic.csv')


# stats_of_survived = df.groupby('Sex')['Survived'].sum()
# plt.bar(stats_of_survived.index, stats_of_survived.values, color=['pink', 'blue'], edgecolor='black')
# plt.grid(axis='y', linestyle='--')
# plt.ylabel('Кол-во выживших')
# plt.xlabel('Пол выживших')
# plt.title('Сравнение выживших м и ж')

# plt.show()

# ages = df['Age'].dropna()

# avg_survived = ages.median()
# plt.hist(ages, bins=20)
# plt.title('Распределение людей по возрасту')
# plt.xlabel('Возраст')
# plt.ylabel('Кол-во выживших')
# plt.axvline(x=avg_survived, color='red', linestyle='--')

# plt.show()


# df_sex_pclass = df.groupby(['Sex', 'Pclass']).agg({'Age': 'mean'})
# df_sex_pclass['Age'] = round(df_sex_pclass['Age']).astype('int16')
# df_sex_pclass = df_sex_pclass.reset_index()
# df_sex_pclass = df_sex_pclass.sort_values(['Pclass', 'Sex'], ascending=[True, False])

# labels = df_sex_pclass['Sex'] + ' ' + df_sex_pclass['Pclass'].astype('str')
# colors = df_sex_pclass['Sex'].map({'male': 'steelblue', 'female':'pink'})

# plt.bar(labels, df_sex_pclass['Age'], color=colors)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.xlabel('Пол и класс билета')
# plt.ylabel('Средний возраст')
# plt.title('Общая информация о среднем возрасте для каждого пола и класса')

# plt.show()


# fare1 = df[df['Pclass'] == 1]['Fare']
# fare2 = df[df['Pclass'] == 2]['Fare']
# fare3 = df[df['Pclass'] == 3]['Fare']

# plt.boxplot([fare1, fare2, fare3], tick_labels=[1, 2, 3])
# plt.show()

# bars = plt.bar(df['Embarked'].value_counts().index, df['Embarked'].value_counts().values)
# plt.xlabel('Порт')
# plt.ylabel('Кол-во пассажиров')
# plt.title('Кол-во пассажиров в каждом порту')
# plt.grid(axis='y', linestyle='--', color='gray')
# plt.bar_label(bars, color='red')
# plt.show()


df_scatter = df[['Age', 'Fare', 'Survived']].dropna().copy()
df_scatter['color'] = df_scatter['Survived'].map({0: 'red', 1:'green'})
# plt.scatter('Age', 'Fare', data=df_scatter, color=df_scatter['color'])
# plt.grid(axis='y', linestyle='--', color='gray')
# plt.xlabel('Возраст')
# plt.ylabel('Стоимость билета')
# plt.title('Статистика выживания по возрасту и стоимости билета')

# plt.show()

# df_pivot = df.pivot_table(
#     columns='Pclass',
#     index='Sex',
#     values='Survived',
#     aggfunc='mean'
# )

# df_pivot *= 100
# print(df_pivot)

# plt.imshow(df_pivot, cmap='RdYlGn')

# plt.xticks([0, 1, 2], ['1 класс', '2 класс', '3 класс'])
# plt.yticks([0, 1], ['Женщины', 'Мужчины'])

# plt.colorbar(label='Процент выживших')

# plt.title('Вероятность выживания по полу и классу')
# plt.show()



# bar_1 = df.groupby(['Sex']).agg({'Survived':'sum'})
# print(bar_1)
# hist_2 = df['Age'].dropna()
# boxplot_3_1 = df[df['Pclass'] == 1]['Fare']
# boxplot_3_2 = df[df['Pclass'] == 2]['Fare']
# boxplot_3_3 = df[df['Pclass'] == 3]['Fare']

# f, ax = plt.subplots(2, 2)
# ax[1, 0].scatter(
#     df_scatter['Age'],
#     df_scatter['Fare'],
#     color=df_scatter['color']
# )
# ax[0, 0].bar(bar_1.index, bar_1['Survived'].values)
# ax[0, 1].hist(hist_2)
# ax[1, 1].boxplot([boxplot_3_1, boxplot_3_2, boxplot_3_3], tick_labels = [1, 2, 3])

# ax[0, 0].set_title('Выжившие по полу')
# ax[0, 1].set_title('Распределение возраста')
# ax[1, 0].set_title('Возраст vs стоимость билета')
# ax[1, 1].set_title('Стоимость билетов по классам')

# for axes in ax.flat:
#     axes.grid(axis='y', linestyle='--', alpha=0.5)

# plt.tight_layout()
# plt.show()


#Ласт 3 гипотезы

#Как возраст влияет на шанс выживания?

bins = [0, 12, 18, 35, 60, 1000]
groups = ['Child', 'Teenagers', 'Young', 'Vzroslye', 'Older']
df['Category_of_age'] = pd.cut(x=df['Age'], bins=bins, labels=groups)


ages_survived = df.groupby('Category_of_age')['Survived'].agg(['sum', 'size'])
ages_survived.columns = ['Survived', 'TotalPassangers']
ages_survived['Shans vizit'] = round(ages_survived['Survived'] / ages_survived['TotalPassangers'] * 100, 1)

plt.bar(ages_survived.index, ages_survived['Shans vizit'].values, color='pink', edgecolor='black')
plt.title('Процент выживания по возрасту')
plt.xlabel('Категория возраста')
plt.ylabel('Процент выживания')
plt.grid(axis='y', linestyle='--', color='gray')
plt.show()