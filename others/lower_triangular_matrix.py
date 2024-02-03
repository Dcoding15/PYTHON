#! /usr/bin/python3

def lowertrianglematrix():
	row = col = int(input('Enter order of square matrix: '))
	A = [[0 if i < j else int(input(f'Enter element for row {i+1}, column {j+1}: ')) for j in range(col)] for i in range(row)]
	return A

print(lowertrianglematrix())
