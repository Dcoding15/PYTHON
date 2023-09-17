#! /usr/bin/python3

# Example of method chaining

class Calculator:
	def __init__(self):
		self.updatedCalc = int(input("Enter a number: "))
	def add(self):
		self.num = int(input("Enter a number: "))
		self.updatedCalc += self.num
		return self
	def subtract(self):
		self.num = int(input("Enter a number: "))
		self.updatedCalc -= self.num
		return self
	def multiplication(self):
		self.num = int(input("Enter a number: "))
		self.updatedCalc *= self.num
		return self
	def division(self):
		try:
			self.num = int(input("Enter a number: "))
			self.updatedCalc /= self.num
		except (ZeroDivisionError):
			print("You can't divided by zero")
		return self
	def power(self):
		self.num = int(input("Enter a number: "))
		self.updatedCalc **= self.num
		return self
	def display(self):
		print("Answer: ",self.updatedCalc)