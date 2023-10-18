# Импортирование библиотеки для визуализации данных
import matplotlib.pyplot as plt

# Следующая функция используется для нахождения подмассива с максимальной суммой
# в массиве чисел с использованием алгоритма Кадана
def max_sub_array(nums):
    # Инициализация переменных для хранения текущей и максимальной суммы
    array_of_sums = [nums[0]]
    max_sum = nums[0]
    max_position = 0

    # Цикл для перебора каждого элемента в массиве.
    # Если текущая сумма отрицательна, она сбрасывается до нуля.
    # Если текущая сумма больше максимальной, она становится новой максимальной суммой.
    for i in range(1, len(nums)):
        if array_of_sums[i - 1] > 0:
            array_of_sums.append(array_of_sums[i - 1] + nums[i])
        else:
            array_of_sums.append(nums[i])
        if array_of_sums[i] > max_sum:
            max_sum = array_of_sums[i]
            max_position = i

    # Если все числа в массиве отрицательные, возвратить максимальное из них.
    if max_sum < 0:
        return [nums[max_position]], array_of_sums

    end_of_max_subarray = max_position
    start_of_max_subarray = end_of_max_subarray
    # Находим начало подмассива с максимальной суммой.
    while start_of_max_subarray >= 0 and array_of_sums[start_of_max_subarray] >= 0:
        start_of_max_subarray -= 1

    # Результатом функции является подмассив с максимальной суммой, а также массив сумм.
    return nums[start_of_max_subarray + 1: end_of_max_subarray + 1], array_of_sums

# Исходный массив.
source_array = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]

# Использование функции для нахождения подмассива с наибольшей суммой.
max_sub_array_values, arr_sums = max_sub_array(source_array)
print('подмассив с наибольшей суммой: ', max_sub_array_values)

# Находим позицию максимальной суммы
max_sum_position = arr_sums.index(max(arr_sums))

# Создаем список цветов, в котором все элементы красные, кроме элемента на позиции максимальной суммы
colors = ['red' if i != max_sum_position else 'green' for i in range(len(arr_sums))]

# Визуализация подмассива с максимальной суммой с помощью бар-графика
plt.bar(range(len(arr_sums)), arr_sums, color=colors)

# Название диаграммы и меток осей.
plt.title('Гистограмма сумм подмассивов')
plt.xlabel('Позиция элемента')
plt.ylabel('Сумма подмассива на данной позиции')

# Включение сетки на графике
plt.grid(True)

# Вывод графика на экран.
plt.show()
