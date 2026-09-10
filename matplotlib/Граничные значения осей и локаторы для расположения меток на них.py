import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator
import numpy as np


#Граничные значения создаются благодаря методу set()
#ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

# fig = plt.figure(figsize=(7, 4))
# ax1 = fig.add_subplot()
# ax1.plot(np.arange(10))

# # ax1.set(xlim=(1, 5), ylim=(2, 3)) #теперь будет отображаться нужный нам кусочек графика

# ax1.set_xlim(1, 50) #или можно так задать границы
# ax1.set_ylim(ymin=2) #или только 1 парметр

# plt.grid()
# plt.show()



#Метки для графиков

# set_major_locator() – управление рисками крупной сетки
# set_minor_locator() - управление рисками мелкой сетки
# matplotlib.ticker.Locator
# from matplotlib.ticker import NullLocator

#NullLocator()
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(10))
# plt.grid()
# ax.xaxis.set_major_locator(NullLocator()) #пропали линии по оси x, теперь график с полосками вместо сетки и ось x пропала

# plt.show()


#LinearLocator()
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(10))
# plt.grid()
# ax.xaxis.set_major_locator(LinearLocator(5)) #взяли ровно 5 меток по оси x
# plt.show()


#MultipleLocator
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(10))

# plt.grid()
# ax.xaxis.set_major_locator(MultipleLocator(base=2)) #шаг по оси x будет равным base
# plt.show()


# IndexLocator()
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))

# plt.grid()
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57)) #шаг по оси x будет равным base, а смещение будет 0.57
# plt.show()


#FixedLocator()
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))

# plt.grid()
# ax.xaxis.set_major_locator(FixedLocator([-2, 0, 1, 2])) #список рисок которые мы хотим увидеть по оси x
# plt.show()


#LogLocator
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))

# plt.grid()
# ax.xaxis.set_major_locator(LogLocator(base=2)) #риски откладываются в логарифмическом масштабе(0.5 1 2 и тд)
# plt.show()


#MaxNLocator
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))


# ax.minorticks_on()
# ax.grid(which='major', lw=2) #мажорная 2 пикселя толщина
# ax.grid(which='minor') #минорная с толщиной пиксель
# ax.xaxis.set_minor_locator(NullLocator()) #максимум 5 рисок, ушла маленькая(минорная сетка) по оси x

# # ax.xaxis.set_major_locator(MaxNLocator(5)) #максимум 5 рисок
# plt.show()