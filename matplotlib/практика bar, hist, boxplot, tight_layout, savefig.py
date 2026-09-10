import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import pandas as pd


# #Практика
# #Блок 1(bar, barh)

# # cities = ["Москва", "СПб", "Казань", "Ярославль", "Сочи"]
# # sales = [120, 95, 60, 75, 140]


# # plt.bar(cities, sales, color='pink', edgecolor='black')
# # plt.xlabel('Города')
# # plt.ylabel('Продажи')
# # plt.title('Показатель продаж для городов')
# # plt.grid(axis="y")

# # plt.show()


# # cities = ["Москва", "СПб", "Казань", "Ярославль", "Сочи"]
# # sales = [120, 95, 60, 75, 140]


# # plt.barh(cities, sales, color='pink', edgecolor='black')
# # plt.xlabel('Города')
# # plt.ylabel('Продажи')
# # plt.title('Показатель продаж для городов')
# # plt.grid(axis="y")

# # plt.show()



# # months = ["Янв", "Фев", "Мар", "Апр", "Май"]

# # income = [40, 55, 60, 70, 90]
# # expenses = [35, 45, 52, 65, 75]

# # fig = plt.figure(figsize=(7, 4))
# # gs = GridSpec(nrows=1, ncols=2, figure=fig)

# # ax1 = plt.subplot(gs[0])
# # ax1.bar(months, income, color='pink', edgecolor='black')
# # plt.ylabel('income')

# # ax2 = plt.subplot(gs[1])
# # ax2.bar(months, expenses, color = 'green', edgecolor='black')
# # plt.ylabel('expenses')

# # plt.show()


# #Блок 2(hist)

# # scores = [45, 52, 61, 67, 68, 70, 71, 73, 74, 75,
# #           76, 77, 78, 79, 80, 81, 83, 84, 85, 90,
# #           91, 92, 95, 97, 98]

# # plt.hist(scores, bins=5, edgecolor='black', color='pink')
# # plt.grid()
# # plt.title('Распределение по возрасту')

# # plt.show()



# # numbers = np.random.normal(50, 10, 500)

# # fig = plt.figure()
# # gs = GridSpec(nrows=1, ncols=3, figure=fig)
# # ax1 = fig.add_subplot(gs[0])
# # ax1.hist(numbers, bins=5)

# # ax2 = fig.add_subplot(gs[1])
# # ax2.hist(numbers, bins=15)

# # ax3 = fig.add_subplot(gs[2])
# # ax3.hist(numbers, bins=30)

# # plt.show()


# #Блок 3(boxplot)


# # heights = [168,170,171,172,173,174,175,176,177,178,180,182,200]

# # plt.boxplot(heights)
# # plt.grid()
# # plt.show() #выбросом будет 200


# # male = [170,172,174,175,176,178,180,181,182,185]
# # female = [158,160,162,163,165,166,167,168,170,172]

# # fig = plt.figure()
# # gs = GridSpec(nrows=1, ncols=2, figure=fig)

# # ax1 = fig.add_subplot(gs[0])
# # ax1.boxplot(male)
# # ax1.grid()
# # plt.title('Boxplot height male')

# # ax2 = fig.add_subplot(gs[1])
# # ax2.boxplot(female)
# # ax2.grid('Boxplot height female')
# # plt.title('Boxplot height female')

# # plt.show()


# #Блок 4(tight layout)

# fig = plt.figure()
# gs = GridSpec(nrows=2, ncols=2, figure=fig)

# ax1 = fig.add_subplot(gs[0, 0])
# ax1.plot(np.arange(10))
# ax1.grid()
# plt.title('Plot')

# ax2 = fig.add_subplot(gs[0, 1])
# ax2.bar(np.arange(10), 10)
# ax2.grid()
# plt.title('Bar')

# ax1 = fig.add_subplot(gs[1, 0])
# ax1.hist(np.arange(10))
# ax1.grid()
# plt.title('Hist')

# ax1 = fig.add_subplot(gs[1, 1])
# ax1.boxplot(np.arange(10))
# ax1.grid()
# plt.title('Boxplot')
# plt.tight_layout()

# # plt.show() #мне лень для каждого графика придумывать данные

# #9 задание лень

# plt.savefig(
#     "dashboard.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()



months = ["Янв", "Фев", "Мар", "Апр", "Май"]

income = [40, 55, 60, 70, 90]
expenses = [35, 45, 52, 65, 75]

x = np.arange(len(months)) 
plt.bar(x - 0.2, income, width=0.4) 
plt.bar(x + 0.2, expenses, width=0.4) 
plt.xticks(x, months)

plt.show()