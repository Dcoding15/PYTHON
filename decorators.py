#! /usr/bin/python3

'''
Decorator: -
---------
	1. It is also known as wrapper function.
	2. It takes input as function and return function after adding some additional functionality.
	3. If there is inner function in decorator then inner function is going to call itself.
	4. It is compulsory to take function as input and return function as output.
	5. Inner function is pointing to parameter of decorator function.
	6. We can call function without actual decorator by assigning decorator_name(function_name) to variable_name and use that variable as function.

	Example:-
	def deco(x):
        def func():                                     #func() will call itself
            print('This is an example of decorator.')
            x()
        return func
	@deco
	def f1():                                           #f1() is pointing to parameter of deco(x)
	    print('This is f1()')
	f1()

	Output: -
	This is an example of decorator.
	This is f1()
'''