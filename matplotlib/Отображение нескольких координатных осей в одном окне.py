import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np


#чтобы отобразить несколько графиков существует функция subplot(nrows, ncols, index)
#nrow, ncols - число строк и столбцов
#index - индекс текущих координатных осей


# ax1 = plt.subplot(1, 3, 1) #1 ряд, 3 графика в ряду, первый индекс
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# ax3 = plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10)) #[0.08590086 0.87168218 0.98675631 0.73283324 0.93031517 0.1814074 0.68062951 0.12596886 0.48055635 0.56221369]

# ax1.grid()
# ax2.grid()
# ax3.grid()
# plt.show()

#если хотим сделать 2 строки, а снизу 1 общий график
# ax1 = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
# ax3 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
# ax4 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))

# plt.show()


#если много графиков надо, то лучше использовать функцию subplots(nrows, ncols)

# f, ax = plt.subplots(2, 2) #разбивка на 2 строки и 2 столбца
# #f - фигура(область, где все графики), ax - список координатных осей
# #можно изменять свойства фигуры
# f.set_size_inches(10, 10)
# f.set_facecolor('green')

# ax[0, 0].plot(np.arange(1, 10, 0.5)) #верний левый угол, только 1 график
# ax[0, 0].grid()
# ax[0, 1].plot([1, 3, 4, 9], [5, 6, 0.3, 2], '--ro', markerfacecolor='w')
# ax[0, 1].grid()

# plt.show()


#можно также создавать еще 1 фигуру

# fig = plt.figure(figsize=[10, 10])
# # plt.plot(np.arange(1, 10, 1)) можно создать график так

# # ax1 = fig.add_axes([0, 0, 1, 1]) #или так. начало координат x, y, доля по высоте и ширине(от 0 до 1)
# # ax1.plot(np.random.random(10), ':go', markerfacecolor='w') или так

# ax1 = fig.add_subplot(1, 3, 1) #так тоже можно
# ax1.plot(np.random.random(10), ':go', markerfacecolor='w')

# plt.show()


#Компоновка графиков с помощью GridSpec

#сначала импортируем from matplotlib.gridspec import GridSpec
#потом создаем фигуру

# ws = [1, 1, 3]
# hs = [2, 1]

# fig = plt.figure()
# gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs) #3 столбца и 2 строки


# #можно добавлять и через subplot и через add_subplot
# ax1 = plt.subplot(gs[0, 0:2])
# ax1.plot(np.random.random(10), '--go', markerfacecolor='w')
# ax2 = fig.add_subplot(gs[1, 0:2])
# ax2.plot(np.random.random(10), '-.ro', markerfacecolor='w')
# ax3 = fig.add_subplot(gs[:, 2])
# ax3.plot(np.random.random(10), ':yo', markerfacecolor='w')

# plt.show()


#Практика

# fig = plt.figure()
# gs = GridSpec(nrows=2, ncols=2, figure=fig)

# ax1 = fig.add_subplot(gs[0, :])
# ax1.plot(np.arange(10), '--ro', markerfacecolor='w')

# ax2 = fig.add_subplot(gs[1, 0])
# ax2.plot(np.arange(10), '-.go', markerfacecolor='w')

# ax3 = fig.add_subplot(gs[1, 1])
# ax3.plot(np.arange(10), ':yo', markerfacecolor='w')

# plt.show()



# fig = plt.figure()
# gs = GridSpec(nrows=2, ncols=2)

# ax1 = fig.add_subplot(gs[:, 0])
# ax1.plot(np.arange(10), '--ro')

# ax2 = fig.add_subplot(gs[0, 1])
# ax2.plot(np.arange(10), '-.ro')

# ax3 = fig.add_subplot(gs[1, 1])
# ax3.plot(np.arange(10), ':ro')

# plt.show()


fig = plt.figure()
gs = GridSpec(nrows=5, ncols=5, figure=fig)

ax1 = fig.add_subplot(gs[0:2, 0:2])
ax1.plot(np.arange(10))

ax2 = fig.add_subplot(gs[0, 2])
ax2.plot(np.arange(10))

ax3 = fig.add_subplot(gs[0, 3])
ax3.plot(np.arange(10))

ax4 = fig.add_subplot(gs[3, 0:3])
ax4.plot(np.arange(10))

ax5 = fig.add_subplot(gs[1:4, 3])
ax5.plot(np.arange(10))

plt.show()

