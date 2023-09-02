#! /usr/bin/python3

'''
Q) Write a program to remove duplicate characters in given string.

INPUT: ABCDABCDFEFEEGHHGII
OUTPUT: ABCDFEGHI
'''

def fun():
	a = input('INPUT: ')
	b = []
	for i in a:
		if i not in b:
			b.append(i)
	del a
	a = ''.join(b)
	print('OUTPUT:',a)

fun()
