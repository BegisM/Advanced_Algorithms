def is_bipartite(graph):
    """
    Проверяет, является ли данный граф двудольным, используя нерекурсивный алгоритм DFS.
    :param graph: Словарь, где ключи - узлы, а значения - списки смежных узлов.
    :return: Кортеж (bool, dict), указывающий, является ли граф двудольным и раскраску узлов.
    """
    color = {}
    stack = []

    for node in graph:
        if node not in color:
            # Начать DFS с этого узла
            stack.append((node, 0))  # (узел, цвет)
            while stack:
                current, c = stack.pop()
                if current in color:
                    if color[current] != c:
                        return False, {}
                else:
                    color[current] = c
                    for neighbor in graph[current]:
                        stack.append((neighbor, 1 - c))

    return True, color


def seating_scheme(guests, dislikes):

    graph = {guest: [] for guest in guests}
    for guest1, guest2 in dislikes:
        graph[guest1].append(guest2)
        graph[guest2].append(guest1)


    is_bipart, coloring = is_bipartite(graph)

    if not is_bipart:
        return "Невозможно рассадить гостей за два стола."

    table1 = [guest for guest in coloring if coloring[guest] == 0]
    table2 = [guest for guest in coloring if coloring[guest] == 1]

    return table1, table2


guests = ["Алиса", "Боб", "Чарли", "Дэвид"]
dislikes = [("Алиса", "Боб"), ("Алиса", "Чарли"), ("Боб", "Дэвид")]

table1, table2 = seating_scheme(guests, dislikes)
print("Стол 1:", table1)
print("Стол 2:", table2)

