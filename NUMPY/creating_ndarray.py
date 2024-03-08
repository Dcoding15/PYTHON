import numpy as np

# Numpy is used to work with array. The array object in Numpy is called ndarray.
arr = np.array([1,2,3,4,5,6])

print(arr)
print("Version: ",np.__version__)


# Different dimensions of array
# using ndim as argument in np.array(), we can create higher dimensions of ndarray.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
