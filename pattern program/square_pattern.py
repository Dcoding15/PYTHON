def pattern1(n):
	'''To print given no. of * symbol in a row'''
	for i in range(n):
		print('*',end=' ')
	print()

def pattern2(n):
    '''To print square pattern of * symbol'''
    for i in range(n):
        print('* '*n)

def pattern3(n):
	'''To print square pattern with same digit'''
	for i in range(n):
		print((str(n)+' ')*n)

def pattern4(n):
	'''To print square pattern with digit starting from 1 (each number for each row) in ascending'''
	for i in range(n):
		print((str(i+1)+' ')*n)

def pattern5(n,a):
	'''To print square pattern with same alphabet'''
	for i in range(n):
		print((str(a)+' ')*n)

def pattern6(n):
    '''To print square pattern with alphabet starting from A (each alphabet for each row) in ascending order'''
    for i in range(n):
        print((chr(65+i)+' ')*n)

def pattern7(n):
    '''To print square pattern with digit starting from 1 (each digit for each column) in ascending order'''
    for i in range(n):
        for j in range(1,n+1):
            print(j,end=' ')
        print()

def pattern8(n):
    '''To print square pattern with alphabet starting from A (each alphabet for each column) in ascending order'''
    for i in range(n):
        for j in range(n):
            print(chr(65+j),end=' ')
        print()

def pattern9(n):
    '''To print square pattern with digit ending to 1 (each digit for each row) in decending order'''
    for i in range(n):
        print((str(n-i)+' ')*n)

def pattern10(n):
    '''To print square pattern with alphabet ending to A (each digit for each row) in decending order'''
    for i in range(n):
        print((chr(64+n-i)+' ')*n)

def pattern11(n):
    '''To print square pattern with digit ending to 1 (each digit for each column) in decending order'''
    for i in range(n):
        for j in range(n):
            print(str(n-j),end=' ')
        print()

def pattern12(n):
    '''To print square pattern with alphabet ending to A (each digit for each column) in decending order'''
    for i in range(n):
        for j in range(n):
            print(chr(64+n-j),end=' ')
        print()

#pattern1(5)
#pattern2(5)
#pattern3(5)
#pattern4(5)
#pattern5(5,'A')
#pattern6(5)
#pattern7(5)
#pattern8(5)
#pattern9(5)
#pattern10(5)
#pattern11(5)
#pattern12(5)