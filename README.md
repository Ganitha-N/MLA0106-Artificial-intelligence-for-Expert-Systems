BFS 
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


   DFS
   DFS(Graph, start)

1. Create empty set Visited
2. Call DFS_Visit(start)

DFS_Visit(node)

1. Mark node as visited
2. Print node

3. For each neighbor u of node:
       If u is not visited:
            Call DFS_Visit(u)

