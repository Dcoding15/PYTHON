#! /usr/bin/python3

'''
Public, Private and Protected member: -
------------------------------------
	1. Public members: -
	   --------------
			(i) Those members which can be access either within the class or outside the class.
			(ii) Everybody inside the class are bydefault public.
		Example:-
		-------
		class A:
			def __init__(self):
				self.a = 10			#public variable
			def fun1():				#public method
				print('This is class A')

	2. Private members: -
	   ---------------
			(i) Those members which can be access only within the class.
			(ii) We can declare them by using double underscore as name prefix.
			(iii) We can't access private members normally by only creating an object. We have to use objectName._className__privateVariableName and objectName._className__privateMethodName()
		Example:-
		-------
		class A:
			def __init__(self):
				self.__a = 10			#private variable
			def __fun1():				#private method
				print('This is class A')

		print(A()._A__a)
		A()._A__fun1()

	3. Protected members: -
	   -----------------
	   		(i) Those member which can be access only within the same class and child class.
			(ii) We can declare them by using single underscore as name prefix.
			(iii) We can't access protected member normally by only creating an object.
		Example:-
		-------
		
'''