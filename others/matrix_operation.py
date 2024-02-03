#! /usr/bin/python3

def checkOrder(matrixA:list, matrixB:list) -> bool:
	ai = len(matrixA)
	aj = len(matrixA[0])
	bi = len(matrixB)
	bj = len(matrixB[0])
	if ai == bi and aj == bj:
		return True
	else:
		return False

def checkOrderForMultiplication(matrixA:list, matrixB:list) -> bool:
	row = len(matrixB)
	col = len(matrixA[0])
	if row == col:
		return True
	else:
		return False

def matrix_addition(matrixA:list, matrixB:list) -> list:
	if checkOrder(matrixA, matrixB):
		row = len(matrixA)
		col = len(matrixA[0])
		C = [[ (matrixA[i][j] + matrixB[i][j]) for j in range(col)] for i in range(row)]
		return C
	else:
		return "Operation can't be performed because matrices are not in same order."


def matrix_subtraction(matrixA:list, matrixB:list) -> list:
	if checkOrder(matrixA, matrixB):
		row = len(matrixA)
		col = len(matrixA[0])
		C = [[ (matrixA[i][j] - matrixB[i][j]) for j in range(col)] for i in range(row)]
		return C
	else:
		return "Operation can't be performed bacause matrices are not in same order."

def matrix_transpose(matrixA:list) -> list:
	row = len(matrixA)
	col = len(matrixA[0])
	C = [[ matrixA[j][i] for j in range(row)] for i in range(col)]
	return C


def matrix_scalar_multiplication(matrixA:list, k:int) -> list:
	row = len(matrixA)
	col = len(matrixA[0])
	C = [[ (k*matrixA[i][j]) for j in range(col)] for i in range(row)]
	return C

def matrix_multiplication(matrixA:list, matrixB:list) -> list:
	if checkOrderForMultiplication(matrixA, matrixB):
		row = len(matrixA)
		col = len(matrixB[0])
		tmp = 0
		C = []
		for k in range(col):
			for i in range(row):
				for j in range(col):
					tmp += (matrixA[i][j] * matrixB[j][k])
				C.append(tmp)
				tmp = 0
		D = [[ j for j in C[i:col+i]] for i in range(0,row*col,col)]
		C = matrix_transpose(D)
		return C
	else:
		return "Operation can't be performed because Matrix A' column is not equal to Matrix B's row."


A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[11,22,33],[44,55,66],[77,88,99]]
print('A =',A,'and B =',B)
print('Matrix Addition of matrix A and B:    ',matrix_addition(A,B))
print('Matrix Subtraction of matrix A and B: ',matrix_subtraction(B,A))
print('Transpose of matrix A:                ',matrix_transpose(A))
print('Transpose of matrix B:                ',matrix_transpose(B))
print('Scalar Multiplication of matrix A:    ',matrix_scalar_multiplication(A,2))
print('Scalar Multiplication of matrix B:    ',matrix_scalar_multiplication(B,2))
print('Matrix Multiplication of A and B:     ',matrix_multiplication(A,B))
