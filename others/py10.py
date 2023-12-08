#! /usr/bin/python3

'''
Write a program to enter name and marks in dictionary and display information on the screen.

INPUT:
OUTPUT:
'''
from os import system
d={}
while True:
	system('clear')
	name=input('\nEnter name: ')
	marks=float(input('Enter marks: '))
	d[name]=marks
	system('clear')
	print('Student record inserted sucessfully !!!\n')
	while True:
		opt=input('Do you want to enter one more [ Y | N ]: ')
		if opt.upper() == 'N':
			opt='N'
			system('clear')
			break
		elif opt.upper() == 'Y':
			system('clear')
			break
		else:
			system('clear')
			print('\nPlease enter valid option !!!\n')
	if opt.upper() == 'N':
		break

print('\n',d)
