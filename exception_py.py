#! /usr/bin/python3

'''
Exception: It is an event which occurs during the execution of a program that interrupts the normal flow of program. It is an python object that represent as an error.

n = eval(input('Enter a number: '))
d = eval(input('Enter a number: '))
try:	# try block will execute as normal flow of program
	r = n / d
except Exception as e:	# except block will catch error
	print(e)
else:	# else will execute if except block doesn't catch any error
	print('Result:',r)
finally:	# Final block will always executed
	print('final block will always executed')
'''
