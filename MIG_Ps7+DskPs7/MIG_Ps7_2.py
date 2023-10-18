# Импорт модуля matplotlib.pyplot для построения графиков.
import matplotlib.pyplot as plt

# Определение функции max_sub_array. Функция принимает список чисел и возвращает подмассив,
# имеющий максимальную сумму, и список сумм.
def max_sub_array(nums):
    # Инициализация списка array_of_sums первым элементом входного массива и
    # переменных max_sum и max_position его индексом и значением.
    array_of_sums = [nums[0]]
    max_sum = nums[0]
    max_position = 0

    # Обход данных начиная со второго элемента
    for i in range(1, len(nums)):
        # Если предыдущая сумма на позиции i - 1 была положительна, добавляем к ней текущее число.
        if array_of_sums[i - 1] > 0:
            array_of_sums.append(array_of_sums[i - 1] + nums[i])
        else:
            # Если предыдущая сумма не была положительной, то начинаем подсчёт суммы заново с текущего числа.
            array_of_sums.append(nums[i])
        # Если текущая сумма больше максимальной, обновляем максимальную сумму и ее позицию.
        if array_of_sums[i] > max_sum:
            max_sum = array_of_sums[i]
            max_position = i

    # Если все числа в массиве отрицательные, возвращаем максимальное из них и список сумм.
    if max_sum < 0:
        return [nums[max_position]], array_of_sums

    end_of_max_subarray = max_position
    start_of_max_subarray = end_of_max_subarray
    # Находим начало подмассива с максимальной суммой.
    while start_of_max_subarray >= 0 and array_of_sums[start_of_max_subarray] >= 0:
        start_of_max_subarray -= 1

    # Возвращаем подмассив с максимальной суммой и список сумм.
    return nums[start_of_max_subarray + 1: end_of_max_subarray + 1], array_of_sums



# Определение исходного массива.
source_array = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]

# Вызов функции max_sub_array и получение нужного подмассива и списка сумм.
max_sub_array_values, arr_sums = max_sub_array(source_array)

# Вывод подмассива с наибольшей суммой.
print('подмассив с наибольшей суммой: ', max_sub_array_values)

# Построение графика для исходного массива и массива сумм.
# Line plot для исходного массива, и dashed line для сумм подмассивов.
plt.plot(source_array, label='Исходный массив')
plt.plot(arr_sums, label='Сумма подмассивов', linestyle='--')

# Название графика и легенды.
plt.title('Максимальный подмассив с наибольшей суммой')
plt.legend()

# Включение сетки на графике.
plt.grid(True)

# Вывод графика.
plt.show()
