import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein


#НАШ КОД ТИП 1
# Время старта выполнения кода
start_time = time.perf_counter_ns()
def levenshtein_percentage(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    levenshtein_distance = current_row[n]
    max_length = max(len(str_1), len(str_2))
    similarity_percentage = ((max_length - levenshtein_distance) / max_length) * 100

    return similarity_percentage
print("процент схожести для нашего кода в первом типе:")
print(levenshtein_percentage('Привет мир', 'Привт кир'))


# время окончания выполнения кода
end_time = time.perf_counter_ns()
print(f"Время выполнения нашего кода: {end_time - start_time} милисекунд.")


#ПЕРВЫЙ ТИП
# Время старта выполнения кода
start_time = time.perf_counter_ns()
a = fuzz.ratio('Привет мир', 'Привт кир')
print(f"Первый тип: {a} .")
end_time = time.perf_counter_ns()
print(f"Время выполнения первого типа: {end_time - start_time} милисекунд.")




#ВТОРОЙ ТИП
# Время старта выполнения кода
start_time = time.perf_counter_ns()
a = fuzz.partial_ratio('Привет мир', 'Привт кир!')
print(f"Второй тип: {a} .")
end_time = time.perf_counter_ns()
print(f"Время выполнения второго типа: {end_time - start_time} милисекунд.")

#НАШ КОД ТИП 2
start_time = time.perf_counter_ns()
def levenshtein_similarity(str_1, str_2):
    len_str_1, len_str_2 = len(str_1), len(str_2)
    if len_str_1 == 0:
        return 0
    if len_str_2 == 0:
        return 0

    matrix = [[0 for _ in range(len_str_2 + 1)] for _ in range(len_str_1 + 1)]

    for i in range(len_str_1 + 1):
        matrix[i][0] = i

    for j in range(len_str_2 + 1):
        matrix[0][j] = j

    for i in range(1, len_str_1 + 1):
        for j in range(1, len_str_2 + 1):
            cost = 0 if str_1[i - 1] == str_2[j - 1] else 1
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)

    max_length = max(len_str_1, len_str_2)
    levenshtein_distance = matrix[len_str_1][len_str_2]
    similarity_percentage = ((max_length - levenshtein_distance) / max_length) * 100

    return similarity_percentage
print("процент схожести для нашего кода во втором типе:")
print(levenshtein_similarity('Привет мир', 'Привт кир'))

end_time = time.perf_counter_ns()
print(f"Время выполнения нашего кода во втором типе: {end_time - start_time} милисекунд.")


# Время старта выполнения кода
start_time = time.perf_counter_ns()
a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(f"Третий тип: {a} .")
end_time = time.perf_counter_ns()
print(f"Время выполнения третьего типа: {end_time - start_time} милисекунд.")
#НАШ КОД ТИП 3
start_time = time.perf_counter_ns()
def levenshtein_token_sort_ratio(str_1, str_2):
    # Разбиваем строки на слова и переводим их в нижний регистр
    tokens_1 = str_1.lower().split()
    tokens_2 = str_2.lower().split()

    # Сортируем слова в каждой из строк
    tokens_1.sort()
    tokens_2.sort()

    # Преобразуем отсортированные слова обратно в строки
    sorted_str_1 = ' '.join(tokens_1)
    sorted_str_2 = ' '.join(tokens_2)

    # Рассчитываем близость Левенштейна для отсортированных строк
    n, m = len(sorted_str_1), len(sorted_str_2)
    if n > m:
        sorted_str_1, sorted_str_2 = sorted_str_2, sorted_str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if sorted_str_1[j - 1] != sorted_str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    levenshtein_distance = current_row[n]
    max_length = max(len(sorted_str_1), len(sorted_str_2))
    similarity_percentage = ((max_length - levenshtein_distance) / max_length) * 100

    return similarity_percentage

print("процент схожести для нашего кода в третьем типе:")
print(levenshtein_token_sort_ratio('Привет мир', 'мир привет'))

end_time = time.perf_counter_ns()
print(f"Время выполнения нашего кода 3 типа: {end_time - start_time} милисекунд.")

