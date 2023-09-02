'''
About python contructor: -
-----------------------

	1. Constructor is a simple method and it is optional within class.
	2. The name of the constructor is always __inti__().
	3. Constructor automatically executed when we are creating an object i.e., we are not required to call contructor explicitly.
	4. If we are creating only one object then the constructor will we executed only once.
	5. The main purpose of constructor is to declare and initialize instance variable in constructor.
	6. In constructor after non-default argument there should not be any default argument. After default argument non-default argument can follow.
	7. If __init__() is not there within class then default contructor will be executed.
		For example: -
		-----------
		class Test:
			def m1(self):
				print('This is default constructor . . . .')

		t = Test()   <-- Here default constructor will be executed by PVM.
	8. We can call constructor explicitly, then it will be executed just as normal method and new object won't be created.
		For example: -
		-----------
		class Test:
			def __init__(self):
				print('Constructor is calling explicity . . . .')

		t = Test()
		t.__init__()
	9. Constructor overloading is not possible in python. If we create more than one constructor in same class then PVM will only consider the last constructor.
	10. Reinitilization using __init__() externally.
		For example: -
		-----------
		class Test:
			def __init__(self,name):
				self.name = name
		t = Test('XYZ')
		print(t.name)	<-- Output: XYZ
		t.__init__('xyz')
		print(t.name)	<-- Output: xyz
'''

class Test:
    def __init__(self,name):
        self.name = name
