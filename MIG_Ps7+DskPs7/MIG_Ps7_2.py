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

    # Если максимальная сумма - отрицательная
    # значит все элементы в массиве отрицательные
    # на каждом шаге сумма вычислялась заново, и array_of_sums равен nums
    # возвращаем максимальное из отрицательных чисел, оно будет в max_position
    if max_sum < 0:
        return [nums[max_position]]

    end_of_max_subarray = max_position
    start_of_max_subarray = end_of_max_subarray

    # надо учесть, что можем дойти до начала массива
    while start_of_max_subarray >= 0 and array_of_sums[start_of_max_subarray] >= 0:
        start_of_max_subarray -= 1

    # i + 1, т.к. цикл завершится на отрицательном элементе
    # который не нужно суммировать,
    # либо вне границ массива (в -1 позиции)
    # end_of_max_subarray + 1, т.к. последний элемент не включается в slice
    return nums[start_of_max_subarray + 1: end_of_max_subarray + 1]


source_array = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]
# будет выведено [2, 2, -1, 3, -1, 2]
print(max_sub_array(source_array))

import matplotlib.pyplot as plt

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
        return [nums[max_position]]
    end_of_max_subarray = max_position
    start_of_max_subarray = end_of_max_subarray
    while start_of_max_subarray >= 0 and array_of_sums[start_of_max_subarray] >= 0:
        start_of_max_subarray -= 1
    return nums[start_of_max_subarray + 1: end_of_max_subarray + 1], array_of_sums

source_array = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]

max_sub_array_values, arr_sums = max_sub_array(source_array)
# будет выведено [2, 2, -1, 3, -1, 2]
print(max_sub_array_values)

plt.plot(source_array, label = 'Исходный массив')
plt.plot(arr_sums, label = 'Сумма подмассивов', linestyle='--')
plt.title('Максимальный подмассив с наибольшей суммой')
plt.legend()
plt.grid(True)
plt.show()
