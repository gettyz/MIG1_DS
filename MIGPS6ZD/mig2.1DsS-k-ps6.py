import matplotlib.pyplot as plt
#основная функция
print('Введите первый прыжок')
a = int(input())
print('Введите второй прыжок')
b = int(input())
print('Введите третий прыжок')
c = int(input())
print('Введите кол-во прыжков')
N = int(input())


def solve(N):
    # список для хранения достижения цели
    dp = [0] * (N+1)
    dp[0] = dp[1] = 1
    dp[2] = 2

    # список для хранения стоимости достижения каждой точки
    cost = [0] * (N+1)
    cost[1] = 1
    cost[2] = 2
    cost[3] = 4

    # арифметическая прогрессия
    for i in range(3, N+1):
        dp[i] = dp[i-a] + dp[i-b] + dp[i-c]
        cost[i] = i * (i+1) // 2
#возврат данных
    return dp, cost


# значения входа
way_counts, costs = solve(N)


#визуализация кол-во способов
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(range(101), way_counts, marker="o", markersize=3)
plt.title('Количество способов достижения точки')
plt.xlabel('Точки')
plt.ylabel('Количество способов')


#визуализация цены
plt.subplot(122)
plt.plot(range(101), costs, marker="o", color="r", markersize=3)
plt.title('Стоимость достижения точки')
plt.xlabel('Точки')
plt.ylabel('Стоимость')

plt.tight_layout()
plt.show()