# input form: [pi] with pi the frequency and  i the index of pi the key
def solver(input):
    n = len(input)
    A = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        A[i][i] = input[i]
    for length in range(2, n+1):
        for i in range(n - length + 2):
            j = i + length - 1
            A[i][j] = float('inf')
            p = sum(input[i:j+1])
            for r in range(i, j+1):
                a = (A[i][r-1] if r > i else 0) + (A[r+1][j] if r < j else 0) + p
                A[i][j] = min(A[i][j], a)
    return A