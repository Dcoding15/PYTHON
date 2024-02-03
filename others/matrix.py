#! /usr/bin/python3

def squarematrix() -> list:
	row = col = int(input('Enter order of square matrix: '))
	A = [[int(input(f'Enter element for row {i+1}, column {j+1}: ')) for j in range(col)] for i in range(row)]
	return A

def nonsquarematrix() -> list:
	row = int(input('Enter no. of rows: '))
	col = int(input('Enter no. of columns: '))
	A = [[int(input(f'Enter element for row {i+1}, column {j+1}: ')) for j in range(col)] for i in range(row)]
	return A

print(squarematrix())
print(nonsquarematrix())
