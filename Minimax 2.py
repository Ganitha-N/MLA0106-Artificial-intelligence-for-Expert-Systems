def minimax(node, maximizing):
    if type(node) != list:
        return node

    if maximizing:
        value = float('-inf')
        for child in node:
            value = max(value, minimax(child, False))
        return value
    else:
        value = float('inf')
        for child in node:
            value = min(value, minimax(child, True))
        return value


tree = [[[8,3],[5,9]],[[0,1],[4,5]]]

result = minimax(tree, True)
print("Best Value:", result)
