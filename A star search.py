import heapq

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start)]
    parent = {}
    g = {start: 0}

    while pq:
        f, cost, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            return path[::-1], cost

        for neigh, w in graph[node]:
            new_cost = cost + w
            if neigh not in g or new_cost < g[neigh]:
                g[neigh] = new_cost
                heapq.heappush(pq, (new_cost + h[neigh], new_cost, neigh))
                parent[neigh] = node

    return None, None


graph = {
    'S':[('A',1),('B',4)],
    'A':[('C',2),('D',5)],
    'B':[('D',1)],
    'C':[('G',3)],
    'D':[('G',2)],
    'G':[]
}

h = {'S':7,'A':6,'B':2,'C':1,'D':1,'G':0}

path, cost = astar(graph, h, 'S', 'G')

print("Path:", " -> ".join(path))
print("Cost:", cost)
