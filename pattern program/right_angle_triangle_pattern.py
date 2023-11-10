def pattern1(n):
    '''To print right angle triangle with * symbol'''
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()

def pattern2(n):
    '''To print right angle triangle pattern with digit starting from 1 (each digit each row) in ascending order'''
    for i in range(n):
        for j in range(i+1):
            print(str(i+1),end=' ')
        print()

def pattern3(n):
    '''To print right angle triangle pattern with alphabet starting from A (each alphabet each row) in ascending order'''
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=' ')
        print()

def pattern4(n):
    '''To print right angle triangle pattern with digit starting from 1 (each digit each column) in ascending order'''
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=' ')
        print()

def pattern5(n):
    '''To print right angle traingle pattern with alphabet starting from A (each alphabet each column) in ascending order'''
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end=' ')
        print()

def pattern6(n):
    '''To print right angle triangle pattern with digit ending to 1 (each digit each column) in descending order'''
    for i in range(n):
        for j in range(i+1):
            print(n-j,end=' ')
        print()

def pattern7(n):
    '''To print right angle traingle pattern with alphabet ending to A (each alphabet each column) in descending order'''
    for i in range(n):
        for j in range(i+1):
            print(chr(64+n-j),end=' ')
        print()

#pattern1(5)
#pattern2(5)
#pattern3(5)
#pattern4(5)
#pattern5(5)
#pattern6(5)
#pattern7(5)