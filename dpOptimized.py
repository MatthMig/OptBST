def optimalSearchTreeCost(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    opt = [[0] * n for _ in range(n)]

    for i in range(n):
        opt[i][i] = i
        cost[i][i] = freq[i]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            mn = float('inf')
            cost_sum = sum(freq[i:j + 1])

            for k in range(opt[i][j - 1], min(j - 1, opt[i + 1][j]) + 1):
                c = (cost[i][k] + cost[k + 1][j] + cost_sum)
                if c < mn:
                    opt[i][j] = k
                    mn = c

            cost[i][j] = mn

    return cost[0][n - 1]
