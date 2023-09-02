#! /usr/bin/python3

# Function: abs()
# Convert any number into positive number.
# Function: round(number, roundoff)
# Return a floating point number rounded to the specified number of digits. By default it will only roundoff upto only one digit.
'''
print(abs(-1234.65))	#1234.65
print(abs(23.445))		#23.445
print(round(11.43, 1))		#11.4
print(round(11.455, 2))		#11.46
print(round(11.5))			#12
'''

# Function: all()
# Return False if any element in iterable object is 0, None, False, otherwise True.
# Function: any()
# Return True if any element in iterable object is 1-9, True, otherwise False.
'''
print(any([1,2,False,4])) #True
print(any([1,2,0,4]))     #True
print(any([1,2,None,4]))  #True
print(any([1,2,3,4,5]))   #True
print(all([1,2,False,4])) #False
print(all([1,2,0,4]))     #False
print(all([1,2,None,4]))  #False
print(all([1,2,3,4,5]))   #True
'''


'''

'''

# Function: bin()
# Convert any integer into base 2 number.
# Function: hex()
# Convert any integer into base 16 number.
# Function: oct()
# Convert any integer into base 8 number.
'''
print(bin(123))		#0b1111011
print(hex(123))		#0x7b
print(oct(123))		#0o173
'''

# Function: bytes(value, encoding)
# Note: encoding are 'utf-8' | 'utf-16' | 'utf-32'. Only integer, boolean, character can be converted into bytes
# Convert return into bytes. Bytes only contain ASCII characters.
# Function: bytearray(iterable_object, encoding)
# Convert iterable_object into bytes.
'''
print(bytes(True))				#b'\x00'
print(bytes(False))				#b''
print(bytes(10))				#b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(bytes('a','utf-8'))		#b'a'
print(bytes('a','utf-16'))		#b'\xff\xfea\x00'
print(bytes('a','utf-32'))		#b'\xff\xfe\x00\x00a\x00\x00\x00'
print(bytearray([12,43,65,78,24]))	#bytearray(b'\x0c+AN\x18')
print(bytearray((12,43,65,78,24)))	#bytearray(b'\x0c+AN\x18')
print(bytearray({12,43,65,78,24}))	#bytearray(b'A\x18+\x0cN')
'''

# Function: callable()
# Return True if specified is object, otherwise False.
'''
def x():
	return 30
y=lambda x: x+1
z=1234
print(callable(x))	#True
print(callable(y))	#True
print(callable(z))	#False
'''

# Function: ascii()
# Return non-ascii characters with escape character.
# Function: chr()
# Convert ASCII and ALT code into character.
# Function: ord()
# Convert character into ASCII and ALT code.
'''
print(ascii('α')) 	'\u03b1'
print(ascii('a')) 	#'a'
print(ord('₹'))		#8377
print(ord('a'))		#97
print(chr(8377))	#₹
print(chr(97))		#a
'''


# Function: classmethod()
# Convert function/method into class method.
# Function: getattr(object, name, value)
# Return the value of specified attribute of an object.
# Function: setattr(object, name, value)
# Set the specified attribute or value of an object.
# Function: delattr(object, name)
# Delete specified attribute of an object.
# Note: If the object has specified attribute is not present then we can create by giving attribute name and value using getattr() and setattr()
# Function: isinstance(object, type)
# Return True if the specified object is of the specified type, otherwise False.
# Function: issubclass(sub_class/derived_class, super_class/base_class)
# Return True if the specified if sub_class is inherited from super_class, otherwise False.
# Function: object()
# Function: property()
# Function: super()
# Function: staticmethod()
'''
def x():
	return 'This is function'
class A:
	def A(self):
		pass
	def msg(self):
		return 'This is method'
print(type(A().msg))					#<class 'method'>
print(type(x))							#<class 'function'>
print(type(classmethod(A().msg())))		#<class 'classmethod'>
print(type(classmethod(x)))				#<class 'classmethod'>
'''
'''
class A:
	pass
class B(A):
	pass
print(issubclass(B, A))									#True
print(isinstance(12, complex))							#False
print(isinstance(12, int))								#True
print(isinstance(20+45j, (list, int, str, tuple)))		#False
class A:
	def msg(self):
		pass
x = A()
print(isinstance(x, A))									#True
'''
'''
class A:
	name = 'Debrishi'
	age = 18

obj = A()
print(getattr(obj, 'name'))			#'Debrishi'
print(getattr(obj, 'gender', 'Male'))	#'Male'
setattr(obj, 'gender', 'Male')
setattr(obj, 'name', 'Biwas')
delattr(obj, 'age')
print(getattr(obj,'age'))
'''

