from collections import deque

def water_jug():
    start = (12, 0, 0)
    goal = (6, 6)
    capacities = (12, 8, 5)

    q = deque([start])
    visited = set()
    parent = {}

    while q:
        state = q.popleft()

        if state in visited:
            continue
        visited.add(state)

        a, b, c = state

        if a == goal[0] and b == goal[1]:
            path = []
            while state in parent:
                path.append(state)
                state = parent[state]
            path.append(start)
            path.reverse()

            print("Steps to get (6,6,0):")
            for step in path:
                print(step)
            return

        jugs = list(state)

        for i in range(3):
            for j in range(3):
                if i != j:
                    new = list(jugs)
                    pour = min(jugs[i], capacities[j] - jugs[j])
                    new[i] -= pour
                    new[j] += pour
                    new_state = tuple(new)

                    if new_state not in visited:
                        parent[new_state] = state
                        q.append(new_state)

water_jug()
