import numpy as np

one_dimensional_array = np.array([1, 2, 3])
print(one_dimensional_array)
print(type(one_dimensional_array))
print(one_dimensional_array.shape)

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dimensional_array)
print(two_dimensional_array.shape)


# Create an array with 3 integers, starting from the default integer 0.
b = np.arange(3)
print(b)

# Create an array with 20 integers, starting from 1, incrementing by 3.
c = np.arange(1,20,3)
print(c)

# default dtype is float64 in np.linspace, so if we want int as dtype, we need to specify it
d = np.linspace(0,100,5,dtype=int)
print(d)
print(type(d))


e = np.arange(3,dtype=float)
print(e)
#
# NumPy did this internally:
# 	•	Detected Unicode string
# 	•	Longest string length = 24
# 	•	Allocated exactly 24 Unicode slots per element
#
# Think of it like this (C-style):
f = np.array(["Welcome to Maths for ML! asdsadada"])
print(f)
print(f.dtype) # this prints u24 what does it mean?
f[0] = "This string is definitely longer than 34 chars"
print(f) # this only prints the first 34 chars because when creating np array , the initial string was of 34 characters, and anything beyond that was truncated, that is how np array store strings

# Return a new array of shape 3, filled with ones.
ones_arr = np.ones(3)
print(ones_arr)

# Return a new array of shape 3, filled with zeroes.
zeros_arr = np.zeros(3)
print(zeros_arr)

# Return a new array of shape 3, without initializing entries.
empt_arr = np.empty(1)
print(empt_arr)

# Return a new array of shape 3 with random numbers between 0 and 1.
rand_arr = np.random.rand(3)
print(rand_arr)
# shape just prints the elements in the array in case of 1-D array
print(rand_arr.shape)
#ndim returns the number of dimensions in the array, in this case 1
print(rand_arr.ndim)



