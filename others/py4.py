#! /usr/bin/python3

'''
Q) Write a program to repeat characters with its numeric pair.

INPUT: B4A1D3
OUTPUT: BBBBADDD
'''

def fun():
	a = input('INPUT: ')
	c = '0'
	d, b = '', ''
	for i in a:
		if i.isalpha():
			d += b * int(c)
			c = '0'
			b = i
		else:
			c += i
	d += b * int(c)
	print('OUTPUT:',d)

fun()
