#! /usr/bin/python3

def rowmatrix():
	row = 1
	col = int(input("Enter no. of column: "))
	A = [[int(input(f'Enter element for row {i+1}, column {j+1}: ')) for j in range(col)] for i in range(row)]
	return A

print(rowmatrix())
