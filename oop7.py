#! /usr/bin/python3
'''
Instance Method: -
----------------
	1. It needs at least one instance variable.
    2. To access within the class use self and outside the class use object reference.
    3. No decorator is needed.
    4. Can access both instance and static variable.
    5. Uses self which is reference to current class object.
'''
'''
class Student:
	def __init__(self,name,marks):
		self.marks = marks  #reference variable
		self.name = name    #reference variable
# Instance methods
	def display(self):
		print('Hi',self.name,'your marks is',self.marks)
		self.rank()
	def rank(self):
		if self.marks >= 60:
			print('You are 1st')
		elif self.marks >= 50:
			print('You are 2nd')
		elif self.marks >= 35:
			print('You are 3rd')
		else:
			print('You are failed !!!')
s=Student('Debrishi',89.76)
s.display()
'''
'''
Getter and Setter Method: -
------------------------

	1. Another name of getter is accessor and setter is mutator.
	2. It is used if we don't know data at the time of creation of object. But if we know then we use contructor.
'''
'''
class Student:
# Setter method
	def setName(self,name):
		self.name = name
# Getter method
	def getName(self):
		return self.name
s=Student()
s.setName('Hello, World!')
print(s.getName())
'''

'''
Class Methods: -
------------
	1. Use of static variables and @classmethod decorator is needed.
	2. Can access only static variables.
	3. Uses cls which is reference vairalbe to current class object.
	4. To access class method either by using class name or object reference (outside the class)
'''
'''
class Student:
	@classmethod
	def fun1(calf,name,age):
		calf.name = name
		calf.age = age
	@classmethod
	def fun2(calf):
		return calf.name,calf.age
s = Student()
s.fun1('rahul',25)
print('Your name is',s.fun2()[0],'and your age is',s.fun2()[1])
'''

'''
Static method: -
-------------
	1.
'''