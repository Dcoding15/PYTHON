#! /usr/bin/python3
'''
Accessing one class member into another class member using object reference
---------------------------------------------------------------------------
'''
'''
class A:
	def setUnit(self):
		self.a=int(input())
		self.b=int(input())
class Rect:
	def getArea(a,b):
		print(a*b)
	def getPerimeter(a,b):
		print(2*(a+b))
x=A()
x.setUnit()
Rect.getArea(x.a,x.b)
Rect.getPerimeter(x.a,x.b)
'''

'''
Inner Class: -
-----------
	1. It is a class which is declared within another class.
	2. Inside inner class we can also create inner class.
	3. It will have security and modularity of application.
'''
'''
class A:		#Outer Class
	a = 10
	b = 'ABC'
	class B:	#Inner Class
		c = 12.23
x = A()
y = A().B()		#Without outer class accessing inner class is not possible
print(x.a,x.b)
print(y.c)
'''
'''
Accessing one class from another class using self refernce variable
---------------------------------------------------------------------
'''
'''
class Outcls:
	def __init__(self):
		print("This is outer class.")
		self.incls = self.Incls()
	class Incls:
		def __init__(self):
			print("This is inner class.")
o = Outcls()
'''

'''
Inner methods: -
-------------
'''
'''
class A:
	def m1():								#Outer method
		print("This is outer method.")
		def m2():							#Inner method
			print("This is inner method.")
		m2()								#Inner method can be call inside that method which is created.
A.m1()
'''

'''
Garbage Collector: -
-----------------
	It is used to automatically free up memory space that has been allocated to the object which is no longer needed.

Q) How to enable and disable garbage collector ?
Ans) By default garbage collector is enabled. Garbage collection is done through gc module.
	gc.isenabled()	---> Returns true is GC is enalbed.
	gc.enable()		---> Explictly enable GC.
	gc.disable()	---> Explictly disable GC.
'''

'''
Destructor: -
----------
	1. It is called by garbage collector just to destroy object or dealocation.
	2. It is denoted by __del__(self):
	3. It is executed just before destorying an object
'''
'''
import time as t
class A:
	def __init__(self):
		print("Object Created . . .")
	def __del__(self):
		print("Object Destoryed . . .")
a = A()
t.sleep(10)		#After execution of last line object will be destroyed.
				#It is only timer to slow the execution.
'''

