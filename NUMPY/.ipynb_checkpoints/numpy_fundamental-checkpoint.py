#! /usr/bin/python3.11
import numpy as np

# Numpy is used to work with array. The array object in Numpy is called ndarray.
'''
print(arr)
print("Version: ",np.__version__)
'''

# There are 6 general mechanism of creating array: -
# 1. python array -> numpy array
'''
arr1 = np.array([1,2,3,4,5,6])
print(arr1)
'''
# 2. Intrinsic numpy array
# For 1d array - linespace(start, end, no._sample), arange(start, end, step/data type),
# Note 1: No. of evenly spaced sample in linspace is 50 and it should be integer type and also provide start and end argument.
# Note 2: Start and step are optional in arange.
print("This is an example of np.arange -->",np.arange(10))
print("This is an example of np.arange -->",np.arange(1,10))
print("This is an example of np.arange -->",np.arange(1,10,.5))
print("This is an example of np.linspace -->",np.linspace(1.5,10.5))
# For 2d array - 

# 3. 

# Different dimensions of array
# Using ndim (int) as argument in np.array(), we can create higher dimensions of ndarray.
'''
a = np.array(42)    # 0-dimensional array
b = np.array([1, 2, 3, 4, 5])   # 1-dimensional array
c = np.array([[1, 2, 3], [4, 5, 6]])    #2-dimensional array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # 3-dimensional array

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
'''
# Accessing array
# N-dimensional array required N no. of sequence to access a particular element element.
# Negative indexing start access from last element of array
'''
print(a)
print(b[1])
print(c[0,1])
print(d[0,0,1])
'''
# Slicing array: varible_name[start : end : step]
'''
Data Type in NumPy: -
------------------
i - integer
u - unsinged integer

f - float
c - complex float

b - boolean

m - timedelta
M - datetime

O - object

S - string
U - unicode string

V - fixed chunck of memory
'''

# To know data type of NumPy array: .dtype
# To set data type of NumPy array: dtype='[ data type in NumPy ]' within np.array()
# To convert existing data type into another data type: astype('[ Data type in NumPy ]')
'''
a1 = np.array([1.2,2.3,3.4,4.5,5.6])
print(a1)
print(a1.dtype)

a2 = a1.astype('i')
print(a2)
print(a2.dtype)
'''

# Array Copy vs View
# Copy of array means copying original array to new array. Change made to new array will not affect the original array.
# View of array means viewing of original array to new array. Changes made to new array will affect the original array.
# To know if array owns its data: .base
# Example of copy of array
'''
a1 = np.array([1,2,3,4,5])
a2 = a1.copy()
a2[0] = 1000
print(a1)
print(a2)
print(a2.base)
'''
# Example of view of array
'''
a1 = np.array([1,2,3,4,5])
a2 = a1.view()
a2[0] = 1000
print(a1)
print(a2)
print(a2.base)
'''

# Shape of Array (Dimension of array)
# The shape of array is the number of elements in each dimension.
# Using ndmin attribute we can create n dimensional array.
'''
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.shape)
arr1 = arr.copy()
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],ndmin=5)
print(arr.shape)
'''

# Reshaping of Array
# Changing dimension by shifting array elements.
# Reshape from 1-D to 2-D
arr = np.array([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19])
a1 = arr.copy()
a1 = a1.reshape(6,3)
print(a1.shape)
# Reshape from 1-D to 3-D
a2 = arr.copy()
a2 = a2.reshape(2,3,3)
print(a2.shape)
# Reshape from N-D to 1-D
a3 = a2.copy()
a3 = a3.reshape(-1)
print(a3.shape)