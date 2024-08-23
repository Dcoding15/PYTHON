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
print('\nSimple Arithematic')
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
print('\nRounding Decimals')
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
print('\nLogs')
a = 5
# Log at base 2
print(np.log2(a))

# Log at base 10
print(np.log10(a))

# Log at base e (Natural Log)
print(np.log(a))

# Summations
print('\nSummation')
a = [1,2,3,4,5]
b = [6,7,8,9,0]
print(np.sum(a))

# Summation Over an Axis
print(np.sum([a,b],axis=1))

# Cummulative Sum
print(np.cumsum(a))

# Products
print(np.prod(a))

# Product Over an Axis
print(np.prod([a,b],axis=1))

# Cummulative Products
print(np.cumprod(a))

# Differences
a = [10,15,25,5]
print(np.diff(a))
print(np.diff(a,n=3))	# where n is no. of iterations

# LCM - Lowest Common Multiple
print('\nLowest Common Multiple')
a = 4
b = 6
print(np.lcm(a,b))
a = [2,4,6,8,10,12]
# reduce() -> convert n dimension array by reducing 1 dimension
print(np.lcm.reduce(a))

# GCD - Greatest Common Denominator
print('\nGreatest Common Denominator')
a = 4
b = 6
print(np.gcd(a,b))
a = [2,4,6,8,10,12]
print(np.gcd.reduce(a))

# Trigonometric Functions
# PI constant
print('\nPI constant')
print(np.pi)

print('\nTrigonometric Functions')
# sine function
print(np.sin(30))

# cosine function
print(np.cos(30))

# tangent function
print(np.tan(30))

# Convert degree into radian
print('\nConvert degree into radian')
a = [15, 30, 45, 60, 90, 180, 270, 360]
print(np.deg2rad(a))

# Convert radian into degree
print('\nConvert radian into degree')
a = [np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]
print(np.rad2deg(a))

# Finding Angles
print('\nFinding Angles')
# arc sine function
print(np.arcsin(1))

# arc cosine function
print(np.arccos(1/2))

# arc tangent function
print(np.arctan(1))

# Hypotenues
print('\nHypotenues')
base = 3
perpendicular = 4
print(np.hypot(base, perpendicular))

# Hyperbolic Functions
'''

sinh(x) = (e^x - e^(-x))/2
cosh(x) = (e^x + e^(-x))/2
tanh(x) = (e^(2x) - 1)/(e^(2x) + 1)

'''
print('\nHyperbolic Functions')
# hyperbolic sine function
print(np.sinh(np.pi/2))

# hyperbolic cosine function
print(np.cosh(np.pi/2))

# hyperbolic tangent function
print(np.tanh(1))

# Finding Hyperbolic Angles
print('\nFinding Hyprbolic Angles')
# arc hyperbolic sine function
print(np.arcsinh(1.0))

# arc hyperbolic cosine function
print(np.arccosh(1.5))

# arc hyperbolic tangent function
print(np.arctanh(0.23))

# Set Operations
print('\nSet Operations')
# find unique elements from any array
print(np.unique([1,1,1,2,3,4,5,5,6,7,7,7,8,8,9]))
a = [1,2,3,4]
b = [3,4,5,6]
# Union - values that are present in both sets
print(np.union1d(a,b))

# Intersection - values which is common between two sets
print(np.intersect1d(a,b))

# Difference - values in first that are NOT present in second set
print(np.setdiff1d(a,b))

# Symmetric Difference -  values that are NOT present in both sets
print(np.setxor1d(a,b))
