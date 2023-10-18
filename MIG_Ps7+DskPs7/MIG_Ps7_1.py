# Импортируем библиотеку matplotlib для визуализации данных
import matplotlib.pyplot as plt

# Инициализируем начальные значения для чисел Трибоначчи (0, 0, 1)
tribonacci_numbers_cache = [0, 0, 1]

# Заполняем список tribonacci_numbers_cache числами Трибоначчи до 100-го числа
# Здесь число Трибоначчи определяется как сумма трех предыдущих чисел в последовательности
for i in range(3, 100):
    tribonacci_numbers_cache.append(
        tribonacci_numbers_cache[i - 1]
        + tribonacci_numbers_cache[i - 2]
        + tribonacci_numbers_cache[i - 3]
    )

# Уже заданная нами конкретная последовательность чисел Трибоначчи, значения которых нам нужно найти
tribonacci_numbers = [73, 10, 4, 15, 20, 7]

# Создаем пустой список для сохранения значений заданных чисел Трибоначчи
tribonacci_numbers_value = []

# Поочередно перебираем каждое число из списка tribonacci_numbers
for number in tribonacci_numbers:
    # Получаем значение текущего числа из нашего ранее созданного кэша чисел Трибоначчи
    tribonacci_numbers_value.append(tribonacci_numbers_cache[number - 1])

# Выводим значения чисел Трибоначчи из списка
print('список значений Трибоначчи: ', tribonacci_numbers_value)

# Начинаем визуализировать наши данные
plt.figure(figsize=(10, 5))

# Используем функцию plot для создания графика, где x-осью являются числа Трибоначчи, а y-осью - их значения
# Tuning the parameters like marker, linestyle and color for better visibility
plt.plot(tribonacci_numbers, tribonacci_numbers_value, marker='o', linestyle='-', color='b')

# Задаем заголовок для графика
plt.title('Значения Трибоначчиевых чисел')

# Задаем название для оси X
plt.xlabel('Трибоначчиевы числа')

# Задаем название для оси Y
plt.ylabel('Значения')

# Добавляем сетку для удобства чтения графика
plt.grid(True)

# Выводим график на экран
plt.show()
