import matplotlib.pyplot as plt
tribonacci_numbers_cache = [0, 0, 1]
for i in range(3, 100):
    tribonacci_numbers_cache.append(
        tribonacci_numbers_cache[i - 1]
        + tribonacci_numbers_cache[i - 2]
        + tribonacci_numbers_cache[i - 3]
    )

tribonacci_numbers = [73, 10, 4, 15, 20, 7]
# список для сохранения самих чисел трибонначи
tribonacci_numbers_value = []
for number in tribonacci_numbers:
    # просто получаем значения из кеша, не делая никаких вычислений
    tribonacci_numbers_value.append(tribonacci_numbers_cache[number - 1])

print(tribonacci_numbers_value)

# Визуализация
plt.figure(figsize=(10, 5))
plt.plot(tribonacci_numbers, tribonacci_numbers_value, marker='o', linestyle='-', color='b')
plt.title('Значения Трибоначчиевых чисел')
plt.xlabel('Трибоначчиевы числа')
plt.ylabel('Значения')
plt.grid(True)
plt.show()
