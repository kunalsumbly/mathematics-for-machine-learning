import numpy as np
from mml_utils import plot_lines
A = np.array([[4,3],[1,-5]],dtype=np.float64)
b = np.array([6,8],dtype=np.float64)
print(np.linalg.solve(A,b))
A_2 = np.hstack((A,b.reshape(2,1)))
plot_lines(A_2)
