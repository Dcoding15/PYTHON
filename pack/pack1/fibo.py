#! /usr/bin/python3
def fibo():
	n1, n2 = 0, 1
	n3 = 0
	c = int(input("Enter range: "))
	while(c):
		n3 = n1 + n2
		print(n1,end=" ")
		n1 = n2
		n2 = n3
		c -= 1
	print()
