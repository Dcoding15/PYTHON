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
