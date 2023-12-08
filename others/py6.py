#! /usr/bin/python3

'''
Q) Write a program to change the numeric value to character by adding value of ascii value of its alphabet pair with the numeric value.

INPUT: a4k3b2
OUTPUT:  aeknbd
'''

def fun():
	a = input('INPUT: ')
	b = ' '
	c = '0'
	d = ''
	for i in a:
		if i.isalpha():
			d += b + chr( ord(b) + int(c) )
			c = '0'
			b = i
		else:
			c += i
	d += b + chr( ord(b) + int(c) )
	d = d[2:]
	print('OUTPUT:',d)

fun()
