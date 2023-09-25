#! /usr/bin/python3

'''
Using member of one class into another class: -
--------------------------------------------
	1. By using composition
	2. By using inheritance
'''

'''
Composition: -
-----------

	1. It is also known as HAS-A relationship.
	2. Other class of member can be access by simply by class_name.class_member or using object reference variable.
	3. Classes that contain objects of other classes is called composites, contained object. Classes that are used to create more complex types is called components, container object.
	4. Both composite and container has a strong relationship.
	5. Create object of another class inside any class.
'''
'''
class A:
	def thisA():
		print("This is class A")
	def thisB():
		B.thisB()
	def thisC(self):
		self.c = C.thisC()
class B:
	def thisB():
		print("This is class B")
class C:
	def thisC():
		print("This is class C")
A.thisA()
A.thisB()
A().thisC()
'''
'''
Aggregation: -
-----------

	1. It is similar as composition but the relationship between composite and container has a weak relationshp.
	2. Create object of another class outside a class.
'''
'''
class A:
	def thisA():
		print("This is class A")
	def thisB(b):
		print(b)
class B:
	c = "This is class B"
A.thisA()
A.thisB(B.c)
'''

'''
Inheritance: -
-----------

	1. It is also known as IS-A relationship.
	2. Other class of member can be access by simply by syntax ===> class child_class_name(parent_class_name_1,parent_class_name_2,...,parent_class_name_N).
	3. Classes that inherit from another class is called derived class, subclass, subtypes. Classes from which other class inherit is called base class, super class.
'''
'''
class A:
	def thisA():
		print("This is class A")
class B:
	def thisB():
		print("This is class B")
class C(A,B):
	def thisC():
		print("This is class C")
C.thisA()
C.thisB()
C.thisC()
'''

'''
Types of Inheritance: -
--------------------
	1. Single
	2. Multi-level
	3. Hierarchical
	4. Multiple
	5. Hybrid
	6. Cyclic
'''

'''
Single Inheritance: One child class inherent from one parent class.
'''
'''
class Parent:
	def infoParent():
		return "Parent Class"
class Child(Parent):
	def infoChild():
		return "Child Class"
	def display():
		print(Child.infoParent(),'<---',Child.infoChild())
Child.display()
'''

'''
Multi-level Inheritance: One child class inherent from one parent class and that parent class inherent from one grandparent class and so on.
'''
'''
class GrandParent:
	def infoGrandParent():
		return "GrandParent Class"
class Parent(GrandParent):
	def infoParent():
		return "Parent Class"
class Child(Parent):
	def infoChild():
		return "Child Class"
	def display():
		print(Child.infoGrandParent(),'<---',Child.infoParent(),'<---',Child.infoChild())
Child.display()
'''

'''
Hierarchical Inheritance: Two or more child class inherent from one parent class.
'''
'''
class Parent:
	def infoParent():
		return "Parent Class"
class Child1(Parent):
	def infoChild1():
		return "Child1 Class"
	def display():
		print(Child1.infoParent(),'<---',Child1.infoChild1())
class Child2(Parent):
	def infoChild2():
		return "Child2 Class"
	def display():
		print(Child2.infoParent(),'<---',Child2.infoChild2())
Child1.display()
Child2.display()
'''

'''
Multiple Inheritence: One child class inherent from two or more parent class.
'''
'''
class Parent1:
	def infoParent1():
		return "Parent1 Class"
class Parent2:
	def infoParent2():
		return "Parent2 Class"
class Child(Parent1, Parent2):
	def infoChild():
		return "Child Class"
	def display():
		print(Child.infoParent1(),'<---',Child.infoChild())
		print(Child.infoParent2(),'<---',Child.infoChild())
Child.display()
'''

'''
Hybrid Inheritance: It is the combination all type of inheritance.
Cyclic Inheritance: One class is inherent from its own class. (It is not required)
'''

'''
Method Resolution Order (MRO): -
-----------------------------

	1. The process of deciding method for method call.
	2. It is an in-built function.
	3. It uses MRO algorithm which is also known as C3 algorithm.
'''
'''
class A:
	pass
class B(A):
	pass
class C(A):
	pass
class D(B,C):
	pass
print("Class A:",A.mro())
print("Class B:",B.mro())
print("Class C:",C.mro())
print("Class D:",D.mro())
'''

'''
super(): -
-------
	1. It is an built-in function to call parent class memberes expicitly from child class. 
	2. If parent and child class has member with same name then super() is required to avoid naming conflict.
    3. super(class_name,self).method_name() ===> It will call method_name() of parent class of class_name into current object.
    4. We can't access parent class instance variable. We can access by self variable only.
    5. Under one object one instance vairable possible with same name.
		Example: -
		-------
		class A:
			def __init__(self):
				self.a = 10

		class B(A):
			def __init__(self):
				self.a = 100
				super().__init__()		#Here value of instance variable a is change to 10
			def m1(self):
				print(self.a)

		b = B()
		b.m1()							#Output: 10
    6. From instance method of child class by using super() we can call parent class --> constructor, instance method, class method, static method.
	   From class method of child class by using super() we can call parent class --> class method, static method.
       From static method of child class by using super() we can't call parent class members.
    7. Indirectly calling parent class --> constructor, instance method from child class using super()
		Example: -
        -------
        class A:
			def __init__(self):
			print("Class A contructor.")
			print('constructor self address: ',id(self))
		def m1(self):
			print("Class A instance method.")
			print('instance method self address: ',id(self))
		
        class B(A):
			@classmethod
			def m1(cls):
				super(B,cls).__init__(cls)
				super(B,cls).m1(cls)
				print('cls address: ',id(cls))
		
        B.m1()
										#Output: -
										#Class A contructor.
										#constructor self address:  20046000
										#Class A instance method.
										#instance method self address:  20046000
										#cls address:  20046000
    8. Indirectly calling parent class --> static method from child class using super()
		Example: -
        -------
        class A:
			@staticmethod
			def m1():
				print('Class A static method')
		class B(A):
			@staticmethod
				def m2():
				super(B,B).m1()
		B.m2()
										#Output: -
                                        #Class A static method
'''
