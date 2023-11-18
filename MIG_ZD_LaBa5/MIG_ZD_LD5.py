import pandas as pd
import matplotlib.pyplot as plt

# Чтение CSV файла
csv_file = 'data.csv'
data = pd.read_csv(csv_file)


# Описание пропущенных значений во всех столбцах
missing_values = data.isnull().sum()
print("Пропущенные значения:")
print(missing_values)

# Проверка доли пропущенных значений в каждом столбце
missing_percentage = (data.isnull().sum() / len(data)) * 100
print("\nДоля пропущенных значений в каждом столбце:")
print(missing_percentage)

# Построение графика
plt.figure(figsize=(10, 6))
missing_percentage.plot(kind='bar', color='skyblue')
plt.title('Доля пропущенных значений в каждом столбце')
plt.xlabel('Столбцы')
plt.ylabel('Процент пропусков')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Нахождение медианы столбца 'к'
median_k = data['total_income'].median()

# Заполнение пропущенных значений в столбце 'к' медианным значением
data['total_income'].fillna(median_k, inplace=True)

#################################################################################################

# Замена отрицательных значений в первом столбце на 0
data.iloc[:, 0] = data.iloc[:, 0].apply(lambda x: max(x, 0))

############################################################

# Замена отрицательных значений во втором столбце на положительные
data.iloc[:, 1] = data.iloc[:, 1].apply(lambda x: abs(x) if x < 0 else x)

# Замена значений больше 20000 на 20000
data['days_employed'] = data['days_employed'].apply(lambda x: min(x, 20000))

#############################################################

# Удаление строк, где значение в третьем столбце равно 0
data = data[data['dob_years'] != 0]

#############################################################

# Нахождение медианы столбца 'к'
median_k = data['days_employed'].median()

# Заполнение пропущенных значений в столбце 'к' медианным значением
data['days_employed'].fillna(median_k, inplace=True)

###################################################################################################

# Замена вещественного типа данных на целочисленный в столбце total_income
data['total_income'] = data['total_income'].astype(int)

####################################################################################################

# Приведение значений четвёртого столбца к нижнему регистру
data.iloc[:, 3] = data.iloc[:, 3].str.lower()

# Удаление повторяющихся строк
data.drop_duplicates(inplace=True)

####################################################################################################

# Создание "словаря" для education
education_dict = data[['education', 'education_id']].drop_duplicates().reset_index(drop=True)

# Создание "словаря" для family_status
family_status_dict = data[['family_status', 'family_status_id']].drop_duplicates().reset_index(drop=True)

# Удаление столбцов education и family_status из исходного DataFrame
data.drop(['education', 'family_status'], axis=1, inplace=True)

# Сохранение "словарей" в новые файлы (
education_dict.to_csv('education_dict.csv', index=False)
family_status_dict.to_csv('family_status_dict.csv', index=False)

# Вывод получившихся "словарей"
print("Словарь education:")
print(education_dict)
print("\nСловарь family_status:")
print(family_status_dict)

##########################################################################################################

# Функция для определения категории на основе значения дохода
def categorize_income(value):
    if value <= 30000:
        return 'E'
    elif 30001 <= value <= 50000:
        return 'D'
    elif 50001 <= value <= 200000:
        return 'C'
    elif 200001 <= value <= 1000000:
        return 'B'
    else:
        return 'A'

# Добавление столбца total_income_category
data['total_income_category'] = data['total_income'].apply(categorize_income)


###########################################################################################################

# Функция для определения категории на основе цели
def categorize_purpose(text):
    if 'авто' in text or 'автомобиль' in text:
        return 'операции с автомобилем'
    elif 'недвиж' in text or 'жиль' in text:
        return 'операции с недвижимостью'
    elif 'свадьб' in text:
        return 'проведение свадьбы'
    elif 'образован' in text or 'учеб' in text:
        return 'получение образования'
    else:
        return 'другое'

# Добавление столбца purpose_category
data['purpose_category'] = data['purpose'].apply(categorize_purpose)


# Сохранение изменений в файл
data.to_csv('file_final__category2.csv', index=False)


import pandas as pd

# Чтение файла
file_name = 'file_final__category2.csv'
data = pd.read_csv(file_name)

# Группировка данных по уникальным значениям 'children' и подсчет суммы 'debt' для каждого значения 'children'
grouped_data = data.groupby('children')['debt'].sum()

# Подсчет количества значений 'debt' для каждого значения 'children'
value_counts_children = data['children'].value_counts()

# Объединение результатов в один DataFrame
result = pd.concat([value_counts_children, grouped_data], axis=1)
result.columns = ['Count', 'Sum of Debt']

# Добавление столбца 'Statistic' с результатом деления количества строк на сумму 'debt'
result['Statistic'] = result['Count'] / result['Sum of Debt']

# Вывод результата
print(result.to_string())

import pandas as pd

# Чтение файла
file_name = 'file_final__category2.csv'
data = pd.read_csv(file_name)

# Группировка данных по уникальным значениям 'children' и подсчет суммы 'debt' для каждого значения 'children'
grouped_data = data.groupby('family_status_id')['debt'].sum()

# Подсчет количества значений 'debt' для каждого значения 'children'
value_counts_children = data['family_status_id'].value_counts()

# Объединение результатов в один DataFrame
result = pd.concat([value_counts_children, grouped_data], axis=1)
result.columns = ['Count', 'Sum of Debt']

# Добавление столбца 'Statistic' с результатом деления количества строк на сумму 'debt'
result['Statistic'] = result['Count'] / result['Sum of Debt']

# Вывод результата
print(result)


# Чтение файла
file_name = 'file_final__category2.csv'
data = pd.read_csv(file_name)

# Группировка данных по уникальным значениям 'children' и подсчет суммы 'debt' для каждого значения 'children'
grouped_data = data.groupby('total_income_category')['debt'].sum()

# Подсчет количества значений 'debt' для каждого значения 'children'
value_counts_children = data['total_income_category'].value_counts()

# Объединение результатов в один DataFrame
result = pd.concat([value_counts_children, grouped_data], axis=1)
result.columns = ['Count', 'Sum of Debt']

# Добавление столбца 'Statistic' с результатом деления количества строк на сумму 'debt'
result['Statistic'] = result['Count'] / result['Sum of Debt']

# Вывод результата
print(result)


# Чтение файла
file_name = 'file_final__category2.csv'
data = pd.read_csv(file_name)

# Группировка данных по уникальным значениям 'children' и подсчет суммы 'debt' для каждого значения 'children'
grouped_data = data.groupby('purpose_category')['debt'].sum()

# Подсчет количества значений 'debt' для каждого значения 'children'
value_counts_children = data['purpose_category'].value_counts()

# Объединение результатов в один DataFrame
result = pd.concat([value_counts_children, grouped_data], axis=1)
result.columns = ['Count', 'Sum of Debt']

# Добавление столбца 'Statistic' с результатом деления количества строк на сумму 'debt'
result['Statistic'] = result['Count'] / result['Sum of Debt']

# Вывод результата
print(result)