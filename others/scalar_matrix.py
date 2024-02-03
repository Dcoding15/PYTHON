#! /usr/bin/python3

def scalarmatrix():
	row = col = int(input('Enter order of square matrix: '))
	k = int(input('Enter a value: '))
	A = [[k if i == j else 0 for j in range(col)] for i in range(row)]
	return A

print(scalarmatrix())