start_time = time.perf_counter_ns()
a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(f"Четветрый тип: {a} .")
end_time = time.perf_counter_ns()
print(f"Время выполнения четветого типа: {end_time - start_time} милисекунд.")

#НАШ КОД 4 ТИП
# Время старта выполнения кода
start_time = time.perf_counter_ns()
def token_set_ratio(str_1, str_2):
    # Разбиваем строки на множества слов и переводим их в нижний регистр
    tokens_1 = set(str_1.lower().split())
    tokens_2 = set(str_2.lower().split())

    # Находим общие слова
    common_tokens = tokens_1.intersection(tokens_2)

    # Рассчитываем близость как отношение общих слов к общему количеству слов в двух строках
    if len(tokens_1) + len(tokens_2) == 0:
        return 100.0
    similarity_percentage = (len(common_tokens) / (len(tokens_1) + len(tokens_2))) * 100.0

    return similarity_percentage


print("процент схожести для нашего кода в 4 типе:")
print(token_set_ratio('Привет мир', 'мир Привет'))

end_time = time.perf_counter_ns()
print(f"Время выполнения нашего кода 4 типа: {end_time - start_time} милисекунд.")



#5 тип
start_time = time.perf_counter_ns()
a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(f"5 тип: {a} .")
end_time = time.perf_counter_ns()
print(f"Время выполнения 5 типа: {end_time - start_time} милисекунд.")

#НАШ КОД ТИП 5
start_time = time.perf_counter_ns()
def w_ratio(str_1, str_2):
    # Переводим строки в нижний регистр
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    # Разбиваем строки на слова
    words_1 = str_1.split()
    words_2 = str_2.split()

    # Создаем множества слов
    set_1 = set(words_1)
    set_2 = set(words_2)

    # Находим общие слова
    common_words = set_1.intersection(set_2)

    # Рассчитываем близость как отношение общих слов к общему количеству слов в двух строках
    if len(set_1) + len(set_2) == 0:
        return 100.0
    similarity_percentage = (len(common_words) / (len(set_1) + len(set_2))) * 100.0

    return similarity_percentage

print("процент схожести для нашего кода в 5 типе:")
print(w_ratio('Привет мир', 'мир Привет'))

end_time = time.perf_counter_ns()
print(f"Время выполнения нашего кода 5ю типа: {end_time - start_time} милисекунд.")


#6 тип
start_time = time.perf_counter_ns()
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city, limit=2)
# Параметр limit по умолчанию имеет значение 5
print(f"6 тип: {a} .")
end_time = time.perf_counter_ns()
print(f"Время выполнения 6 типа: {end_time - start_time} милисекунд.")

#НАШ КОД ТИП 6
start_time = time.perf_counter_ns()
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def find_best_matches(query, options, limit=2):
    distances = []
    for option in options:
        distance = levenshtein_distance(query, option)
        distances.append((option, distance))

    distances.sort(key=lambda x: x[1])
    best_matches = distances[:limit]
    return best_matches

cities = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
query = "Саратов"

result = find_best_matches(query, cities)
print("процент схожести для нашего кода в 6 типе:")
print(result)

end_time = time.perf_counter_ns()
print(f"Время выполнения нашего кода 6 типа: {end_time - start_time} милисекунд.")


print('     ')
print('библиотека python-Levenshtein')

#python-Levenshtein

start_time = time.perf_counter_ns()
print("тип 1")
str1 = 'Привет мир'
str2 = 'Привет мир'

similarity_ratio = 100 - Levenshtein.distance(str1, str2)
print(similarity_ratio)
end_time = time.perf_counter_ns()
print(f"Время выполнения 1 типа: {end_time - start_time} милисекунд.")

start_time = time.perf_counter_ns()
print("тип 2")
def partial_ratio(str1, str2):
    shorter, longer = (str1, str2) if len(str1) <= len(str2) else (str2, str1)

    m1 = len(shorter)
    m2 = len(longer)
    partial_ratio = 100 * (m1 - Levenshtein.distance(shorter, longer)) / m1

    return partial_ratio

