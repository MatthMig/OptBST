from codecarbon import EmissionsTracker

import brute_force
import dp


def random_input(n, inf=0, sup=1000):
    import random
    return [random.uniform(inf, sup) for _ in range(n)]

#input = [0.1, 0.2, 0.4, 0.3]
input = random_input(10)

print("Brute force:")
print(brute_force.solver(input))
print("\nDynamic programming:")
dp_matrix = dp.solver(input)
print(dp_matrix[0][-2])