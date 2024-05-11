#! /usr/bin/python3

'''
Q) Write a program to sort characters present in the given string. First alphabet symbols and then numeric values.

INPUT: B4A1D3
OUTPUT: ABD134
'''

def fun():
	a = input('Enter string: ')
	b, c = '', ''
	i = 0
	for i in a:
		if i.isnumeric():
			b += i
		else:
			c += i
	del a
	a = ''.join(sorted(c) + sorted(b))
	print('OUTPUT:',a)

fun()
