def ways_to_reach_n(n):
    # Если точка 0 или 1, то только один способ добраться
    if n == 1 or n == 0:
        return 1
    # Если точка 2, то два способа добраться
    if n == 2:
        return 2
    # Создаем список с размером n+1 и заполняем его нулями
    ways = [0] * (n + 1)
    ways[0], ways[1], ways[2] = 1, 1, 2
    # Для каждой точки выше 2
    for i in range(3,n + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
    return ways[n]

#введите на какой шаг необходимо понять вариант
n = 10


#вывод
print('Количество путей для достижения точки', n, 'равно', ways_to_reach_n(n))