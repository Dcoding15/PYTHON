#! /usr/bin/python3

def f1():
# add two numbers using eval()
	a = eval(input('Enter 1st number: '))
	b = eval(input('Enter 2nd number: '))
	print('The sum is',(a+b))

def f2():
# adding multiple values
	a = 0
	for i in input('Enter multiple values: ').split():
		a += int(i)
	print('The sum is',a)

f1()
f2()
