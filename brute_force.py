# input form: [pi] with pi the frequency and i the index of pi the key
def solver(input):
    n = len(input)
    return optCost(input, 0, n - 1)

def optCost(freq, i, j):
    if j < i:
        return 0
    if j == i:
        return freq[i]
    
    fsum = Sum(freq, i, j)

    # Initialize minimum value
    Min = float('inf')
    
    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1) +
                optCost(freq, r + 1, j))
        if cost < Min:
            Min = cost

    return Min + fsum

def Sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s