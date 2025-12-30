import numpy as np
import mml_utils as utils
# this is an example of non singular system
A_1 = np.array([[4,-3,1],[2,1,3],[-1,2,-5]], dtype=np.dtype(float))
b = np.array([-10,0,17], dtype=np.dtype(float))
sol_1 = np.linalg.solve(A_1,b)
print(sol_1)
print(A_1.shape)
print(b.shape)
d_1 = np.linalg.det(A_1)
print(f'Determinant = {d_1:.2f}')

# example of singular system
A_2 = np.array([[1,1,1],[0,1,-3],[2,1,5]], dtype=np.dtype(float))
b_2 = np.array([2,1,0], dtype=np.dtype(float))

'''
   Remember that np.linalg.solve gives an error if there are no or infinitely many solutions.
   When using it, you will need to check for that case to prevent your program from crashing.
'''
sol_2 = np.linalg.solve(A_2,b_2)  # this will throw an error numpy.linalg.LinAlgError: Singular matrix
print(f'Solution = {sol_2:.2f}')

d_2 = np.linalg.det(A_2)
print(f'Determinant = {d_2:.2f}')