# Function: compile(source, filename, mode)
# Return the specified source as a code object which is ready to be executed.
# Function: exec(source_object)
# Execute the specified source object. Its return type is None.
'''
a = ""print('Hello, World!')""
b = compile(a,'builtin_function','exec')
exec(b)
'''

# Function: list()
# Function: tuple()
# Function: set()
# Function: dict()
# Function: str()
# Function: frozenset()
# Convert iterable object into frozenset object
'''
def fun(n):
	for i in n:
		print(i, end=" ")
a = frozenset({1,2,3,4,5,6})
b = frozenset([1,2,3,4,5,6])
c = frozenset((1,2,3,4,5,6))
d = frozenset("123456")
e = frozenset({'a':1, 'b':2, 'c':3, 'd':4})
fun(a)	#1 2 3 4 5 6
fun(b)	#1 2 3 4 5 6
fun(c)	#1 2 3 4 5 6
fun(d)	#3 2 6 1 5 4
fun(e)	#a d b c
'''
# Function: range(start, end, step)
# Returns sequnce of values.
'''
print(list(range(11)))		#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))	#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,21,2)))	#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
'''

# Function: dir(object)
# Return a list of object's property and methods.
'''
class A:
	def __dir__(self):
		return [10, 20, 30, 40, 50]

obj = A()
print(dir(obj)) #[10, 20, 30, 40, 50]

l = [10,20,30,40,50]
#l = []
print(dir(l))
'''



# Function: enumerate()
# Convert iterable object into enum object.
'''
l = ['Kolkata', 'Mumbai', 'Chennai', 'Guahati']
e = enumerate(l)
print(list(e)) #[(0, 'Kolkata'), (1, 'Mumbai'), (2, 'Chennai'), (3, 'Guahati')]
'''

# Function: eval()
# Evaluate expression and various data types.
'''
x = 5
print(eval("2*x*x+3*x+6"))	#71
'''

# Function: filter(argument_function, iterable_object)
# To exclude items from iterable object.
# Function: map(argument_function, iterable_object)
# Return result of funtion applied with every item of iterable object.
'''
a = [10, 50, 60, 80, 90, 5, 45, 65]
def fun(n):
	if n >= 60:
		return False
res = filter(fun, a)
print(list(res))	#[60, 80, 90, 65]
'''
'''
def mul_2(n):
	return n*2
x = [1,2,3,4,5,6,7,8,9]
y = map(mul_2, x)
print(list(y))	#[2, 4, 6, 8, 10, 12, 14, 16, 18]
'''

# Function: bool()
# Convert any non empty value into True, otherwise False.
# Function: float()
# Retuen a floating point number.
# Function: int()
# Return an integer number.
# Function: complex()
# Return a complex number.
'''
print(bool(False))					#False
print(bool(None))					#False
print(bool(0))						#False
print(bool())						#False
print(bool('Hello'))				#True
print(complex(12+45j))				#(12+45j)
print(complex(34.65+45.66j))		#(34.65+45.66j)
print(complex('12.54+23.87j'))		#(12.54+23.87j)
print(complex('hello!@#00'))		#
print(float(123))	 				#123.0
print(float(123.54)) 				#123.54
print(float('12.43'))				#12.43
print(float('hello!@#00'))			#only numeric string can be converted into float
print(float('23+56j'))				#complex can't be converted into float
print(float(bytes(30)))				#byte can't be converted into float
print(int(12.365))					#12
print(int(56+45j))					#complex can't be converted into integer
print(int('123'))					#123
print(int('hello!@#00'))			#only numeric string can be converted into integer
print(int(bytes(30)))				#byte can't be converted into integer
'''

