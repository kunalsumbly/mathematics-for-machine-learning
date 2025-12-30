import numpy as np

arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])
addition = arr_1 + arr_2
# this changed a 2-D array into 1-D array
print(addition)

subtraction = arr_1 - arr_2
print(subtraction)

division = arr_1 / arr_2
print(division)

multiplication = arr_1 * arr_2
print(multiplication)

vector = np.array([1, 2, 3])
vector = vector * 1.6
print(vector)

# 1-D array
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(
                one_dim_arr, # the array to be reshaped
               (2,3) # dimensions of the new array
              )
# Print the new 2-D array with two rows and three columns
print(multi_dim_arr)

# 2-D array
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b.shape) # (2,3) 2 rows and 3 columns
print(b.ndim) # 2

# 3-D arrays
c = np.array([[[1,2,3],[4,5,6]]])
# shape returns the shape of the array, in this case (1,2,3) which means
print(c.shape)
print(c.ndim)

# array indexing
print(c[0])
print(c[0][0])
print(c[0][1])
print(c[0][0][0])

d= np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(d.shape)
e = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(e.shape)

# 4-D array
f = np.array([[[[1,2],[3,4]],[[5,6],[7,8]]]])
print(f.shape)
print(f.ndim)

# Array Slicing 1-D
a = ([1, 2, 3, 4, 5])
print(a[1:3])
print(a[1:])
print(a[:])
print(a[:4:2])
print(a[::2])
print(a[1::2])


#  Array Slicing 2-D
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(b[0, 1:4])
print(b[0:2])


# Indexing on a 2-D array
two_dim = np.array(([1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]))
# gives first two rows
print(two_dim[:2])
# gives last two rows
print(two_dim[1:3])
# prints 1st column
print(two_dim[:,1])


#Stacking arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))
print(c)
d = np.hstack((a, b))
print(d)

a1 = np.array([[1,1],
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])
print(f'a1:\n{a1}')
print(f'a2:\n{a2}')
print(np.vstack((a1, a2)))
