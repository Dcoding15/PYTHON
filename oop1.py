#! /usr/bin/python3

# Method chaining: When we call multiple method subquentially each call performs an action on same object and return self

class A:
	def f1(self):
		print('This is method f1')
		return self

	def f2(self):
		print('This is method f2')
		return self

	def f3(self):
		print('This is method f3')
		return self

A().f1().f2().f3()
'''

Output: -

This is method f1
This is method f2
This is method f3

'''
