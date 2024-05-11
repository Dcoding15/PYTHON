#! /usr/bin/python3

def detmatrix(matrixA:list) -> list:
	row = len(matrixA)
	col = len(matrixA[0])
	if row != col:
		return "Operation can't performed because row and column are not same."
	else:
		det = 0
		pass
