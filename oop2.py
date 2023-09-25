#! /usr/bin/python3

# Example of super() in inheritance

class Square:
	def __init__(self, side):
		self.width = side

	def area(self):
		aos = self.width ** 2
		print('Area of square whose side =',self.width,'is',aos)

class Rectangle(Square):
	def __init__(self, length, width):
		super().__init__(width)
		self.length = length

	def area(self):
		aor = self.length * self.width
		print('Area of rectangle whose length =',self.length,'and width =',self.width,'is',aor)


Square(10).area()
Rectangle(10, 20).area()
'''

Output: -

Area of square whose side = 10 is 100
Area of rectangle whose length = 10 and width = 20 is 200

'''
