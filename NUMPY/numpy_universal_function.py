#!/usr/bin/bash
import numpy as np

'''
ufuncs: It stands for "Universal Functions" which operate on ndarray object.
zip(): Without ufuncs we can operate ndarray object using zip() and for loop.
'''

# Example of zip()
'''
a = np.array([1,2,3,4,5],dtype='i')
b = np.array([11,22,33,4,55],dtype='i')
z = np.empty(5,dtype='i')
k = 0
for i,j in zip(a,b):
    z[k] = i+j
    k += 1
print(z)
'''

# Creating own ufunc
# frompyfunc(function_name, input_array_size, output_array_size)
'''
def fun1(a, b):
    return a+b
x = np.frompyfunc(fun1,2,1)
print(x([1,2,3,4,5],[11,22,33,44,55]))
'''

# Simple Arithematic
a = np.array([1,2,3,4,5,6],dtype='f')
b = np.array([10,20,30,40,50,60],dtype='f')
# Addition
arr1 = np.add(a,b)
# Subtraction
arr2 = np.subtract(b,a)
# Multiplication
arr3 = np.multiply(a,b)
# Division
arr4 = np.divide(a,b)
# Power
arr5 = np.power(b,a)
# Remainder
arr6 = np.remainder(a,b)
# Quotient and Mod
arr7 = np.divmod(b,a)
# Absolute Values
arr8_1 = np.absolute(a)
arr8_2 = np.absolute(b)
# Reciprocal
arr9 = np.reciprocal(a)
print(arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8_1,arr8_2,arr9,sep="\n")

# Rounding Decimals
# Turncation - return fractional part to zero
a = np.trunc([3.1666, 3.6667])
b = np.fix([3.1666, 3.6667])
print(a,b,sep='\n')

# Rounding - increment by 1 if fractional part is greater than and equal to 5.
a = np.around([3.1666, 3.6667])
print(a)

# Floor - return largest integer which is less than or equal to number
a = np.floor([3.7, -1.2])
print(a)

# Ceil - return smallest integer which is greater than or equal to number
a = np.ceil([3.7, -1.2])
print(a)

# Logs
a = 5
# Log at base 2
print(np.log2(a))

# Log at base 10
print(np.log10(a))

# Log at base e (Natural Log)
print(np.log(a))
