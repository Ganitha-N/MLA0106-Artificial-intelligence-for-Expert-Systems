def minimax(node, depth, isMax):
    if depth == 0 or type(node) != list:
        return node

    if isMax:
        best = float('-inf')
        for child in node:
            best = max(best, minimax(child, depth-1, False))
        return best
    else:
        best = float('inf')
        for child in node:
            best = min(best, minimax(child, depth-1, True))
        return best


tree = [[[3,5],[6,9]],[[1,2],[0,-1]]]

result = minimax(tree, 3, True)
print("Optimal Value:", result)
