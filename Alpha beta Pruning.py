def alphabeta(node, depth, alpha, beta, maximizing):
    if depth == 0 or type(node) != list:
        return node

    if maximizing:
        value = float('-inf')
        for child in node:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node:
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


tree = [
            [[3,3],[5,9]],
            [[0,1],[4,5]]
       ]

print("Optimal value:", alphabeta(tree, 3, float('-inf'), float('inf'), True))
