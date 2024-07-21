#! /usr/bin/python3.11
import numpy as np

# Zero array - array filled with only 0's element
zero_arr = np.zeros((2,3),dtype='i')
print(zero_arr)

# Ones array - array filled with only 1's element
ones_arr = np.ones((2,3),dtype='i')
print(ones_arr)

# Empty array - array filled with values of previous used memory
empty_arr = np.empty((2,3),dtype='i')
print(empty_arr)

# Range array - array filled with elements starting from 0
range_arr = np.arange(1,20,2,dtype='i')
print(range_arr)

# Diagonal array - array where diagonal element filled with 1's
diagonal_arr = np.eye(2,3,dtype='i')
print(diagonal_arr)

# linear spaced array - array with values that are spaced linearly in a specified interval
linear_space_arr = np.linspace(1,10,num=3,dtype='i')
print(linear_space_arr)