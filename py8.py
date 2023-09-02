#! /usr/bin/python3

'''
Q) Write a program to count duplicate characters in given string.

INPUT: ABCDABCDFEFEEGHHGII
OUTPUT: {'A': 2, 'B': 2, 'C': 2, 'D': 2, 'F': 2, 'E': 3, 'G': 2, 'H': 2, 'I': 2}
'''

def fun():
	a = input('INPUT: ')
	b = dict({})
	for i in a:
		if i in b.keys():
			b[i] += 1
		else:
			b.update({i : 1})
	print('OUTPUT:',b)

fun()
