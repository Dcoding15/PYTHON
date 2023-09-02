#! /usr/bin/python3

# Example of method overriding

class A:
	def msg():
		print('This is method msg() before method overloading')

# Python doesn't support method overloading, it actually replace the localspace with new definition
	def msg():
		print('This is method msg() after method overloading')

class B(A):

# Method overriding
	def msg():
		print('This is method msg() after method overloading')

A.msg()
B.msg()
'''

Output: -

This is method msg() after method overloading
This is method msg() after method overloading

'''
