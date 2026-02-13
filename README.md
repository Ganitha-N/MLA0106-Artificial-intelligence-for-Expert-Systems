BFS(Graph, start):

1. Create an empty queue Q
2. Create an empty set Visited

3. Add start to Q
4. Mark start as visited

5. While Q is not empty:
       a. Remove vertex v from Q
       b. Print v

   c. For each neighbor u of v:
              If u is not visited:
                     Add u to Q
                     Mark u as visited


DFS(Graph, start)

1. Create empty set Visited
2. Call DFS_Visit(start)
DFS_Visit(node)

1. Mark node as visited
2. Print node

3. For each neighbor u of node:
       If u is not visited:
            Call DFS_Visit(u)
   

MINIMAX(node, maximizing)

1. If node is leaf:
       Return node value

2. If maximizing:
       best = -∞
       For each child:
            best = max(best, MINIMAX(child, False))
       Return best

3. Else (minimizing):
       best = +∞
       For each child:
            best = min(best, MINIMAX(child, True))
       Return best


ALPHABETA(node, alpha, beta, maximizing)

1. If node is leaf:
       Return node value

2. If maximizing:
       value = -∞
       For each child:
            value = max(value, ALPHABETA(child, alpha, beta, False))
            alpha = max(alpha, value)
            If alpha >= beta:
                  Break   // Beta cut-off
       Return value

3. Else (minimizing):
       value = +∞
       For each child:
            value = min(value, ALPHABETA(child, alpha, beta, True))
            beta = min(beta, value)
            If beta <= alpha:
                  Break   // Alpha cut-off
       Return value

A*(Graph, start, goal)

1. Create priority queue OPEN
2. Insert start with f = h(start)
3. g(start) = 0
4. Create empty parent map

5. While OPEN not empty:
       a. Remove node with lowest f value
       b. If node is goal:
              Reconstruct path and return

   c. For each neighbor:
              new_g = g(current) + cost
              If neighbor not visited OR new_g < g(neighbor):
                    g(neighbor) = new_g
                    f = new_g + h(neighbor)
                    Insert into OPEN
                    Set parent of neighbor


WATER_JUG(start)

1. Create queue Q
2. Create empty set Visited
3. Enqueue start state

4. While Q not empty:
       a. Remove state (x, y)
       b. If goal condition satisfied:
              Print solution and stop

    c. Generate all possible next states:
              - Fill jug
              - Empty jug
              - Pour one jug into another

    d. For each new state:
              If not visited:
                   Mark visited
                   Enqueue state
