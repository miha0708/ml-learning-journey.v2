import numpy as np
import matplotlib.pyplot as plt


# x = np.arange(6, 12)
# y = np.array([1, 2, -6, 0, 4, 10])
# plt.plot(x, y)
# plt.show()

# plt.plot([1, 1, 5, 5, 1], [1, 5, 5, 1, 1]) #квадрат
# plt.show()

# x = np.arange(5)
# y2 = [x**2 for x in x]
# y = [x for x in x]
# plt.plot(x, y2, x, y) #пары x и y
# plt.grid() #график с сеткой
# plt.show()


# x = np.arange(5)
# y2 = [x**2 for x in x]
# y = [x for x in x]
# lines = plt.plot(x, y, '-.r', x, y2, '--g') #график будет вместо непрерывной линии вот таким ------, после каждого графика пишем формат
# #два графика с точка с чертой и просто черточками и красного и зеленого цвета
# #есть параметр color='g', который назначает всем графикам зеленый цвет и стоит выше всех по цвету, можно также #0000СС, (0, 0, 0)

# # print(lines) #[<matplotlib.lines.Line2D object at 0x000001BE96AF3B60>]
# # plt.setp(lines, linestyle=':') #изменили на график с точками

# lines = plt.plot(x, y, '-.ro', x, y2, '--gs') #буква o - маркер, на каждой координате будет стоять жирная точка в цвет графика
# #также можно букву s(square) - будет квадрат или отдельно в параметре marker
# # plt.setp(lines, marker='*') #теперь каждая координата будет отмечаться звездочкой
# lines = plt.plot(x, y, '-.ro', x, y2, '--gs', markerfacecolor='w') #белая заливка внутри, квадрат - [], кружок - (), вместо полной заливки
# plt.setp(lines[0], linestyle='-.', marker='s', markerfacecolor='w', linewidth=1)
# #линия пунктир, квадратик, белая заливка внутри, толщина линии 1


# x = np.arange(-2*np.pi, 2*np.pi, 0.1)
# y = np.cos(x)
# plt.plot(x, y)
# plt.fill_between(x, y, where=(y < 0), color='r', alpha=0.5) #заливка графика, косинусоида, вот от прямой y=0, до отклонения идет заливка и при y < 0
# plt.fill_between(x, y, where=(y > 0), color='g', alpha=0.5) #aplha - прозрачность

# plt.grid() 
# plt.show()


#Практика matplotlib + numpy

# import numpy as np

# x = np.arange(1, 8)
# y = np.array([3, 5, 4, 7, 8, 10, 9])

# plt.plot(x, y)
# plt.title('График') #заголовок
# plt.xlabel('Ось x')
# plt.ylabel('Ось y')
# plt.grid()

# plt.show()


# epochs = np.arange(1, 7)

# train_loss = np.array([1.2, 0.9, 0.7, 0.5, 0.35, 0.25])
# val_loss = np.array([1.3, 1.0, 0.85, 0.8, 0.82, 0.88])

# plt.plot(epochs, train_loss, '--ro', markerfacecolor='w', label='Потери') #название для легенды
# plt.plot(epochs, val_loss, '-.gs', markerfacecolor='w', label='Вес')
# plt.legend()
# plt.show()


# epochs = np.arange(1, 7)

# accuracy = np.array([0.60, 0.67, 0.73, 0.79, 0.83, 0.86])
# std = np.array([0.04, 0.03, 0.03, 0.02, 0.02, 0.015])

# plt.plot(epochs, accuracy, ':gs', markerfacecolor='w', label='Точность')
# plt.plot(epochs, std, '--ro', markerfacecolor='w', label='Стандартное отклонение')
# plt.legend()
# plt.xlabel('Эпоха')
# plt.ylabel('Значение')
# plt.fill_between(epochs,
#                  accuracy - std,
#                  accuracy + std,
#                  color='blue',
#                  alpha=0.3)

# plt.show()


#Практика matplotlib + pandas

import pandas as pd

# df = pd.DataFrame({
#     "day": [1, 2, 3, 4, 5, 6, 7],
#     "sales": [120, 150, 140, 170, 200, 190, 220]
# })

# df.plot('day', 'sales', xlabel='День', ylabel='Продажи', label='Продажи')
# plt.title('График продаж магазина за неделю')
# plt.show()


# df = pd.DataFrame({
#     "month": [1, 2, 3, 4, 5, 6],
#     "income": [40, 45, 50, 55, 60, 70],
#     "expenses": [35, 37, 42, 44, 48, 53]
# })

# df.plot(x='month', y=['income', 'expenses'], marker='o')
# plt.show()


df = pd.DataFrame({
    "epoch": [1, 2, 3, 4, 5, 6],
    "mean": [0.58, 0.65, 0.72, 0.78, 0.82, 0.85],
    "std": [0.05, 0.04, 0.03, 0.03, 0.02, 0.02]
})

df.plot('epoch', 'mean')
plt.fill_between(df['epoch'],
                 df['mean'] + df['std'],
                 df['mean'] - df['std'],
                 color='green',
                 alpha=0.3)

plt.show()