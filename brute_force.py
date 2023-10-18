# input form: [pi] with pi the frequency and i the index of pi the key
def solver(input):
    n = len(input) - 1
    W = [[0 for i in range(n+1)] for j in range(n+1)]
    for j in range(n+1):
        for i in range(j):
            p = sum(input[k] for k in range(i, j+1))
            W[i][j] = p + min([W[i][r-1] + W[r+1][j] for r in range(i, j)])
    for row in W:
        print(row)
    return W[0][n]