import time
import matplotlib.pyplot as plt

# Определение первой функции с сохренением результатов(мемоизацией)
def tribonacci_number_memo(n, tribonacci_numbers_cache={}):
    if n == 1 or n == 2:
        return 0  # два первых числа Трибоначчи равны нулю
    if n == 3:
        return 1  # третье число Трибоначчи равно единице
    if n in tribonacci_numbers_cache:
        return tribonacci_numbers_cache[n]  # если число уже было высчитано, возвращаем его значение из кэша
    # иначе, вычисляем новое число Трибоначчи как сумму трёх предыдущих
    n_tribonacci_number = (
                tribonacci_number_memo(n - 1) + tribonacci_number_memo(n - 2) + tribonacci_number_memo(n - 3))
    tribonacci_numbers_cache[n] = n_tribonacci_number  # сохраним рассчитанное значение в кэше
    return n_tribonacci_number


# Определение второй функции без мемоизации
def tribonacci_number(n):
    if n == 1 or n == 2:
        return 0  # два первых числа Трибоначчи равны нулю
    if n == 3:
        return 1  # третье число Трибоначчи равно единице
    return (tribonacci_number(n - 1) + tribonacci_number(n - 2) + tribonacci_number(n - 3))  # иначе, вычисляем новое число Трибоначчи


test_numbers = [10, 20, 25, 30]

times_memo = []
times_nonmemo = []

# Для каждого числа тестового списка замеряем время выполнения обоих функций
for num in test_numbers:
    start_time = time.time()
    tribonacci_number_memo(num)
    times_memo.append(time.time() - start_time)

    start_time = time.time()
    tribonacci_number(num)
    times_nonmemo.append(time.time() - start_time)

plt.figure(figsize=(12, 8))
plt.plot(test_numbers, times_memo, marker='o', linestyle='-', color='r', label='С мемоизацией')
plt.plot(test_numbers, times_nonmemo, marker='o', linestyle='-', color='b', label='Без мемоизации')
plt.xlabel('n')
plt.ylabel('Время (секунды)')
plt.legend()
plt.title('Время выполнения функции Трибоначчи с мемоизацией и без')
plt.show()
