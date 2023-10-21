import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#метод 1
def generate_random_list1(n, lower, upper):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(lower, upper))
    return rand_list

def merge_functions(rand_list):
    # count rate
    kub_rate = {}
    for i in rand_list:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0

    # sort rate
    sorted_rate = {key: kub_rate[key] for key in sorted(kub_rate.keys())}

    # create dataframe
    df = pd.DataFrame(sorted_rate.items(), columns=['Количество выпаданий', 'Частота'])
    df.set_index('Количество выпаданий', inplace=True)

    # solve probability
    sum_rate = df['Частота'].sum()
    df['Вероятность'] = df['Частота'].apply(lambda x: x / sum_rate)

    return df

numbers_of_throws = [100, 1000, 10000, 1000000]  # Numbers of throws

fig, axs = plt.subplots(len(numbers_of_throws), figsize=(10, 5*len(numbers_of_throws)))
plt.subplots_adjust(hspace=0.4)
plt.suptitle("Первый метод")

# создаём список с цветами
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

for ax, n in zip(axs, numbers_of_throws):
    data = generate_random_list1(n, 1, 6)
    df = merge_functions(data)

    # устанавливаем цвета для столбцов
    df['Частота'].plot(kind='bar', ax=ax, color=colors)  # заменили color='skyblue' на color=colors

    ax.set_title('Гистограмма для {} бросков'.format(n))
    ax.set_xlabel('Что выпало')
    ax.set_ylabel('Частота')

    # add text
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()

#метод 2
def generate_random_list2(n, lower, upper):
    res = random.sample(range(lower, upper + 1), n)
    return res

def merge_functions(res):
    # count rate
    kub_rate = {}
    for i in res:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0

    # sort rate
    sorted_rate = {key: kub_rate[key] for key in sorted(kub_rate.keys())}

    # create dataframe
    df = pd.DataFrame(sorted_rate.items(), columns=['Количество выпаданий', 'Частота'])
    df.set_index('Количество выпаданий', inplace=True)

    # solve probability
    sum_rate = df['Частота'].sum()
    df['Вероятность'] = df['Частота'].apply(lambda x: x / sum_rate)

    return df

numbers_of_throws = [100, 1000, 10000, 1000000]  # Numbers of throws

fig, axs = plt.subplots(len(numbers_of_throws), figsize=(10, 5*len(numbers_of_throws)))
plt.subplots_adjust(hspace=0.4)
plt.suptitle("Второй метод")

# создаём список с цветами
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

for ax, n in zip(axs, numbers_of_throws):
    data = generate_random_list1(n, 1, 6)
    df = merge_functions(data)

    # устанавливаем цвета для столбцов
    df['Частота'].plot(kind='bar', ax=ax, color=colors)  # заменили color='skyblue' на color=colors

    ax.set_title('Гистограмма для {} бросков'.format(n))
    ax.set_xlabel('Что выпало')
    ax.set_ylabel('Частота')

    # add text
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()

#метод 3
def generate_random_list3(n, lower, upper):
    res2 = [random.randrange(lower, upper + 1) for i in range(n)]
    return res2

def merge_functions(res2):
    # count rate
    kub_rate = {}
    for i in res2:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0

    # sort rate
    sorted_rate = {key: kub_rate[key] for key in sorted(kub_rate.keys())}

    # create dataframe
    df = pd.DataFrame(sorted_rate.items(), columns=['Количество выпаданий', 'Частота'])
    df.set_index('Количество выпаданий', inplace=True)

    # solve probability
    sum_rate = df['Частота'].sum()
    df['Вероятность'] = df['Частота'].apply(lambda x: x / sum_rate)

    return df

numbers_of_throws = [100, 1000, 10000, 1000000]  # Numbers of throws

fig, axs = plt.subplots(len(numbers_of_throws), figsize=(10, 5*len(numbers_of_throws)))
plt.subplots_adjust(hspace=0.4)
plt.suptitle("Третий метод")

# создаём список с цветами
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

for ax, n in zip(axs, numbers_of_throws):
    data = generate_random_list1(n, 1, 6)
    df = merge_functions(data)

    # устанавливаем цвета для столбцов
    df['Частота'].plot(kind='bar', ax=ax, color=colors)  # заменили color='skyblue' на color=colors

    ax.set_title('Гистограмма для {} бросков'.format(n))
    ax.set_xlabel('Что выпало')
    ax.set_ylabel('Частота')

    # add text
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()


#метод 4
def generate_random_list4(n, lower, upper):
    lis = []
    for _ in range(n):
        lis.append(random.randint(lower, upper))
    return lis


