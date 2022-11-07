print("*" * 40)
print('Exersice 4')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
# корректировка окна графика
ax.set_xlim((-50, 50))
ax.set_ylim((-50, 50))
ax.set_aspect("equal") #область построения остаётся такой же, независимо от размера окна
ax.grid() #добавление сетки
# ax.set_title("Парабола") #добавление названия графику
ax.set_xlabel('x') #добавление названия оси
ax.set_ylabel('y')
x = np.linspace(0, 50)
k = 1
k2 = 5
plt.plot(x, np.cos(k * x),'r-',x, np.cos(k2 * x),'b--')
# x = np.linspace(-5, 5, 100)
# y = x ** 2 #парабола
# # y = np.sin(x) #cинусоида
# # y = np.exp(x) #экспонента
# # y = x ** 2 + 5 * np.sin(x)
# ax.plot(x, y)
plt.show()
