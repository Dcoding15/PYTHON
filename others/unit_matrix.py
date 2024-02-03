#! /usr/bin/python3

def unitmatrix():
	row = col = int(input('Enter order of square matrix: '))
	A = [[1 if i == j else 0 for j in range(col)] for i in range(row)]
	return A

print(unitmatrix())
