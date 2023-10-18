# Функция, которая вычисляет максимальную сумму подмассива в переданном массиве.
def max_sub_array(nums):
    # Создаем массив, в котором будет храниться сумма каждого подмассива, начиная с первого элемента.
    array_of_sums = [nums[0]]
    # Начальная максимальная сумма устанавливается как первый элемент массива.
    max_sum = nums[0]
    # Позиция максимальной субсуммы на данный момент.
    max_position = 0
    # Проходимся по оставшимся элементам.
    for i in range(1, len(nums)):
        # Если сумма с предыдущим подмассивом положительна, то продолжаем этот подмассив.
        if array_of_sums[i - 1] > 0:
            array_of_sums.append(array_of_sums[i - 1] + nums[i])
        # Если сумма с предыдущим подмассивом отрицательна, то начинаем новый подмассив.
        else:
            array_of_sums.append(nums[i])
        # Если текущая сумма больше максимальной, то обновляем максимальную сумму и его позицию.
        if array_of_sums[i] > max_sum:
            max_sum = array_of_sums[i]
            max_position = i
            
    # Если максимальная сумма - отрицательная
    # значит все элементы в массиве отрицательные
    # на каждом шаге сумма вычислялась заново, и array_of_sums равен nums
    # возвращаем максимальное из отрицательных чисел, оно будет в max_position
    if max_sum < 0:
        return [nums[max_position]]

    # Инициализация границ максимального подмассива.
    end_of_max_subarray = max_position
    start_of_max_subarray = end_of_max_subarray

    # Перемещаемся назад по массиву, чтобы найти начало этого подмассива.
    while start_of_max_subarray >= 0 and array_of_sums[start_of_max_subarray] >= 0:
        start_of_max_subarray -= 1

    # Возвращаем максимальный подмассив, используя Python slicing
    return nums[start_of_max_subarray + 1: end_of_max_subarray + 1]

# Исходный массив
source_array = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]
# Вызываем функцию и выводим результат.
# Вывод: [2, 2, -1, 3, -1, 2]
print(max_sub_array(source_array))

# Importing the matplotlib library for plotting
import matplotlib.pyplot as plt

# Модифицированная функция max_sub_array, которая также возвращает array_of_sums для демонстрации на графике.
def max_sub_array(nums):
    array_of_sums = [nums[0]]
    max_sum = nums[0]
    max_position = 0
    for i in range(1, len(nums)):
        if array_of_sums[i - 1] > 0:
            array_of_sums.append(array_of_sums[i - 1] + nums[i])
        else:
            array_of_sums.append(nums[i])
        if array_of_sums[i] > max_sum:
            max_sum = array_of_sums[i]
            max_position = i
            
    if max_sum < 0:
        return [nums[max_position]], array_of_sums
    
    end_of_max_subarray = max_position
    start_of_max_subarray = end_of_max_subarray
    while start_of_max_subarray >= 0 and array_of_sums[start_of_max_subarray] >= 0:
        start_of_max_subarray -= 1
    return nums[start_of_max_subarray + 1: end_of_max_subarray + 1], array_of_sums

# Исходный массив
source_array = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]

max_sub_array_values, arr_sums = max_sub_array(source_array)
# Вывод: [2, 2, -1, 3, -1, 2]
print(max_sub_array_values)

# Построение графиков исходного массива и подмассивов.
plt.plot(source_array, label = 'Исходный массив')
plt.plot(arr_sums, label = 'Сумма подмассивов', linestyle='--')
plt.title('Максимальный подмассив с наибольшей суммой')
plt.legend()
plt.grid(True)
plt.show()
