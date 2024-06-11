def is_bipartite(graph):
    color = {}
    stack = []

    for node in graph:
        if node not in color:
            stack.append((node, 0))
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
        return "Not possible"

    table1 = [guest for guest in coloring if coloring[guest] == 0]
    table2 = [guest for guest in coloring if coloring[guest] == 1]

    return table1, table2


guests = ["Anna", "Boris", "Viktor"]
dislikes = [("Anna", "Boris"), ("Anna", "Viktor"), ("Boris", "Viktor")]

res = seating_scheme(guests, dislikes)
print(res)

guests = ["Anna", "Boris", "Viktor", "Gleb"]
dislikes = [("Anna", "Boris"), ("Anna", "Viktor"), ("Boris", "Gleb"), ("Viktor", "Gleb")]
res = seating_scheme(guests, dislikes)
print(res)