str1 = 'Привет мир'
str2 = 'Привет мир!'

similarity_partial_ratio = partial_ratio(str1, str2)
print(similarity_partial_ratio)
end_time = time.perf_counter_ns()
print(f"Время выполнения 2 типа: {end_time - start_time} милисекунд.")


start_time = time.perf_counter_ns()
print("тип 3")
def token_sort_ratio(str1, str2):
    # Разбиваем строки на слова и сортируем их
    words1 = sorted(str1.split())
    words2 = sorted(str2.split())

    # Преобразуем отсортированные списки слов обратно в строки
    sorted_str1 = ' '.join(words1)
    sorted_str2 = ' '.join(words2)

    # Вычисляем близость Левенштейна между отсортированными строками
    distance = Levenshtein.distance(sorted_str1, sorted_str2)

    # Рассчитываем близость, аналогичную token_sort_ratio
    max_length = max(len(sorted_str1), len(sorted_str2))
    similarity_ratio = 100 - (distance / max_length) * 100

    return similarity_ratio


str1 = 'Привет наш мир'
str2 = 'мир наш Привет'

similarity_token_sort_ratio = token_sort_ratio(str1, str2)
print(similarity_token_sort_ratio)
end_time = time.perf_counter_ns()
print(f"Время выполнения 3 типа: {end_time - start_time} милисекунд.")


start_time = time.perf_counter_ns()
print("тип 4")
def token_set_ratio(str1, str2):
    # Разбиваем строки на слова
    words1 = set(str1.split())
    words2 = set(str2.split())

    # Преобразуем множества слов обратно в строки
    set_str1 = ' '.join(words1)
    set_str2 = ' '.join(words2)

    # Вычисляем близость Левенштейна между множествами слов
    distance = Levenshtein.distance(set_str1, set_str2)

    # Рассчитываем близость, аналогичную token_set_ratio
    max_length = max(len(set_str1), len(set_str2))
    similarity_ratio = 100 - (distance / max_length) * 100

    return similarity_ratio


str1 = 'Привет наш мир'
str2 = 'мир мир наш наш наш ПриВЕт'

similarity_token_set_ratio = token_set_ratio(str1, str2)
print(similarity_token_set_ratio)
end_time = time.perf_counter_ns()
print(f"Время выполнения 4 типа: {end_time - start_time} милисекунд.")



start_time = time.perf_counter_ns()
print("тип 5")
def wratio(str1, str2):
    # Преобразуем строки в нижний регистр и удаляем знаки препинания
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())

    # Вычисляем близость Левенштейна между очищенными строками
    distance = Levenshtein.distance(str1, str2)

    # Рассчитываем близость, аналогичную WRatio
    max_length = max(len(str1), len(str2))
    similarity_ratio = 100 - (distance / max_length) * 100

    return similarity_ratio


str1 = 'Привет наш мир'
str2 = '!ПриВЕт, наш мир!'

similarity_wratio = wratio(str1, str2)
print(similarity_wratio)
end_time = time.perf_counter_ns()
print(f"Время выполнения 5 типа: {end_time - start_time} милисекунд.")



start_time = time.perf_counter_ns()
print("тип 6")
def find_best_matches(query, options, limit=2):
    # Создаем пустой список для хранения наилучших совпадений
    best_matches = []

    # Проходим по всем опциям и вычисляем близость с запросом
    for option in options:
        similarity = 100 - (Levenshtein.distance(query, option) / max(len(query), len(option))) * 100

        # Добавляем пару (город, близость) в список
        best_matches.append((option, similarity))

    # Сортируем список по убыванию близости
    best_matches.sort(key=lambda x: x[1], reverse=True)

    # Возвращаем указанное количество лучших совпадений
    return best_matches[:limit]


cities = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск",
          "Красноярск", "Самара"]
query = "Саратов"

best_matches = find_best_matches(query, cities, limit=2)
print(best_matches)
end_time = time.perf_counter_ns()
print(f"Время выполнения 6 типа: {end_time - start_time} милисекунд.")