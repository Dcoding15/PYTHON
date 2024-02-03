#! /usr/bin/python3

def diagonalmatrix():
	row = col = int(input('Enter order of square matrix: '))
	A = [[int(input(f'Enter element for row {i+1}, column {j+1}: ')) if i == j else 0 for j in range(col)] for i in range(row)]
	return A

print(diagonalmatrix())