# Function: format(value, format_specifier)
# Represent the value into a specified format.
'''
Format specifier: -
[[fill]align][sign][#][0][width][,][.precision][type]
where, the options are
fill        ::=  any character
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
'''
'''
print(format(123, 'd'))    	#123
print(format(123.65, 'f')) 	#123.650000
print(format(97, 'c')) 		#a
print(format(12, 'e'))	    #1.200000e+01
'''

# Function: id()
# Return memory address of the object.
# Function: memoryview()
# Note: memoryview need byte like object only.
# Return a memory view object.
'''
s1 = (65,66,67,68)
s2= 'ABCD'
encode = 'utf-8'
a = bytearray(s1)
b = bytearray(s2, encode)
m = memoryview(a)
n = memoryview(b)
for i in range(len(s1)):
	print(chr(m[i]),'=',m[i],end=' | ')
print()
# Output: ã = 227 | § = 1677
for i in range(len(s2)):
	print(chr(n[i]),'=',n[i],end=' | ')
print()
# Output: A = 65 | B = 66 | C = 67 | D = 68
x = (10,20,30,40)
print(id(x))	#140467253009504
'''

# Function: iter()
# Returns an iterator object.
# Function: next()
# Return next item in iterable object.
'''
city = ('Kolkata', 'Delhi', 'Mumbai', 'Chennai', 'Noida')
a = iter(city)
print(next(a), end=" ")
print(next(a), end=" ")
print(next(a), end=" ")
print(next(a), end=" ")
print(next(a), end=" ")
# Output: Kolkata Delhi Mumbai Chennai Noida
'''

# Function: len()
# Return the length of an iterable object.
# Function: max()
# Return the largest item from iterable.
# Function: min()
# Return the smallest item from iterable.
# Function: sum()
# Return the sum of items of an iterable object.
# Function: pow(base_value, power_value)
# Return the value after base value to the power value.
# Function: divmod()
# Return (quotient, remainder) as tuple
'''
l = [10,'hello',12.32,12+32j]
print(len(l))		#4
print(len(l[0]))	#It doesn't return any length because int, float, complex, bool has no length
s = 'hellomynameisABC'
print(max(s))	#y
print(min(s))	#A
l = (1,4,3,2,5,7,6,9,8)
print(max(l))	#9
print(min(l))	#1
print(sum(l))	#45
print(divmod(5, 10))	  #(0, 5)
print(divmod(10, 5))	  #(2, 0)
print(divmod(5.6, 23.4)) #(0.0, 5.6)
print(divmod(23.4, 5.6)) #(4.0, 1.0)
print(pow(2,4))	#16
print(pow(4,0))	#1
print(pow(8,3))	#512
'''

# Function: reversed()
# Return iterable object of reverse orderd element.
# Function: Sorted()
# Return list with element sorted in ascending order.
'''
l = 9,8,5,6,7,3,2,7,1,4
k = reversed(l)
j = sorted(l)
print(list(k))	#[4, 1, 7, 2, 3, 7, 6, 5, 8, 9]
print(j)		#[1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
'''

# Function: slice(start_index, stop_index - 1, step_size)
# Return a slice object that is used to slice any sequence.
'''
s = 'Debrishi Biswas'
print(s[slice(0,8)])		#Debrishi
print(s[slice(0,8,2)])		#Dbih
'''

# Function: zip()
# Return iterable object (iterator) from two or more iterator.
'''
l = [1,2,3,4,5]
s = ['moon','sun','star','earth','space']
c = ['kolkata','delhi','chennai','mumbai','indore']
z = zip(l,s,c)
print(list(z))	#[(1, 'moon', 'kolkata'), (2, 'sun', 'delhi'), (3, 'star', 'chennai'), (4, 'earth', 'mumbai'), (5, 'space', 'indore')]
'''

# Function: globals()
# Function: locals()
