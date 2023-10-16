# input form: [pi] with pi the frequency and  i the index of pi the key
def solver(input):
    n = len(input) - 1
    A = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for s in range(n):
        for i in range(n-s):
            j = i + s + 1
            p = sum(input[k] for k in range(i, j+1))
            A[i][j] = p + min([A[i][r-1] + A[r+1][j] for r in range(i, j)])
    for row in A:
        print(row)
    return A[0][n]