# импорт модулей
import time
import matplotlib.pyplot as plt

# Определение первой функции с сохранением результатов (мемоизацией)
def tribonacci_number_memo(n, tribonacci_numbers_cache={}):
    if n == 1 or n == 2:
        return 0  # два первых числа Трибоначчи равны нулю
    if n == 3:
        return 1  # третье число Трибоначчи равно единице
    if n in tribonacci_numbers_cache:
        return tribonacci_numbers_cache[n]  # если число уже было высчитано, возвращаем его значение из кэша
    # если значение не сохранено в кэше, вычисляем новое число Трибоначчи как сумму трёх предыдущих
    n_tribonacci_number = (
            tribonacci_number_memo(n - 1) + tribonacci_number_memo(n - 2) + tribonacci_number_memo(n - 3))
    # сохраняем рассчитанное значение в кэше для последующего использования
    tribonacci_numbers_cache[n] = n_tribonacci_number
    return n_tribonacci_number  # возвращаем рассчитанное число Трибоначчи

# Определение второй функции, которая не использует мемоизацию - она каждый раз рассчитывает значение заново
def tribonacci_number(n):
    if n == 1 or n == 2:
        return 0  # два первых числа Трибоначчи равны нулю
    if n == 3:
        return 1  # третье число Трибоначчи равно единице
    # если значение не сохранено в кэше, вычисляем новое число Трибоначчи как сумму трёх предыдущих
    return (tribonacci_number(n - 1) + tribonacci_number(n - 2) + tribonacci_number(n - 3))

# список чисел для тестов
test_numbers = [10, 20, 25, 30]

times_memo = []  # список для хранения замеров времени работы функции с мемоизацией
times_nonmemo = []  # список для хранения замеров времени работы функции без мемоизации

# рассчёт времени выполнения функций и запись результатов в соответствующие списки
for num in test_numbers:
    start_time = time.time()  # засекаем время
    tribonacci_number_memo(num)  # вызываем функцию с мемоизацией
    # запись результата в список: текущее время минус время начала выполнения
    times_memo.append(time.time() - start_time)

    # аналогично для функции без мемоизации
    start_time = time.time()
    tribonacci_number(num)
    times_nonmemo.append(time.time() - start_time)

# отрисовка графиков для двух подходов
plt.figure(figsize=(12, 8))  # размеры графика
plt.plot(test_numbers, times_memo, marker='o', linestyle='-', color='r', label='С мемоизацией')  # график для функции с мемоизацией
plt.plot(test_numbers, times_nonmemo, marker='o', linestyle='-', color='b', label='Без мемоизации')  # график для функции без мемоизации
plt.xlabel('n')  # подпись оси Х
plt.ylabel('Время (секунды)')  # подпись оси Y
plt.legend()  # отображение легенды
plt.title('Время выполнения функции Трибоначчи с мемоизацией и без')  # заголовок графика
plt.show()  # отображение графика
