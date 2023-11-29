#! /usr/bin/python3

'''
Q) Write a program to print different vowels present in the given word

INPUT: durgasoftwaresolutions
OUTPUT: ['a', 'e', 'i', 'o', 'u']
'''

a = set(input('INPUT: '))
b = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sorted(a&b)
print('OUTPUT:',c)
