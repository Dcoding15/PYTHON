#! /usr/bin/python3
'''
1. Aliasing: -
   --------
   	(a) Creating duplicate reference vairable. If any changes perform to a refernce variable then reference variable will get affected.
   	(b) It can be performed by simply assigning value from one reference variable to another.
   		For example: -
   			l1 = [10,20,30,40]
   			l2 = l1

2. Cloning: -
   ------
	(a) Creating duplicate list object.
	(b) It can be performed by using copy()
		For example: -
			l1 = [10,20,30,40]
			l2 = l1.copy()

3. Deep Cloning and Shallow Cloning: -
   --------------------------------
   	Aliasing ---> Shallow Cloning
   	Cloning	 ---> Deep Cloning

   	(a) Shallow cloning is done using copy() of copy module. It refers to same address of object. Only nested objects will be affected if any nested object value change.
   	(b) Deep cloning is done using deepcopy() of copy module. It refers to different address of object. Only nested object will not be affected if any nested object value change.
'''