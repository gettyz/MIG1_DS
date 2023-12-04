import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11,w12]) #матрица 2x3
    weight2 = np.array([-1,1])    #вектор 1x3

    sum_hidden = np.dot(weight1, x)     #вычисляем сумму на входах нейронов скрытого слоя
    print('Значения сумм на нейронах скрытого слоя: '+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print('Значения на выходных нейронов скрытого слоя: '+str(out_hidden))

    sum_end = np.dot(weight2,out_hidden)
    y = act(sum_end)
    print('Выходное значение НС: '+str(y))

    return y

house = 1
rock = 0
attr = 1

res = go(house, rock, attr)
if res ==1:
    print('Ты мне нравишься')
else:
    print("Созвонимся")

N = 5
b = 3
x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for i in range(N)] + b
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for i in range(N)] - 0.1 + b
C2 = [x1, x2]

f = [0 + b, 1 + b]
w2 = 0.5
w3 = -b * w2
w = np.array([-w2, w2, w3])
for i in range(N):
    x = np.array([C1[0][i], C1[1][i], 1])
    y = np.dot(w, x)
    if y >= 0:
        print("Класс С1")
    else:
        print("Класс С2")
plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()


def act(x):
    return 0 if x <= 0 else 1
def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = [1, 1, -1.5]
    w2 = [1, 1, -0.5]
    w_hidden = np.array([w1, w2])
    w_out = np.array([-1, 1, -0.5])

    sum = np.dot(w_hidden, x)
    out = [act(x) for x in sum]
    out.append(1)
    out = np.array(out)

    sum = np.dot(w_out, out)
    y = act(sum)
    return y

C1 = [(1,0), (0,1)]
C2 = [(0,0), (1,1)]

print( go(C1[0]), go(C1[1]) )
print( go(C2[0]), go(C2[1]) )