import numpy as np
import matplotlib.pyplot as plt
from mml_utils import plot_lines

# system of equation with 1 unique solution , non singular system

A = np.array([[-1,3],[3,2]],dtype=np.float64)
b = np.array([7,1],dtype=np.float64)
print(A.ndim)
print(b.ndim)
x = np.linalg.solve(A,b)
print(x)
y = np.linalg.det(A)
print(y)
z = np.hstack((A,b.reshape(2,1)))
print(z[1])
plot_lines(z)
z=np.vstack((A,b))
print(z)

# system of equation with no solution, singular system
B = np.array([[-1,3],[3,-9]], dtype=np.dtype(float))
c = np.array([7,1], dtype=np.dtype(float))
print(np.linalg.solve(B,c))
print(np.linalg.det(B))

A_2 = np.array([
        [-1, 3],
        [3, -9]
    ], dtype=np.dtype(float))
d_2 = np.linalg.det(A_2)
print(f"Determinant of matrix A_2: {d_2:.2f}")

try:
    x_2 = np.linalg.solve(A_2, c)
except np.linalg.LinAlgError as err:
    print(err)

z = np.hstack((A_2, c.reshape(2, 1)))
plot_lines(z)

b_3 = np.array([7, -21], dtype=np.dtype(float))
A_3 = np.hstack((A_2, b_3.reshape(2, 1)))
plot_lines(A_3)

