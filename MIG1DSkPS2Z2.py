import pulp
import time
import numpy as np
import matplotlib.pyplot as plt

#Задача
start = time.time()
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

#maximum
problem_max = pulp.LpProblem('0_max', pulp.LpMaximize)
problem_max += x - 2 * y, "Функция цели"
problem_max += 5 * x + 3 * y >= 30, "1"
problem_max += x - y <= 3, "2"
problem_max += -3 * x + 5 * y <= 15, "3"
problem_max.solve()

print("Результат для макс.:")
for variable in problem_max.variables():
    print(variable.name, "=", variable.varValue)

print("Max:")
print(pulp.value(problem_max.objective))

# minimum
problem_min = pulp.LpProblem('0_min', pulp.LpMinimize)
problem_min += x - 2 * y, "Функция цели"
problem_min += 5 * x + 3 * y >= 30, "1"
problem_min += x - y <= 3, "2"
problem_min += -3 * x + 5 * y <= 15, "3"
problem_min.solve()

print("Результат для мин.:")
for variable in problem_min.variables():
    print(variable.name, "=", variable.varValue)

print("Min:")
print(pulp.value(problem_min.objective))

stop = time.time()
print("Время :")
print(stop - start)

#График
x1 = np.linspace(-5, 40, 100)
x2 = np.linspace(-5, 40, 100)

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-3,20)
plt.ylim(-3,20)

plt.plot(x1, (30 - 5*x1) / 3, label='5x + 3y >= 30', linestyle='dashed', color='black')
plt.plot(x1, x1-3, label='x - y <= 3', linestyle='dashed', color='grey')
plt.plot(x1, (15 + 3 * x1) / 5, label='-3x + 5y <= 15', linestyle='dashed', color='purple')
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

plt.fill_between([3.075, 4.87, 15, 3.075], [4.84, 1.874, 12, 4.84], color='lavender')

plt.arrow(0,0 ,1,-2, head_width=0.3, head_length=0.6, ec='black', label='вектор')
x1_green = np.linspace(-3, 3, 100)
plt.plot(x1_green, 1/2 * x1_green, linestyle='-.', color='green', label='перпендикуляр')

plt.plot(4.87,1.874,'o', c='red')
plt.text(6,1.874, 'max')
plt.plot(15,12,'o', c='blue')
plt.text(16,12, 'min')
plt.title('Задача 2')
plt.grid(True)
plt.legend()
plt.show()
