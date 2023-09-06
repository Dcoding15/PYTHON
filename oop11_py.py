#! /usr/bin/python3
'''
Encapsulation: -
-------------

	Abstract method: -
	---------------
		1. It is a method that is only decalared but not implemented by itself. It forces child class for implementation.
		2. It can be declared using @abstractmethod decorator which is imported from abc module.
		Example:-
		-------
		from abc import abstractmethod
		class A:
			@abstractmethod
			def fun1():		#This is declaration of abstract method
				pass
		class B(A):
			def fun1():
				print('This is an example of abstract method . . .')
		B.fun1()

	Abstract class: -
	--------------
		1. Partial implementation of class is known as abstract class.
		2. It can be declared using ABC (Abstract Base Class) class which is parent class of all  from abc module
		3. We can create object for abstract class if abstract method is not present and vice versa.
		4. It can contain zero number of abstract methods.
		5. We can call abstract method only by class name.
		6. It can contain both abstract and non-abstract methods.
		Example:-
		-------
		from abc import abstractmethod,ABC
		class A(ABC):			#This is declaration of abstract class
			@abstractmethod		#This is declaration of abstract method
			def fun1():
				pass
		class B(A):
			def fun1():
				print('This is an example of abstract class and method . . .')
		B.fun1()
	
	Interface: -
	---------
		1.
'''
