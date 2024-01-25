#! /usr/bin/python3

class student:

# __init__(self, name, age, state) <-- it is use to make constructor for variable.
# Instance variable are declared inside the constructor.
# Class variables are declared inside a class and outside a method.

	pincode = 700097	# class variable

	def __init__(self, name, age, state):
		self.name = name	# Instance variable
		self.age = age		# Instance variable
		self.state = state	# Instance variable

	def display(self, pincode):
		print('My name is',self.name,'\nMy age is',self.age,'\nI live in',self.state,'\nMy pincode is',pincode)



print(student.pincode)
# Output: 700097

student('Debrishi Biswas', 19, 'Kolkata').display(210003)
'''

Output: -

My name is Debrishi Biswas
My age is 19
I live in Kolkata
My pincode is 210003

'''
