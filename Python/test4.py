import numpy as np

input_x = input().strip()
input_y = input().strip()
x = np.array(list(map(float, input_x.split())))
y = np.array(list(map(float, input_y.split())))
MX = np.mean(x)
MY = np.mean(y)
SX = np.std(x)
SY = np.std(y)
correlation_matrix = np.corrcoef(x, y)
r = correlation_matrix[0, 1]
b = r * (SY / SX)
A = MY - b * MX

# Print the results
print(f"Mean of x = {MX:.1f}")
print(f"Mean of y = {MY:.2f}")
print(f"SD of x = {SX:.3f}")
print(f"SD of y = {SY:.3f}")
print(f"Correlation of x and y = {r:.3f}")
print(f"Scope = {b:.3f}")
print(f"Intercept = {A:.3f}")