def merge_functions(lis):
    # count rate
    kub_rate = {}
    for i in lis:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0

    # sort rate
    sorted_rate = {key: kub_rate[key] for key in sorted(kub_rate.keys())}

    # create dataframe
    df = pd.DataFrame(sorted_rate.items(), columns=['Количество выпаданий', 'Частота'])
    df.set_index('Количество выпаданий', inplace=True)

    # solve probability
    sum_rate = df['Частота'].sum()
    df['Вероятность'] = df['Частота'].apply(lambda x: x / sum_rate)

    return df

numbers_of_throws = [100, 1000, 10000, 1000000]  # Numbers of throws

fig, axs = plt.subplots(len(numbers_of_throws), figsize=(10, 5*len(numbers_of_throws)))
plt.subplots_adjust(hspace=0.4)
plt.suptitle("Четвертый метод")

# создаём список с цветами
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

for ax, n in zip(axs, numbers_of_throws):
    data = generate_random_list1(n, 1, 6)
    df = merge_functions(data)

    # устанавливаем цвета для столбцов
    df['Частота'].plot(kind='bar', ax=ax, color=colors)  # заменили color='skyblue' на color=colors

    ax.set_title('Гистограмма для {} бросков'.format(n))
    ax.set_xlabel('Что выпало')
    ax.set_ylabel('Частота')

    # add text
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()


#метод 5
def generate_random_list5(n1, n2, lower1, upper1, lower2):
    # print the list of 10 integers from 3 to 7
    list15 = list(np.random.randint(low=lower1, high=upper1, size=n1))

    # print the list of 5 integers from 0 to 2
    # if high parameter is not passed during
    # function call then results are from [0, low)
    list2 = list(np.random.randint(low=lower2, size=n2))

    return list15, list2

def merge_functions(list15):
    # count rate
    kub_rate = {}
    for i in list15:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0

    # sort rate
    sorted_rate = {key: kub_rate[key] for key in sorted(kub_rate.keys())}

    # create dataframe
    df = pd.DataFrame(sorted_rate.items(), columns=['Количество выпаданий', 'Частота'])
    df.set_index('Количество выпаданий', inplace=True)

    # solve probability
    sum_rate = df['Частота'].sum()
    df['Вероятность'] = df['Частота'].apply(lambda x: x / sum_rate)

    return df

numbers_of_throws = [100, 1000, 10000, 1000000]  # Numbers of throws

fig, axs = plt.subplots(len(numbers_of_throws), figsize=(10, 5*len(numbers_of_throws)))
plt.subplots_adjust(hspace=0.4)
plt.suptitle("Пятый метод")

# создаём список с цветами
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

for ax, n in zip(axs, numbers_of_throws):
    data = generate_random_list1(n, 1, 6)
    df = merge_functions(data)

    # устанавливаем цвета для столбцов
    df['Частота'].plot(kind='bar', ax=ax, color=colors)  # заменили color='skyblue' на color=colors

    ax.set_title('Гистограмма для {} бросков'.format(n))
    ax.set_xlabel('Что выпало')
    ax.set_ylabel('Частота')

    # add text
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()

#метод 6
def generate_random_list6(size1, size2):
    # generates list of 4 float values
    list1 = np.random.random_sample(size=size1)

    # generates 2d list of 4*4
    list2 = np.random.random_sample(size=size2)

    return list1, list2

def merge_functions(list1):
    # count rate
    kub_rate = {}
    for i in list1:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0

    # sort rate
    sorted_rate = {key: kub_rate[key] for key in sorted(kub_rate.keys())}

    # create dataframe
    df = pd.DataFrame(sorted_rate.items(), columns=['Количество выпаданий', 'Частота'])
    df.set_index('Количество выпаданий', inplace=True)

    # solve probability
    sum_rate = df['Частота'].sum()
    df['Вероятность'] = df['Частота'].apply(lambda x: x / sum_rate)

    return df

numbers_of_throws = [100, 1000, 10000, 1000000]  # Numbers of throws

fig, axs = plt.subplots(len(numbers_of_throws), figsize=(10, 5*len(numbers_of_throws)))
plt.subplots_adjust(hspace=0.4)
plt.suptitle("Шестой метод")

# создаём список с цветами
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

for ax, n in zip(axs, numbers_of_throws):
    data = generate_random_list1(n, 1, 6)
    df = merge_functions(data)

    # устанавливаем цвета для столбцов
    df['Частота'].plot(kind='bar', ax=ax, color=colors)  # заменили color='skyblue' на color=colors

    ax.set_title('Гистограмма для {} бросков'.format(n))
    ax.set_xlabel('Что выпало')
    ax.set_ylabel('Частота')

    # add text
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()