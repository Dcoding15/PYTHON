#! /usr/bin/python3

"""

Syntax for user defined function: -
--------------------------------

def function_name(function_parameter (optional)):
	''' doc string '''	(optional)
	statement / code
	return functio_value (optional)

Note: -
	(1) The number of argument must be matched.
	(2) The order is not important.
	(3) The keyword argument always comes after positional argument.
	(4) Default argument always comes after non-default argument.
	(5) We can put default argument both before and after the variable length argument.
	(6) We can take atmost one variable length argument.
	(7) Key=value pair argument should be last argument,
	(8) Default return value of function is None.

"""

'''

def f1(name):
	print('This is f1 function . . .')
	return 'My name is {}'.format(name)

f1('Debrishi')			#This is f1 function . . .

print(f1('Debrishi'))	#This is f1 function . . .
						#My name is Debrishi
'''

'''

# Keyword argument and positional argument

def add(a,b):
	print(a+b)

add(10,20)		#30
#add(a=10,20)	# This will give an SyntaxError which says first positional argument followed by keyword argument
add(10,b=20)	#30
add(a=10,b=20)	#30

'''

'''

# Default argument

def msg(name=None,age=0):
	print('My name is {} and I am {} yrs old.'.format(name,age))

msg()				#My name is None and I am 0 yrs old.
msg('Debrishi')		#My name is Debrishi and I am 0 yrs old.
msg(19)				# This will give wrong output because default argument should always last argument
msg('Debrishi',19)	#My name is Debrishi and I am 19 yrs old.

'''

'''

# Multiple Argument / Variable Length Argument

def fun(*var1):		# This parameter take multiple argument and return those argument as tuples.
	print(var1)

fun(1,2,3,4,5,6)	#(1, 2, 3, 4, 5, 6)

def fun1(**var2):	# This parameter take and return argument as key=value pairs as dictionaries.
	print(var2)

fun1(one=1, two=2, three=3, four=4, five=5, six=6)	#{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

def fun2(*var3,num):
	print(var3,end='  ')
	print(num)

fun2(1,2,3,4,5,num=100)		#(1, 2, 3, 4, 5)  100
#fun2(1,2,3,4,5,100)		# This will give TypeError as some missing argument

def fun3(num,*var4):
	print(num,var4,sep='  ')

fun3(100,10,20,30,40,50)	#100  (10, 20, 30, 40, 50)

def fun4(num,**var5):
	print(var5,end='  ')
	print(num)

fun4(num=100, one=1, two=2, three=3, four=4, five=5, six=6)		#{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}  100

'''

"""
Variable scopes in User Defined Function: -
----------------------------------------
	(1) Global variable: Those variables which are declared outside the user defined function.
		---------------

	(2) Local variable: Those variables which are declared inside the user defined function.
		--------------

		For example: -
		-----------
			a = 10			<--- This is global variable
			def f1():
				print(a)
			def f2():
				b = 20		<--- This is local variable
				print(b)
			def f3():
				global c	<--- This is global variable
				c = 30
				print(c)
"""

'''

# Recursion

# Write a program to calculate factorial using recursion.

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

for i in range(7):
	print(fact(i),end='  ')		#1  1  2  6  24  120  720

# Write a program to print fibonacci sequence.

def sum_fibo(n):
	if n < 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return (sum_fibo(n-1) + sum_fibo(n-2))

for i in range(10):
	print(sum_fibo(i),end='  ')		# 0  1  1  2  3  5  8  13  21  34

'''

"""

# Anonymous Functions / Lambda Functions

variable_name = lambda parameter_name : return_expression_or_condition

Note: -
	(1) It is compulsory to give parameter.
	(2) It is automatically going to return value.
	(3) It is a single line function.
	(4) It can't contain assignment operation.
"""

'''

# Write a program to calculate factorial using lambda function.

a = lambda n : 1 if n == 0 else n*a(n-1)

for i in range(7):
	print(a(i),end='  ')		#1  1  2  6  24  120  720

# Write a program to check weather a number is even or odd.

a1 = lambda n : True if n%2 == 0 else False
a2 = lambda n : False if n%2 == 0 else True
l = [i for i in range(10)]
b1 = filter(a1,l)
b2 = filter(a2,l)
print(list(b1))					#[0, 2, 4, 6, 8]
print(list(b2))					#[1, 3, 5, 7, 9]

'''

'''

# Function Aliasing

For existing function we can give another name.

Example:-
def sms(msg):
	print(msg)

sms1 = sms		#sms1 is pointing address of sms

sms1('Hello')	#Output: Hello

'''

'''

# Nested Function

Function inside another function. Inner function is local to outer function.

Example:-
def fun1():
    print('This is outer function.')
    def fun2():
        print('This is inner function.')
    fun2()	            #calling inner function
fun1()                  #calling outer function

Output: -
This is outer function.
This is inner function.

'''

'''

# Function can return value as another function

Note: Assigning function to a variable makes the variable also a function.

Example:-
def fun1():
    print('This is outer function.')
    def fun2():
        print('This is inner function.')
	return fun2         #returning function
x = fun1()					#assigning value of fun1() i.e., fun()
x()							#calling the assigned function

Output: -
This is outer function.
This is inner function.

'''

'''

# Function passing as argument to another function

Example:-
def fun(x):
    print(x())

def f1():
    return 'This is f1 function.'

fun(f1)         #passing f1() as argument
                #f1() and parameter of fun() i.e., x are pointing to same address

'''