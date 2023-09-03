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
			   When child class have method of same name as parent class but have different definition.

            ii) Constructor overriding: -
				----------------------
'''
