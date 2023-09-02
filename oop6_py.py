'''
Class: It acts as a plan /  model / blue print / design for objects.
Object: A physical existence of a class.
Reference Variable: It can be used to refer objects and can invoke functionalities of objects. We can create multiple reference variable for a single object.

class name_of_class:
	Documentation string quoted with triple single/double quotes.
	properties (variables)
	actions (methods/behaviour)

print(name_of_class) <-- This will print the doc string of the class

Every object has properties and behaviour. Properties are described by variables. Behaviours are described by methods.

Types of variables in class: -
---------------------------

	1. Instance Variables (Object Level)
	2. Static Variables	  (Class Level)
	3. Local Variables    (Method Level)

Types of methods in class: -
-------------------------

	1. Instance Methods (Instance, Static, Local variable related method)
	2. Class Methods	(Static, Local variable related method)
	3. Static Methods   (Local variable related method)
'''

class Student:
	def __init__(self):		#This is python constructor
		self.name = 'Debrishi'
		self.rollno = 195
		self.marks = 95
	def talk(self):
		print('Hello I am ',self.name,'.')
		print('My roll number is ',self.rollno,'.')
		print('I got ',self.marks,' in semester exam.')

s1 = Student()  #Here s1 is reference variable and Student() is object creation syntax
print(s1.name)  #Access of class variables
s1.talk()       #Access of class methods

'''

self / or any name (not recommended) -->  reference variable to current object
cls  / or any name (not recommended) -->  reference variable to class object

'''
class Student:
    ''' This is Student Class doc string . . . . . . . '''
    collegeName ='Brainware University'  #StaticVariable
    collegeLocation = 'Barasat'          #StaticVariable
    def __init__(self,name,rollno):
        self.name = name            #InstanceVariable
        self.rollno = rollno        #InstanceVariable

    def getStudentInfo(self):           #InstanceMethods
        print('Student name:',self.name)
        print('Student rollno:',self.rollno)

    def mthd1(self):                       #InstanceMethods
        self.address = 'Kolkata'           #InstanceVariable

#    Note: We can declare and initialize instance variables inside instance methods but that variable will not act until we call that instance methods with a reference variable.

    @classmethod                        #We have to declare @classmethod decorator so that PVM can consider the below method as class method
    def getCollegeInfo(cls):            #ClassMethods
        print('College name:',cls.collegeName)
        print('College location:',cls.collegeLocation)

#    Note: In every class there is one special object created by python virtual machine (PVM) i.e., class object. These type of objects hold class level data. Class level object can be created only once.


    @staticmethod                       #We have to devlare @staticmethod decorator so that PVM (Python Virtual Machine) can consider the below method as static method
    def getAverage(a,b,c):              #StaticMethods
        return (a + b + c) / 3

s1 = Student('Debrishi Biswas', 195)
# s1.getStudentInfo()
# s1.getCollegeInfo()
print(s1.__doc__)                       #Prining documnation string which is within the class.
print(s1.__dict__)                      #Printing instance variables related to the reference / class.
s1.pincode = 785546                     #We can declare and initialize instance variables outside class using reference variable.
print(s1.__dict__)
s1.mthd1()
print(s1.__dict__)
# print(s1.getAverage(10,20,30))

'''
Note: Here, self is not a keyword ( it is a variable ) which provide value automatically by Python Virtual Machine at runtime.
	  Whenever we are creating an object constructor will automatically executed.
	  We can give any name other name to variable (in exchange of self).
	  __init__() and __init__.py file has no relation.

About self variable: -
-------------------

	1. self variable is a reference varialble which is always pointing to current object.
	2. Within python class to access the current object, we can use self variable.
	3. The first argument to the construcutor / instance method is always pointing to current object. <---- (V.V.Imp)
	4. We are not requied to provide value for self variable, PVM itself will provide value.
	5. We can use self within the class only. Inside constructor and instance method we can use self to declare instance variables and access instance variables respectively.

About instance variable: -
-----------------------

	1. It is varied from object to object i.e., for every object seperate copy of instance variable will be created.
	2. We can declare/access the instance varible outside the class using object reference.
	3. We can delete instance variable within the class / outside of class as del self.variable_name / del object_reference.variable_name respectively.
	4. We can update instance varible within the class / outside the class as self.variable_name = value / object_reference.variable_name = value repectively.

About static variable: -
---------------------

	1. We can update the value of static variable either by class name or cls variable and class method, static method.
	   For example: -
	   class Test:
			a=10
			@classmethod
			def m1(cls):
				cls.a=20
			@staticmethod
			def m2():
				Test.a=30
		Test.m1()
		print(Test.a)	#output: 20
		Test.m2()
		print(Test.a)	#output: 30
		Test.a=40
		print(Test.a)	#output: 40
	2. We can't use self or object reference to update static variable value. If we going to update using self or object reference variable then a new object will be created and we have to use that new object to update static variable.
	   For example: -
	   class Test:
			a=10
			def m3(self):
				self.a=20
		t = Test()
		t.m3()
		print(Test.a)	#output: 10
		print(t.a)		#output: 20
	3. We can declare static variable within the class directly but outside of any method.
	4. We can declare static variable within constructor and instance method using class name.
	5. We can declare static variable within class method using class name or cls variable.
	6. We can declare static variable within static method using class name.
	7. We can declare static variable outside class by using class name and within the class we can declare directly.
	8. We can access static variable using class name, cls variable, self varialbe, object reference.
	9. We can delete static variable using class name, cls variable. For example: del class_name.variable_name (it is applicable anywhere), del cls.variable_name (it is applicable only in classmethod).

	About local variable: -
	--------------------
	1. It can be declared inside a method directly.
	2. It will be created and destoryed at the time of execution of execution of method.
	3. It can't be accessed from outside of the method.
'''
