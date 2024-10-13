#! /usr/bin/python3

def columnmatrix():
	row = int(input('Enter no. of rows: '))
	col = 1
	A = [[int(input(f'Enter element for row {i+1}, column {j+1}: ')) for j in range(col)] for i in range(row)]
	return A

print(columnmatrix())
