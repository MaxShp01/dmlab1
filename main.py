# Визначення функції, що реалізує алгоритм Борувки
def boruvka(graph):
    # Визначення кількості вершин у графі
    n = len(graph)

    # Створення списку компонентів, де на початку кожна вершина є окремою компонентою
    components = [[i] for i in range(n)]

    # Початок циклу Борувки
    while len(components) > 1:
        # Створення списку мінімальних ребер для кожної компоненти
        min_edges = [None] * n
        for i, comp in enumerate(components):
            for j in comp:
                for k in range(n):
                    if k not in comp and (
                            min_edges[k] is None or graph[j][k] < graph[min_edges[k][0]][min_edges[k][1]]):
                        min_edges[k] = (j, k)

        # Об'єднання компонент, що мають мінімальні ребра
        for edge in min_edges:
            if edge is not None:
                comp1 = next((comp for comp in components if edge[0] in comp), None)
                comp2 = next((comp for comp in components if edge[1] in comp), None)
                if comp1 != comp2:
                    components.remove(comp1)
                    components.remove(comp2)
                    components.append(comp1 + comp2)

    # Повернення результату
    return components[0]


# Задання графа у вигляді матриці суміжності
graph = [[0, 0, 38, 95, 0, 1, 57, 0],
         [0, 0, 0, 0, 79, 0, 36, 19],
         [38, 0, 0, 51, 0, 0, 44, 0],
         [95, 0, 51, 0, 0, 44, 0, 0],
         [0, 79, 0, 0, 0, 93, 41, 48],
         [1, 0, 0, 44, 93, 0, 1, 0],
         [57, 36, 44, 0, 41, 1, 0, 0],
         [0, 19, 0, 0, 48, 0, 0, 0]]

# Виклик функції boruvka() та виведення результату
result = boruvka(graph)
print(result)
