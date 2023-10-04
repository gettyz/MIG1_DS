import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение нашей функции
def f(x, y):
    return (np.cos(x))**2 + (np.sin(y))**2

# Функция для вычисления градиента
def grad(x, y):
    df_dx = derivative(func=lambda x: f(x, y), x0 = x, dx = 1e-6)
    df_dy = derivative(func=lambda y: f(x, y), x0 = y, dx = 1e-6)
    return np.array([df_dx, df_dy])

# Функция для метода градиентного спуска
def grad_descent(start, learning_rate, num_iterations):
    points = [start]
    for _ in range(num_iterations):
        current_point = points[-1]
        gradient = grad(current_point[0], current_point[1])
        next_point = current_point - learning_rate * gradient
        points.append(next_point)
    return np.array(points)

# Создаем диапазон значений и выполните градиентный спуск
x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
start = np.array([3, 3])
points = grad_descent(start, learning_rate=0.1, num_iterations=100)

# Создание сетки значений (x, y, f(x, y))
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Визуализация в 3D
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)
ax.scatter(points[:,0], points[:,1], f(points[:,0], points[:,1]), c='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
ax.set_title('3D визуализация градиентного спуска')

plt.show()
