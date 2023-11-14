import time
import matplotlib.pyplot as plt
import random
from collections import deque

#функция загрузки и обработки файлика
def load_incidence_matrix(file_path):
    incidence_matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = line.replace(',', ' ')  # Заменяем запятые на пробелы
            row = list(map(int, cleaned_line.strip().split()))
            incidence_matrix.append(row)
    return incidence_matrix

#поиск в ширину
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    paths = {start: [start]}
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, edge in enumerate(graph[vertex - 1]):
                if edge == 1 and neighbor + 1 not in visited:  # Изменяем индекс соседа
                    queue.append(neighbor + 1)  # Изменяем индекс соседа
                    paths[neighbor + 1] = paths[vertex] + [neighbor + 1]  # Изменяем индекс соседа
    return paths
#новый поиск в ширину
def breadth_first_search(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path, sum(graph[start][path[i]] for i in range(len(path) - 1))
        if node not in visited:
            visited.add(node)
            for i, weight in enumerate(graph[node]):
                if weight > 0:
                    queue.append((i, path + [i]))
    return None, 0


#поиск в глубину
def dfs(graph, start):
    visited = set()
    stack = [start]
    paths = {start: [start]}
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, edge in enumerate(graph[vertex - 1]):
                if edge == 1 and neighbor + 1 not in visited:  # Изменяем индекс соседа
                    stack.append(neighbor + 1)  # Изменяем индекс соседа
                    paths[neighbor + 1] = paths[vertex] + [neighbor + 1]  # Изменяем индекс соседа
    return paths
#новый поиск в глубину
def depth_first_search(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == end:
        path_weight = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        return path, path_weight

    for i, weight in enumerate(graph[start]):
        if weight > 0 and i not in visited:
            new_path, new_path_weight = depth_first_search(graph, i, end, visited.copy(), path)
            if new_path:
                return new_path, new_path_weight

    return None, 0

#поиск максимальных вершин
def find_two_largest_vertices(graph):
    num_vertices = len(graph)
    max_vertex1 = max_vertex2 = -1

    for vertex in range(1, num_vertices + 1):  # Изменение диапазона до 20
        for neighbor in range(1, num_vertices + 1):  # Изменение диапазона до 20
            if graph[vertex - 1][neighbor - 1] == 1:  # Индексы в матрице инцидентности начинаются с 0
                if vertex > max_vertex1:
                    max_vertex2 = max_vertex1
                    max_vertex1 = vertex
                elif vertex > max_vertex2:
                    max_vertex2 = vertex

    return max_vertex1, max_vertex2

# функция BFS с подсчетом глубины
def bfs_with_depth(graph, start):
    visited = set()
    queue = deque([(start, 0)])  # Добавляем глубину
    paths = {start: [start]}
    depths = {start: 0}  # Словарь для хранения глубины
    while queue:
        vertex, depth = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, edge in enumerate(graph[vertex]):
                if edge == 1 and neighbor not in visited:
                    queue.append((neighbor, depth + 1))  # Увеличиваем глубину
                    paths[neighbor] = paths[vertex] + [neighbor]
                    depths[neighbor] = depth + 1
    return paths, depths

# функция для измерения времени выполнения
def measure_execution_time(graph, algorithm, start_node):
    start_time = time.perf_counter()
    if algorithm == "BFS":
        bfs_with_depth(graph, start_node)
    elif algorithm == "DFS":
        dfs(graph, start_node)
    end_time = time.perf_counter()
    return end_time - start_time

# Функция для построения графика количества предшествующих узлов
def plot_predecessor_counts(bfs_paths, dfs_paths):
    plt.figure(figsize=(12, 6))

    # График для BFS
    plt.subplot(1, 2, 1)
    bfs_counts = [len(path) for path in bfs_paths.values()]
    plt.plot(list(bfs_paths.keys()), bfs_counts, label='Кол-во предшествующих узлов BFS', color='blue')
    plt.title('Кол-во предшествующих узлов в BFS до максимума')
    plt.xlabel('Узел')
    plt.ylabel('Кол-во предшествующих узлов')
    plt.legend()

    # График для DFS
    plt.subplot(1, 2, 2)
    dfs_counts = [len(path) for path in dfs_paths.values()]
    plt.plot(list(dfs_paths.keys()), dfs_counts, label='Кол-во предшествующих узлов DFS', color='green')
    plt.title('Кол-во предшествующих узлов в DFS до максимума')
    plt.xlabel('Узел')
    plt.ylabel('Кол-во предшествующих узлов')
    plt.legend()

    plt.tight_layout()
    plt.show()


#фунця для подсчета всех путей
def all_paths_dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for i, weight in enumerate(graph[start]):
        if weight > 0 and i not in path:
            new_paths = all_paths_dfs(graph, i, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


###########################################################################################



# Загрузка матрицы инциденций
incidence_matrix = load_incidence_matrix('матрица инцидентности.txt')

# Выполнение BFS и нахождение путей
bfs_paths = bfs(incidence_matrix, 1)

# Выполнение DFS и нахождение путей
dfs_paths = dfs(incidence_matrix, 1 )

# Генерация случайных весов для рёбер
num_vertices, num_edges = len(incidence_matrix), len(incidence_matrix[0])
weights = [random.randint(1, 100) for _ in range(num_edges)]

# Создание взвешенной матрицы смежности
weighted_graph = []
for i in range(num_vertices):
    row = []
    for j in range(num_edges):
        if incidence_matrix[i][j] == 1:
            row.append(weights[j])
        else:
            row.append(0)
    weighted_graph.append(row)

# Измерение времени выполнения BFS
start_time = time.perf_counter_ns()
bfs_paths = bfs(incidence_matrix, 1)
end_time = time.perf_counter_ns()
bfs_execution_time = end_time - start_time

# Нахождение двух самых больших вершин и путей к ним
max_vertex1, max_vertex2 = find_two_largest_vertices(incidence_matrix)
path_to_max_vertex1 = bfs_paths.get(max_vertex1, [])
path_to_max_vertex2 = bfs_paths.get(max_vertex2, [])

print("Самая большая вершина 1:", max_vertex1)
print("Самая большая вершина 2:", max_vertex2)
print("Путь к самой большой вершине 1 (BFS):", path_to_max_vertex1)
print("Путь к самой большой вершине 2 (BFS):", path_to_max_vertex2)
print("Время выполнения BFS:", bfs_execution_time)

# Измерение времени выполнения DFS
start_time = time.perf_counter_ns()
dfs_paths = dfs(incidence_matrix, 1)
end_time = time.perf_counter_ns()
dfs_execution_time = end_time - start_time


path_to_max_vertex1_dfs = dfs_paths[max_vertex1]
path_to_max_vertex2_dfs = dfs_paths[max_vertex2]

print("Путь к самой большой вершине 1 (DFS):", path_to_max_vertex1_dfs)
print("Путь к самой большой вершине 2 (DFS):", path_to_max_vertex2_dfs)
print("Время выполнения DFS:", dfs_execution_time)

# Выполнение BFS и нахождение путей и глубин
bfs_paths, bfs_depths = bfs_with_depth(incidence_matrix, 0)

# Измерение времени выполнения BFS
bfs_execution_time = measure_execution_time(incidence_matrix, "BFS", 1)

# Выполнение DFS и нахождение путей
dfs_paths = dfs(incidence_matrix, 1)

# Измерение времени выполнения DFS
dfs_execution_time = measure_execution_time(incidence_matrix, "DFS", 1)

print('пожежда напиши начальную точку')
start_vertex = int(input())
print('пожежда напиши конечную точку')
end_vertex = int(input())

#новый поиск в ширину вывод
path, path_weight = breadth_first_search(weighted_graph, start_vertex, end_vertex)

if path:
    print("Минимальный путь (поиск в ширину):", path)
    print("Вес пути (поиск в ширину):", path_weight)
else:
    print("Минимальный путь (поиск в ширину): Путь не найден")


#новый поиск в глубину вывод
path, path_weight = depth_first_search(weighted_graph, start_vertex, end_vertex)

if path:
    print("Минимальный путь (поиск в глубину):", path)
    print("Вес пути (поиск в глубину):", path_weight)
else:
    print("Минимальный путь (поиск в глубину): Путь не найден")

#подсчет всех путей
all_paths = all_paths_dfs(weighted_graph, start_vertex, end_vertex)

if all_paths:
    print("Все пути из A в B:")
    for path in all_paths:
        path_weight = sum(weighted_graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        print("Путь:", path)
        print("Вес пути:", path_weight)
else:
    print("Пути из A в B не найдены")

# Выполнение BFS и нахождение путей
bfs_paths = bfs(incidence_matrix, 1)

# Выполнение DFS и нахождение путей
dfs_paths = dfs(incidence_matrix, 1)

# Построение графиков количества предшествующих узлов
plot_predecessor_counts(bfs_paths, dfs_paths)


execution_times = [bfs_execution_time, dfs_execution_time]
algorithms = ["BFS", "DFS"]

plt.figure(figsize=(8, 4))
plt.bar(algorithms, execution_times, color=['blue', 'green'])
plt.title('Время выполнения BFS и DFS до максимумов')
plt.xlabel('Алгоритм')
plt.ylabel('Время выполнения (наносекунды)')
plt.show()