import brute_force
import dp

input = [0.1, 0.2, 0.4, 0.3]

print("Brute force:")
print(brute_force.solver(input))
print("\nDynamic programming:")
dp_matrix = dp.solver(input)
print(dp_matrix[0][-2])