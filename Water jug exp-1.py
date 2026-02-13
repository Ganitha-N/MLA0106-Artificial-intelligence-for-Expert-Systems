from collections import deque

def water_jug():
    start = (0, 0)
    goal = 4
    q = deque([start])
    visited = set()
    parent = {}

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == goal:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()

            print("Steps to get 4 Litres:")
            for step in path:
                print(step)
            return

        next_states = [
            (5, y),
            (x, 3),
            (0, y),
            (x, 0),
            (x - min(x, 3 - y), y + min(x, 3 - y)),
            (x + min(y, 5 - x), y - min(y, 5 - x))
        ]

        for state in next_states:
            if state not in visited:
                parent[state] = (x, y)
                q.append(state)

water_jug()
