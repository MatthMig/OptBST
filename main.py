import brute_force
import dp

input = [0.1, 0.2, 0.3, 0.4]

print("Brute force:")
print(brute_force.solver(input))
print("\nDynamic programming:")
print(dp.solver(input))