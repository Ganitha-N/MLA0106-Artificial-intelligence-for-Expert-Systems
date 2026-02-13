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
