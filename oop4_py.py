#! /usr/bin/python3

# Abstraction in Python
# Prevent an user from creating an object of that class and it compels user to override abstract methods in child class.
# abstract class = a class which contain one or more abstract methods.
# abstract method = a method that has declaration but does not have any implementation.
# To use abstraction we have to use abc (abstract class) module in Python.

from abc import *

class A(ABC):

	@abstractmethod
	def display():
		pass

class B(A):
	def display():
		print('This is from class B after inherting display() from abstract class A')

class C(A):
	def display():
		print('This is from class C after inherting display() from abstract class A')

class D(A):
	def display():
		print('This is from class D after inherting display() from abstract class A')

B.display()
C.display()
D.display()