import math

MAX, MIN = 1000, -1000

# Alpha-Beta Pruning
def alpha_beta_minimax(depth, nodeIndex, maximizingPlayer,
                       values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = alpha_beta_minimax(depth + 1, nodeIndex * 2 + i,
                                     False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = alpha_beta_minimax(depth + 1, nodeIndex * 2 + i,
                                     True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Normal Minimax Algorithm
def minimax(curDepth, nodeIndex, maxTurn, values, targetDepth):
    if curDepth == targetDepth:
        return values[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, values, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, values, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, values, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, values, targetDepth))

# Ask the user for the mode and root node preference
print("Choose a mode:")
print("1. Alpha-Beta Pruning")
print("2. Normal Minimax Algorithm")
mode = input("Enter the mode (1 or 2): ")
root_preference = input("Enter 'max' or 'min' for the root node: ")

values = [3, 5, 6, 9, 1, 2, 0, -1]

if mode == '1':
    print("Using Alpha-Beta Pruning")
    if root_preference == 'max':
        print("The optimal value is:", alpha_beta_minimax(0, 0, True, values, MIN, MAX))
    elif root_preference == 'min':
        print("The optimal value is:", alpha_beta_minimax(0, 0, False, values, MIN, MAX))
    else:
        print("Invalid root node preference. Please enter 'max' or 'min'.")
elif mode == '2':
    treeDepth = math.log(len(values), 2)
    print("Using Normal Minimax Algorithm")
    if root_preference == 'max':
        print("The optimal value is:", minimax(0, 0, True, values, int(treeDepth)))
    elif root_preference == 'min':
        print("The optimal value is:", minimax(0, 0, False, values, int(treeDepth)))
    else:
        print("Invalid root node preference. Please enter 'max' or 'min'.")
else:
    print("Invalid mode selection. Please enter 1 or 2.")
