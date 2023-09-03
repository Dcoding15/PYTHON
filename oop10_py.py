#! /usr/bin/python3

'''
Polymorphism: -
------------

    1. Poly means many and morphism means form. It means one thing have the ability to display many form.
    2. There are two types of polymophism: -
        (a) Overloading
            i)  Operator overloading: -
                --------------------
                Same operator but different purposes.

                + operator: -
                ----------
                    10 + 20       ===> Addition
                    'abc' + 'def' ===> String Concatenation
                
                * operator: -
                ----------
                    10 * 20        ===> Multiplication
                    'abc' * 10     ===> String Multiplication

                Note: We have to explicitly overiding operator using dunder or magic method at time of using objects.

            ii) Method overloading: -
				------------------
				Two or more methods are said to be overloaded iff methods having same name but different parameters. But in python method overloading is not applicable. If we are trying to declare multiple method with same name then PVM will consider the latest one.

            iii) Constructor overloading: -
				 -----------------------
				 Same of method overloading . . .

        (b) Overrinding
            i) Method overriding: -
			   -----------------
			   Child class have method of same name as parent class but have different definition.
			   Example: -
			   class A:
					def m1():
						print('This is class A method . . .')

				class B(A):
					def m1():		#Here method m1() from class A have been override.
						print('This is class B method . . .')

				B.m1()

            ii) Constructor overriding: -
				----------------------
				Child class constructor overrides the property of parent constructor.
				Example: -
				class A:
	def __init__(self):
		print('This is class A contructor . . .')

class B(A):
	def __init__(self):		#Here method __init__() from class A have been override.
		print('This is class B constructor . . .')

b=B()
'''
