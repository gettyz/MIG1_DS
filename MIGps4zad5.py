import pulp

problem = pulp.LpProblem("Задача о ZP2", pulp.LpMaximize)

#x1 и x2
x1 = pulp.LpVariable("x1", lowBound=1)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)

#функция цели
problem += x1 + 2 * x2 + x4 + x5, "Функция цели"

# добавляем ограничения
problem +=  (-2)*x1 + (-1)* x2 + (-1 )* x3 == -1, "1"
problem += x2 + x4 == 6, "2"
problem += x1 + x2 + (-1)* x5 == 25, "3"
problem.solve()

# выводим результат
print("Оптимальные значения: x1 =", x1.varValue, "x2 =", x2.varValue, "x3 =", x3.varValue, "x4 =", x4.varValue, "x5 =", x5.varValue)
print("Оптимальное значение целевой функции:", pulp.value(problem.objective))
if  pulp.value(problem.objective) == 0:
    print('функция в бесконечность')
else:
    print(pulp.value(problem.objective))



problem = pulp.LpProblem("Задача о ZP1", pulp.LpMaximize)

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



