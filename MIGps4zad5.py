import pulp

problem = pulp.LpProblem("Задача о ZP", pulp.LpMaximize)

#x1 и x2
x1 = pulp.LpVariable("x1", lowBound=1)
x2 = pulp.LpVariable("x2", lowBound=0)

#функция цели
problem += 3 * x1 + 4 * x2, "Функция цели"

# добавляем ограничения
problem += 3 * x1 + 2 * x2 >= 6, "1"
problem += 3 * x1 + (-2) * x2 >= (-7), "2"
problem += 2 * x1 + (-4) * x2 <= 8, "3"
problem += x1 >=1, "4"
problem.solve()

# выводим результат
print("Оптимальные значения: x1 =", x1.varValue, "x2 =", x2.varValue)
print("Оптимальное значение целевой функции:", pulp.value(problem.objective))
if  pulp.value(problem.objective) == 0:
    print('функция в бесконечность')
else:
    print('все супер ответ:' + pulp.value(problem.objective) + 'верен')
