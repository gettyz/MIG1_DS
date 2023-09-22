import pulp
import time
import numpy as np
import matplotlib.pyplot as plt
#Решение
start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += 400*x1 + 300*x2, "Функция цели"
problem += 2*x1+ 3*x2 <= 21, "1"
problem +=x1+x2<=10, "2"
problem +=2*x1+2*x2<=16, "3"
problem.solve()
print ("Итог:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)

print ("Прибыль:")
print(pulp.value(problem.objective))
stop = time.time()

print ("Время дейтсвия:")
print(stop- start)
#График
x1 = np.linspace(-1, 40, 100)
x2 = np.linspace(-1, 40, 100)

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-3,15)
plt.ylim(-3,15)

plt.plot(x1, (21 - 2*x1) / 3, label='2X1 + 3X2 <= 21', linestyle='dashed', color='blue')
plt.plot(x1, 10 - x1, label='X1 + X2 <= 10', linestyle='dashed', color='red')
plt.plot(x1, (16 - 2 * x1) / 2, label='2X1 + 2X2 <= 16', linestyle='dashed', color='gray')
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

plt.fill_between([0, 0, 3,8], [0, 7, 5, 0], color='lavender')

plt.arrow(0,0,  2.7,  2, head_width=0.4, head_length=0.8, ec='black', label='вектор')
x1_green = np.linspace(-3, 3, 100)
plt.plot(x1_green, -3/4 * x1_green, linestyle='-.', color='green', label='перпендикуляр')

plt.plot(8,0,'o', color='black')
plt.text(6,-1.5, 'max (8,0)')
plt.title('Задача 1')
plt.grid(True)
plt.legend()
plt.show()