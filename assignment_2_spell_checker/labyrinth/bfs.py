from collections import deque

class BFS:
    @staticmethod
    def find_shortest_path(labyrinth, start, end):
        queue = deque([start])
        visited = {start}
        distance = {start: 0}

        while queue:
            current = queue.popleft()

            if current == end:
                return distance[current]

            for neighbor in labyrinth.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    distance[neighbor] = distance[current] + 1

        return float('inf')