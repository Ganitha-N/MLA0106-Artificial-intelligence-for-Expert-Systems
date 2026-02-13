BFS(Graph, start)

1. Create empty queue Q
2. Create empty set Visited
3. Enqueue start into Q
4. Mark start as visited

5. While Q is not empty:
       a. Dequeue node v
       b. Print v
       c. For each neighbor u of v:
              If u not in Visited:
                    Enqueue u
                    Mark u as visited

   

DFS(Graph, node)

1. Mark node as visited
2. Print node

3. For each neighbor u of node:
       If u not visited:
            Call DFS(Graph, u)

   

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

   

A_STAR(Graph, start, goal)

1. Create Priority Queue OPEN
2. Insert start with f = h(start)
3. g(start) = 0

4. While OPEN not empty:
      a. Remove node with lowest f value
      b. If node == goal:
            Return path

      c. For each neighbor:
            new_g = g(current) + cost
            If neighbor not visited OR new_g < g(neighbor):
                  g(neighbor) = new_g
                  f = new_g + h(neighbor)
                  Insert neighbor into OPEN

   
WATER_JUG(start)

1. Create queue Q
2. Create empty set Visited
3. Enqueue start state

4. While Q not empty:
       a. Remove state (x, y)
       b. If goal condition satisfied:
              Print solution and stop

    c. Generate all possible next states
    d. For each new state:
            If not visited:
                  Mark visited
                  Enqueue state
